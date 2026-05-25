import streamlit as st
import pandas as pd

from database.db import get_connection
from utils.sidebar import load_sidebar
from utils.styles import load_css
load_css()
load_sidebar()
st.title("📜 Transaction History")

st.markdown("View, search, and manage all transactions.")

# Database Connection
conn = get_connection()

# Load Data
df = pd.read_sql_query(
    "SELECT * FROM transactions",
    conn
)

# No Data
if df.empty:

    st.warning("No transactions found.")

else:

    # =========================
    # Search Filter
    # =========================

    search = st.text_input(
        "🔍 Search by Category or Description"
    )

    if search:

        df = df[
            df["category"].str.contains(
                search,
                case=False,
                na=False
            )
            |
            df["description"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    # =========================
    # Transaction Table
    # =========================

    st.subheader("📊 All Transactions")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    # =========================
    # Delete Transaction
    # =========================

    st.subheader("🗑️ Delete Transaction")

    transaction_ids = df["id"].tolist()

    selected_id = st.selectbox(
        "Select Transaction ID",
        transaction_ids
    )

    if st.button("Delete Transaction"):

        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM transactions WHERE id = ?",
            (selected_id,)
        )

        conn.commit()

        st.success(
            f"✅ Transaction ID {selected_id} deleted successfully!"
        )

        st.rerun()

    st.divider()

    # =========================
    # Export CSV
    # =========================

    st.subheader("⬇️ Export Report")

    csv = df.to_csv(index=False)

    st.download_button(
        label="Download CSV Report",
        data=csv,
        file_name="expense_report.csv",
        mime="text/csv"
    )

conn.close()