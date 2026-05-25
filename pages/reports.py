import streamlit as st
import pandas as pd
import plotly.express as px

from database.db import get_connection
from utils.sidebar import load_sidebar
from utils.styles import load_css
load_css()
load_sidebar()
# =========================
# Page Title
# =========================

st.title("📅 Financial Reports")

st.markdown(
    "Analyze your income and expenses by time period."
)

# =========================
# Database Connection
# =========================

conn = get_connection()

df = pd.read_sql_query(
    "SELECT * FROM transactions",
    conn
)

conn.close()

# =========================
# Empty Check
# =========================

if df.empty:

    st.warning("No transaction data found.")

else:

    # =========================
    # Date Conversion
    # =========================

    df["date"] = pd.to_datetime(
        df["date"]
    )

    # =========================
    # Report Selector
    # =========================

    report_type = st.selectbox(
        "📌 Select Report Type",
        [
            "Weekly",
            "Monthly",
            "Yearly"
        ]
    )

    # =========================
    # WEEKLY REPORT
    # =========================

    if report_type == "Weekly":

        df["week"] = (
            df["date"]
            .dt.strftime("%Y-%U")
        )

        grouped = (
            df.groupby(
                ["week", "type"]
            )["amount"]
            .sum()
            .reset_index()
        )

        latest_week = grouped["week"].max()

        report_df = grouped[
            grouped["week"] == latest_week
        ]

        latest_date = df["date"].max()

        formatted_date = latest_date.strftime(
            "%A, %d %B %Y"
        )

        st.subheader(
            f"📅 Weekly Report - {formatted_date}"
        )

    # =========================
    # MONTHLY REPORT
    # =========================

    elif report_type == "Monthly":

        df["month"] = (
            df["date"]
            .dt.strftime("%Y-%m")
        )

        grouped = (
            df.groupby(
                ["month", "type"]
            )["amount"]
            .sum()
            .reset_index()
        )

        latest_month = grouped["month"].max()

        report_df = grouped[
            grouped["month"] == latest_month
        ]

        latest_date = df["date"].max()

        formatted_month = latest_date.strftime(
            "%B %Y"
        )

        st.subheader(
            f"📅 Monthly Report - {formatted_month}"
        )

    # =========================
    # YEARLY REPORT
    # =========================

    else:

        df["year"] = (
            df["date"]
            .dt.strftime("%Y")
        )

        grouped = (
            df.groupby(
                ["year", "type"]
            )["amount"]
            .sum()
            .reset_index()
        )

        latest_year = grouped["year"].max()

        report_df = grouped[
            grouped["year"] == latest_year
        ]

        latest_date = df["date"].max()

        formatted_year = latest_date.strftime(
            "%Y"
        )

        st.subheader(
            f"📅 Yearly Report - {formatted_year}"
        )

    # =========================
    # Financial Metrics
    # =========================

    income = report_df[
        report_df["type"] == "Income"
    ]["amount"].sum()

    expense = report_df[
        report_df["type"] == "Expense"
    ]["amount"].sum()

    balance = income - expense

    # =========================
    # KPI Cards
    # =========================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "💰 Income",
            f"₹ {income:,.2f}",
            border=True
        )

    with col2:

        st.metric(
            "💸 Expense",
            f"₹ {expense:,.2f}",
            border=True
        )

    with col3:

        st.metric(
            "🏦 Balance",
            f"₹ {balance:,.2f}",
            border=True
        )

    st.divider()

    # =========================
    # Income vs Expense Chart
    # =========================

    st.subheader("📊 Income vs Expense")

    fig = px.bar(
        report_df,
        x="type",
        y="amount",
        color="type",
        title=f"{report_type} Financial Overview"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # =========================
    # Smart Insights
    # =========================

    st.subheader("🤖 Smart Insights")

    if expense > income:

        st.error(
            "⚠️ Expenses exceeded income during this period."
        )

    else:

        st.success(
            "✅ Financial balance is healthy."
        )

    savings = income - expense

    if savings > 0:

        st.info(
            f"💰 Estimated savings: ₹ {savings:,.2f}"
        )

    if expense > 5000:

        st.warning(
            "📉 High spending detected during this period."
        )

    st.divider()

    # =========================
    # Raw Report Data
    # =========================

    st.subheader("📜 Report Data")

    st.dataframe(
        report_df,
        use_container_width=True
    )