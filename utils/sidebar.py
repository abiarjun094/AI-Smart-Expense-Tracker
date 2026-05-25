import streamlit as st


def load_sidebar():

    st.sidebar.image(
        "https://cdn-icons-png.flaticon.com/512/2489/2489756.png",
        width=120
    )

    st.sidebar.markdown("""
    # 💰 Expense Tracker

    ### Smart Financial Management System
    """)

    st.sidebar.markdown("---")

    st.sidebar.success("🚀 AI Powered Analytics")

    st.sidebar.info("📈 Weekly / Monthly Reports")

    st.sidebar.warning("🎯 Smart Budget Tracking")

    st.sidebar.markdown("---")

    st.sidebar.caption(
        "Built using Python & Streamlit"
    )