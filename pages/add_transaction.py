import streamlit as st
from datetime import date

from database.db import (
    get_connection
)

from utils.sidebar import load_sidebar
from utils.styles import load_css
load_css()
load_sidebar()
# =========================
# LOAD SIDEBAR
# =========================

load_sidebar()

# =========================
# PAGE HEADER
# =========================

st.markdown("""
# ➕ Add Transaction

### Add your income or expenses easily.
""")

st.divider()

# =========================
# DATABASE
# =========================

conn = get_connection()

cursor = conn.cursor()

# =========================
# FORM CARD
# =========================

with st.container():

    st.markdown("""
    <div style='
        background: linear-gradient(
            145deg,
            #111827,
            #1E293B
        );
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #334155;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    '>
    """, unsafe_allow_html=True)

    with st.form("transaction_form"):

        col1, col2 = st.columns(2)

        with col1:

            transaction_type = st.selectbox(
                "Transaction Type",
                [
                    "Income",
                    "Expense"
                ]
            )

        with col2:

            category = st.selectbox(
                "Category",
                [
                    "Food",
                    "Travel",
                    "Shopping",
                    "Bills",
                    "Investments",
                    "Entertainment",
                    "Health",
                    "Others"
                ]
            )

        amount = st.number_input(
            "Amount (₹)",
            min_value=0.0,
            format="%.2f"
        )

        description = st.text_input(
            "Description"
        )

        transaction_date = st.date_input(
            "Transaction Date",
            value=date.today()
        )

        st.markdown("<br>", unsafe_allow_html=True)

        submit_button = st.form_submit_button(
            "💾 Save Transaction"
        )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# SAVE DATA
# =========================

if submit_button:

    cursor.execute("""
    INSERT INTO transactions
    (
        type,
        category,
        amount,
        description,
        date
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        transaction_type,
        category,
        amount,
        description,
        transaction_date
    ))

    conn.commit()

    st.success(
        "✅ Transaction Added Successfully!"
    )

conn.close()