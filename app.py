import streamlit as st

# 1. Configuracao de Pagina - TRADEMIND GLOBAL
st.set_page_config(page_title="TradeMind | Global Intelligence", layout="wide")

# 2. CSS - Design Profissional de Alto Contraste
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    
    /* Sidebar Dark Profissional */
    [data-testid="stSidebar"] { background-color: #020617 !important; border-right: 1px solid #1E293B; }
    
    /* Botoes Menu */
    .stButton > button {
        width: 100%; border-radius: 8px; height: 45px; font-weight: 600;
        background-color: transparent; color: #94A3B8; border: 1px solid transparent;
    }
    .stButton > button:hover { border: 1px solid #38BDF8; color: #38BDF8; }

    /* Banner de Boas-Vindas Recheado */
    .welcome-banner {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 45px; border-radius: 20px; color: white;
        margin-bottom: 30px; border-left: 10px solid #38BDF8;
    }
    
    /* Cards de Dados */
    .data-card {
        background: white; padding: 25px; border-radius: 16px;
        border: 1px solid #E2E8F0; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        height: 100%;
    }
    .data-card h3 { color: #64748B; font-size: 13px; margin: 0; text-transform: uppercase; letter-spacing: 1px; }
    .data-card h1 { color: #0F172A; margin: 10px 0; font-size: 28px; font-weight: 800; }

    /* Inputs Visiveis */
    .stTextInput input {
        border: 2px solid #0F172A !important; border-radius: 10px !important;
        height: 50px !important; background-color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Logica de Sessao
if 'auth' not in st.session_state: st.session_state.auth = False
if 'aba' not in st.session_state: st.session_state.aba = "Home"

if not st.session_state.auth:
    # --- TELA DE LOGIN ---
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.markdown("<div style='text-align:center;'><h1>TRADEMIND</h1><p style='color:#64748B;'>Intelligence for Global Trade</p></div>", unsafe_allow_html=True)
        u = st.text_input("Usuario Master")
        p = st.text_input("Chave de Acesso", type="password")
        if st.button("AUTENTICAR NO TERMINAL", use_container_width=True):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True
                st.rerun()
else:
    # --- SIDEBAR ---
    with st.sidebar:
        st.markdown("<div style='padding:20px; text-align:center;'><h2 style='color:white;'>TRADEMIND</h2><p style='color:#38BDF8; font-size:11px;'>GLOBAL INTELLIGENCE</p></div>", unsafe_allow_html=True)
        if st.button("Terminal de Inteligencia"): st.session_state.aba = "Home"; st.rerun()
        if st.button("Classificacao NCM"): st.session_state.aba = "NCM"; st.rerun()
        if st.button("Historico Estrategico"): st.session_state.aba = "History"; st.rerun()
        if st.button("TradeMind AI"): st.session_state.aba = "AI"; st.rerun()
        st.markdown("<br><br>")
        if st.button("ENCERRAR SESSAO"): st.session_state.auth = False; st.rerun
