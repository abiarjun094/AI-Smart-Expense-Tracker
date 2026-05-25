import streamlit as st
import pandas as pd

from database.db import get_connection
from utils.sidebar import load_sidebar
from utils.styles import load_css
load_css()
load_sidebar()
st.title("🎯 Budget Management")

st.markdown("Set and monitor your monthly spending budget.")

# Database Connection
conn = get_connection()

cursor = conn.cursor()

# Get Existing Budget
cursor.execute(
    "SELECT monthly_budget FROM budget ORDER BY id DESC LIMIT 1"
)

budget_data = cursor.fetchone()

current_budget = 0

if budget_data:
    current_budget = budget_data[0]

# Set Budget Form
with st.form("budget_form"):

    monthly_budget = st.number_input(
        "Set Monthly Budget (₹)",
        min_value=0.0,
        value=float(current_budget),
        format="%.2f"
    )

    save_budget = st.form_submit_button(
        "Save Budget"
    )

# Save Budget
if save_budget:

    cursor.execute("""
    INSERT INTO budget (monthly_budget)
    VALUES (?)
    """, (monthly_budget,))

    conn.commit()

    st.success("✅ Budget Saved Successfully!")

# Fetch Expense Data
df = pd.read_sql_query(
    "SELECT * FROM transactions",
    conn
)

conn.close()

# Calculate Expenses
if not df.empty:

    total_expense = df[
        df["type"] == "Expense"
    ]["amount"].sum()

    remaining_budget = current_budget - total_expense

    st.divider()

    st.subheader("📊 Budget Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "💰 Monthly Budget",
            f"₹ {current_budget:,.2f}"
        )

    with col2:
        st.metric(
            "💸 Total Expenses",
            f"₹ {total_expense:,.2f}"
        )

    with col3:
        st.metric(
            "🏦 Remaining Budget",
            f"₹ {remaining_budget:,.2f}"
        )

    # Progress Bar
    if current_budget > 0:

        progress = min(
            total_expense / current_budget,
            1.0
        )

        st.progress(progress)

    # Alerts
    if total_expense > current_budget:

        st.error(
            "⚠️ Budget Exceeded!"
        )

    elif total_expense > current_budget * 0.8:

        st.warning(
            "⚠️ You have used more than 80% of your budget."
        )

    else:

        st.success(
            "✅ Budget is under control."
        )