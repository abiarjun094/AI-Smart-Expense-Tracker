import streamlit as st
import pandas as pd
import plotly.express as px

from database.db import get_connection
from utils.insights import generate_insights
from utils.sidebar import load_sidebar
from utils.styles import load_css
load_css()

# =====================================
# LOAD SIDEBAR
# =====================================

load_sidebar()

# =====================================
# PAGE HEADER
# =====================================

st.markdown("""
# 💰 AI Smart Expense Tracker

### AI-Based Personal Financial Management Dashboard
""")

st.markdown("""
Manage your:

- 💸 Expenses
- 💰 Income
- 📈 Financial Analytics
- 🎯 Budgets
- 📅 Reports
- 🤖 AI Insights

with a modern interactive dashboard.
""")

st.divider()

# =====================================
# DATABASE CONNECTION
# =====================================

conn = get_connection()

df = pd.read_sql_query(
    "SELECT * FROM transactions",
    conn
)

conn.close()

# =====================================
# EMPTY CHECK
# =====================================

if df.empty:

    st.warning("⚠️ No transactions found.")

else:

    # =====================================
    # CALCULATIONS
    # =====================================

    total_income = df[
        df["type"] == "Income"
    ]["amount"].sum()

    total_expense = df[
        df["type"] == "Expense"
    ]["amount"].sum()

    balance = total_income - total_expense

    # =====================================
    # TOP CARDS
    # =====================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div style="
            background: linear-gradient(
                145deg,
                #052e16,
                #14532d
            );
            padding: 25px;
            border-radius: 20px;
            border: 1px solid #166534;
        ">
            <h4>💰 Total Income</h4>
        """, unsafe_allow_html=True)

        st.metric(
            "",
            f"₹ {total_income:,.2f}"
        )

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div style="
            background: linear-gradient(
                145deg,
                #450a0a,
                #7f1d1d
            );
            padding: 25px;
            border-radius: 20px;
            border: 1px solid #991b1b;
        ">
            <h4>💸 Total Expense</h4>
        """, unsafe_allow_html=True)

        st.metric(
            "",
            f"₹ {total_expense:,.2f}"
        )

        st.markdown("</div>", unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div style="
            background: linear-gradient(
                145deg,
                #172554,
                #1e3a8a
            );
            padding: 25px;
            border-radius: 20px;
            border: 1px solid #2563eb;
        ">
            <h4>🏦 Current Balance</h4>
        """, unsafe_allow_html=True)

        st.metric(
            "",
            f"₹ {balance:,.2f}"
        )

        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    # =====================================
    # QUICK FEATURE CARDS
    # =====================================

    card1, card2, card3 = st.columns(3)

    with card1:

        st.markdown("""
        <div style="
            background: #0f2747;
            padding: 20px;
            border-radius: 18px;
            border: 1px solid #1d4ed8;
            text-align: center;
        ">
            <h3>📊 Interactive Analytics Dashboard</h3>
        </div>
        """, unsafe_allow_html=True)

    with card2:

        st.markdown("""
        <div style="
            background: #052e16;
            padding: 20px;
            border-radius: 18px;
            border: 1px solid #15803d;
            text-align: center;
        ">
            <h3>🎯 Smart Budget Monitoring</h3>
        </div>
        """, unsafe_allow_html=True)

    with card3:

        st.markdown("""
        <div style="
            background: #3f3f0d;
            padding: 20px;
            border-radius: 18px;
            border: 1px solid #ca8a04;
            text-align: center;
        ">
            <h3>🤖 AI Spending Insights</h3>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # =====================================
    # CHARTS SECTION
    # =====================================

    chart_col1, chart_col2 = st.columns(2)

    expense_df = df[
        df["type"] == "Expense"
    ]

    # PIE CHART

    with chart_col1:

        st.subheader("🥧 Expense Categories")

        if not expense_df.empty:

            category_data = (
                expense_df.groupby("category")["amount"]
                .sum()
                .reset_index()
            )

            fig1 = px.pie(
                category_data,
                names="category",
                values="amount",
                hole=0.4
            )

            fig1.update_layout(
                paper_bgcolor="#020817",
                plot_bgcolor="#020817",
                font_color="white"
            )

            st.plotly_chart(
                fig1,
                use_container_width=True
            )

    # BAR CHART

    with chart_col2:

        st.subheader("📈 Income vs Expense")

        summary = (
            df.groupby("type")["amount"]
            .sum()
            .reset_index()
        )

        fig2 = px.bar(
            summary,
            x="type",
            y="amount",
            color="type"
        )

        fig2.update_layout(
            paper_bgcolor="#020817",
            plot_bgcolor="#020817",
            font_color="white"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.divider()

    # =====================================
    # AI INSIGHTS
    # =====================================

    st.subheader("🤖 AI Spending Insights")

    insights = generate_insights(df)

    for insight in insights:

        st.info(insight)

    st.divider()

    # =====================================
    # RECENT TRANSACTIONS
    # =====================================

    st.subheader("📜 Recent Transactions")

    recent_df = df.sort_values(
        by="id",
        ascending=False
    ).head(10)

    st.dataframe(
        recent_df,
        use_container_width=True
    )

    st.divider()

    # =====================================
    # FOOTER
    # =====================================

    st.caption(
        "Developed using Python, Streamlit, SQLite & Plotly 🚀"
    )