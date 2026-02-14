import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIG
st.set_page_config(
    page_title="TradeMind",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== CSS PERSONALIZADO =====
st.markdown("""
<style>
body {
    background-color: #F4F6F9;
}
[data-testid="stSidebar"] {
    background-color: #0B1F3A;
}
.sidebar-title {
    color: white;
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 30px;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}
.big-number {
    font-size: 28px;
    font-weight: 600;
}
.section-title {
    font-size: 26px;
    font-weight: 600;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ===== SIDEBAR =====
with st.sidebar:
    st.markdown("<div class='sidebar-title'>TRADEMIND</div>", unsafe_allow_html=True)
    menu = st.radio(
        "",
        ["📊 Dashboard", "🔎 Inteligência NCM", "🤖 Assistente IA", "🏢 Quem Somos"]
    )
    st.markdown("---")
    st.write("© 2026 TradeMind")

# ===== DASHBOARD =====
if menu == "📊 Dashboard":
    st.markdown("<div c
