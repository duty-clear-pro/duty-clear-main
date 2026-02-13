import streamlit as st

# 1. SETUP DE PÁGINA
st.set_page_config(page_title="TradeMind | Global Intelligence", layout="wide")

# 2. CSS UNIFICADO (LOGIN + INTERNO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    
    /* Login & Quem Somos */
    .about-box { background: linear-gradient(135deg, #020617 0%, #0F172A 100%); padding: 40px; border-radius: 20px; color: white; border-right: 5px solid #38BDF8; height: 100%; }
    .art-placeholder { background: #FFFFFF; border-radius: 20px; height: 280px; display: flex; align-items: center; justify-content: center; border: 2px dashed #E2E8F0; color: #94A3B8; margin-bottom: 20px; }
    
    /* Dashboard Interno */
    .hero-banner { background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); padding: 40px; border-radius: 20px; color: white; margin-bottom: 20px; border-left: 10px solid #38BDF8; }
    .stat-card { background: white; padding: 20px; border-radius: 15px; border: 1px solid #E2E8F0; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    [data-testid="stSidebar"] { background-color: #020617 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. CONTROLE DE ESTADO (Sessão)
if 'auth' not in st.session_state: st.session_state.auth = False
if 'aba' not in st.session_state: st.session_state.aba = "Home"

# --- FLUXO DE TELAS ---

if not st.session_state.auth:
    # TELA DE LOGIN + QUEM SOMOS
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_info, col_login = st.columns([1.3, 1], gap="large")
    
    with col_info:
        st.markdown("""
            <div class='about-box'>
                <h1 style='color:#38BDF8;'>TRADEMIND</h1>
                <p style='font-size:20px;'><b>A Inteligência que antecede o movimento.</b></p>
                <p>O TradeMind analisa a viabilidade da sua operação internacional <b>antes</b> dela acontecer.</p>
                <hr style='opacity:0.1;'>
                <p>✅ <b>Blindagem Fiscal:</b> Evite multas por classificação errada.</p>
                <p>✅ <b>Land Cost:</b> Saiba o custo real da mercadoria no destino.</p>
                <p>✅ <b>Compliance:</b> Monitoramento de órgãos anuentes (ANVISA/INMETRO).</p>
            </div>
        """, unsafe_allow_html=True)

    with col_login:
        st.markdown("<div class='art-placeholder'>[ ESPAÇO PARA ARTE TRADEMIND ]</div>", unsafe_allow_html=True)
        u = st.text_input("Usuário Master")
        p = st.text_input("Chave de Acesso", type="password")
        if st.button("AUTENTICAR SISTEMA", use_container_width=True):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Acesso Negado")
else:
    # MENU LATERAL (SÓ APARECE LOGADO)
    with st.sidebar:
        st.markdown("<h2 style='color:white; text-align:center;'>TRADEMIND</h2>", unsafe_allow_html=True)
        if st.button("🏠 Home / Dashboard"): st.session_state.aba = "Home"; st.rerun()
        if st.button("🔍 Inteligência NCM"): st.session_state.aba = "NCM"; st.rerun()
        if st.button
