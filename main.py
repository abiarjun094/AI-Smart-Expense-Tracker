import streamlit as st

from database.db import create_tables

# ======================================
# DATABASE SETUP
# ======================================

create_tables()

# ======================================
# PAGE CONFIGURATION
# ======================================

st.set_page_config(
    page_title="AI Smart Expense Tracker",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================
# LOAD CUSTOM CSS
# ======================================

def load_css():

    with open("assets/styles.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ======================================
# SIDEBAR
# ======================================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2489/2489756.png",
    width=120
)

st.sidebar.markdown("""
# 💰 Expense Tracker

### Smart Financial Management System
""")

st.sidebar.markdown("---")

st.sidebar.success("🚀 AI-Powered Expense Analytics")

st.sidebar.markdown("""
### 📌 Features

- 📊 Dashboard  
- ➕ Add Transactions  
- 📈 Analytics  
- 🎯 Budget Management  
- 📅 Reports  
- 📜 History  
- 🤖 AI Insights  
""")

st.sidebar.markdown("---")

st.sidebar.info(
    "Use the sidebar navigation above to explore all modules."
)

# ======================================
# MAIN HOME PAGE
# ======================================

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

# ======================================
# QUICK OVERVIEW CARDS
# ======================================

col1, col2, col3 = st.columns(3)

with col1:

    st.info(
        "📊 Interactive Analytics Dashboard"
    )

with col2:

    st.success(
        "🎯 Smart Budget Monitoring"
    )

with col3:

    st.warning(
        "🤖 AI Spending Insights"
    )

st.divider()

# ======================================
# FEATURES SECTION
# ======================================

st.subheader("🚀 Project Features")

feature_col1, feature_col2 = st.columns(2)

with feature_col1:

    st.markdown("""
    ✅ Add Income & Expenses  
    ✅ SQLite Database Integration  
    ✅ Interactive Charts  
    ✅ Financial Analytics  
    ✅ Weekly / Monthly Reports  
    """)

with feature_col2:

    st.markdown("""
    ✅ AI Spending Insights  
    ✅ Budget Management  
    ✅ CSV Export  
    ✅ Responsive UI  
    ✅ Professional Dashboard  
    """)

st.divider()

# ======================================
# TECHNOLOGY STACK
# ======================================

st.subheader("🛠️ Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.success("🐍 Python")

with tech2:
    st.info("🎨 Streamlit")

with tech3:
    st.warning("🗄️ SQLite")

with tech4:
    st.error("📊 Plotly")

st.divider()

# ======================================
# FOOTER
# ======================================

st.caption(
    "Developed using Python, Streamlit, SQLite, Pandas & Plotly 🚀"
)