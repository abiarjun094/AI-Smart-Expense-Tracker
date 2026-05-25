import streamlit as st
import pandas as pd

from database.db import get_connection
from utils.sidebar import load_sidebar
from utils.styles import load_css
load_css()
load_sidebar()
from utils.charts import (
    category_pie_chart,
    income_expense_chart,
    monthly_trend_chart
)

st.title("📈 Analytics Dashboard")

st.markdown("Visualize your financial data.")

# Database Connection
conn = get_connection()

df = pd.read_sql_query(
    "SELECT * FROM transactions",
    conn
)

conn.close()

# No Data
if df.empty:

    st.warning("No transaction data found.")

else:

    expense_df = df[df["type"] == "Expense"]

    # Pie Chart
    st.subheader("🥧 Category Spending")

    pie_chart = category_pie_chart(
        expense_df
    )

    st.pyplot(pie_chart)

    st.divider()

    # Income vs Expense
    st.subheader("📊 Income vs Expense")

    bar_chart = income_expense_chart(df)

    st.pyplot(bar_chart)

    st.divider()

    # Monthly Trend
    st.subheader("📉 Monthly Expense Trend")

    trend_chart = monthly_trend_chart(
        expense_df
    )

    st.pyplot(trend_chart)