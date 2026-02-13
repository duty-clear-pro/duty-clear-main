import streamlit as st

# 1. Configuracao de Pagina - TRADEMIND GLOBAL
st.set_page_config(page_title="TradeMind | Global Intelligence", layout="wide")

# 2. CSS - Estilo High-Tech (Marinho, Slate e Ciano)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    
    /* Sidebar Ultra-Dark */
    [data-testid="stSidebar"] { background-color: #020617 !important; border-right: 1px solid #1E293B; }
    
    /* Botoes do Menu */
    .stButton > button {
        width: 100%; border-radius: 8px; height: 48px; font-weight: 600;
        background-color: transparent; color: #94A3B8; border: 1px solid transparent;
    }
    .stButton > button:hover { border: 1px solid #38BDF8; color: #38BDF8; }

    /* Banner Principal - TradeMind */
    .hero-section {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 50px; border-radius: 24px; color: white;
        margin-bottom: 30px; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1);
    }
    
    /* Inputs de Pesquisa */
    .stTextInput input {
        border: 2px solid #0F172A !important; border-radius: 12px !important;
        height: 55px !important; font-size: 18px !important;
    }
    
    /* Cards de Cambio */
    .currency-card {
        background: white; padding: 20px; border-radius: 16px;
        border: 1px solid #E2E8F0; text-align: center;
    }
    .currency-card h4 { color: #64748B; margin: 0; font-size: 14px; }
    .currency-card h2 { color: #0F172A; margin: 5px 0; font-size: 24px; }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Login Simplificada
if 'auth' not in st.session_state: st.session_state.auth = False
if 'aba' not in st.session_state: st.session_state.aba = "Home"

if not st.session_state.auth:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.markdown("<div style='text-align:center;'><h1>TRADEMIND</h1><p>Intelligence for Global Trade</p></div>", unsafe_allow_html=True)
        u = st.text_input("Username")
        p = st.text_input("Access Key", type="password")
        if st.button("SIGN IN", use_container_width=True):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True
                st.rerun()
else:
    # --- SIDEBAR TRADEMIND ---
    with st.sidebar:
        st.markdown("<h2 style='color:white; text-align:center;'>TRADEMIND</h2>", unsafe_allow_html=True)
        st.markdown("<hr style='border-color:#1E293B'>", unsafe_allow_html=True)
        if st.button("Intelligence Center"): st.session_state.aba = "Home"; st.rerun()
        if st.button("NCM Search"): st.session_state.aba = "NCM"; st.rerun()
        if st.button("Search History"): st.session_state.aba = "History"; st.rerun()
        if st.button("Compliance AI"): st.session_state.aba = "AI"; st.rerun()
        st.markdown("<br><br>")
        if st.button("LOGOUT"): st.session_state.auth = False; st.rerun()

    # --- HOME (CENTRO DE COMANDO) ---
    if st.session_state.aba == "Home":
        st.markdown("<div class='hero-section'><h1>What do you want to import or export today?</h1><p>TradeMind analyzes taxes, regulations, and opportunities in real-time.</p></div>", unsafe_allow_html=True)
        
        # Cambio do Dia
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown("<div class='currency-card'><h4>USD / BRL</h4><h2>5.12</h2></div>", unsafe_allow_html=True)
        with c2: st.markdown("<div class='currency-card'><h4>EUR / BRL</h4><h2>5.48</h2></div>", unsafe_allow_html=True)
        with c3: st.markdown("<div class='currency-card'><h4>CNY / BRL</h4><h2>0.71</h2></div>", unsafe_allow_html=True)
        with c4: st.markdown("<div class='currency-card'><h4>BTC / USD</h4><h2>64.2k</h2></div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Barra de Pesquisa Rápida
        st.text_input("Enter NCM or Product Description for a Quick Analysis")
        
        # Alertas Recentes
        st.markdown("### Regulatory Alerts")
        st.warning("New IPI rates for electronics effective from March 1st.")
        st.info("Bilateral agreement Brazil-Mexico: Tax reduction on automotive parts.")

    # --- NCM SEARCH ---
    elif st.session_state.aba == "NCM":
        st.markdown("<h1>NCM Intelligence Report</h1>", unsafe_allow_html=True)
        busca = st.text_input("Search Base (15,160 items active)")
        if busca:
            st.markdown(f"<div style='background:white; padding:20px; border-radius:12px; border:1px solid #E2E8F0;'><h3>Results for: {busca}</h3><p>Detailed analysis loading...</p></div>", unsafe_allow_html=True)

    # --- HISTORICO ---
    elif st.session_state.aba == "History":
        st.markdown("<h1>Search History</h1>", unsafe_allow_html=True)
        st.write("List of your last 100 strategic searches.")
