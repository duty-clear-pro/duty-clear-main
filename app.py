import streamlit as st

# 1. Configuração de Página - TRADEMIND
st.set_page_config(page_title="TradeMind | Global Intelligence", layout="wide")

# 2. CSS - Design de Terminal de Dados de Alta Performance
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    
    /* Sidebar Dark Profissional */
    [data-testid="stSidebar"] { background-color: #020617 !important; border-right: 1px solid #1E293B; }
    
    /* Botões Menu Sidebar */
    .stButton > button {
        width: 100%; border-radius: 8px; height: 48px; font-weight: 600;
        background-color: transparent; color: #94A3B8; border: 1px solid transparent;
        text-align: left; padding-left: 20px;
    }
    .stButton > button:hover { border: 1px solid #38BDF8; color: #38BDF8; background-color: #0F172A; }

    /* Banner Hero (Boas-Vindas) */
    .hero-banner {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 50px; border-radius: 24px; color: white;
        margin-bottom: 35px; border-left: 10px solid #38BDF8;
        box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1);
    }
    
    /* Cards de Dados de Mercado */
    .market-card {
        background: white; padding: 25px; border-radius: 16px;
        border: 1px solid #E2E8F0; text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .market-card h4 { color: #64748B; font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 10px; }
    .market-card h2 { color: #0F172A; margin: 0; font-size: 32px; font-weight: 800; }

    /* Seção "O que temos" */
    .info-card {
        background: #FFFFFF; padding: 35px; border-radius: 20px;
        border-top: 5px solid #0F172A; height: 100%;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);
    }
    .info-card h3 { color: #0F172A; font-weight: 700; margin-bottom: 15px; }
    .info-card p { color: #475569; line-height: 1.7; font-size: 15px; }
    
    /* Input de Busca */
    .stTextInput input {
        border: 2px solid #E2E8F0 !important; border-radius: 12px !important;
        height: 60px !important; font-size: 18px !important;
    }
    .stTextInput input:focus { border-color: #38BDF8 !important; }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Login
if 'auth' not in st.session_state: st.session_state.auth = False
if 'aba' not in st.session_state: st.session_state.aba = "Home"

if not st.session_state.auth:
    # --- TELA DE LOGIN ---
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1, 1])
    with col:
        st.markdown("<div style='text-align:center;'><h1>TRADEMIND</h1><p>Global Trade Intelligence Center</p></div>", unsafe_allow_html=True)
        u = st.text_input("Identificação do Operador")
        p = st.text_input("Chave de Segurança", type="password")
        if st.button("AUTENTICAR ACESSO", use_container_width=True):
            if u == "admin" and p == "trade202
