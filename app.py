import streamlit as st
from datetime import datetime

# CONFIGURAÇÃO
st.set_page_config(
    page_title="TradeMind",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== CSS =====
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #0B1F3A;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
}
.big-number {
    font-size: 28px;
    font-weight: 600;
}
.section-title {
    font-size: 26px;
    font-weight: 600;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ===== SIDEBAR =====
with st.sidebar:
    st.markdown("## TRADEMIND")
    menu = st.radio(
        "",
        ["📊 Dashboard", "🔎 Inteligência NCM", "🤖 Assistente IA", "🏢 Quem Somos"]
    )
    st.markdown("---")
    st.caption("© 2026 TradeMind")

# ===== DASHBOARD =====
if menu == "📊 Dashboard":
    st.markdown("<div class='section-title'>Terminal TradeMind</div>", unsafe_allow_html=True)
    st.write(f"Bem-vindo, Igor • {datetime.now().strftime('%d/%m/%Y')}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='card'>
            <div>Dólar</div>
            <div class='big-number'>R
