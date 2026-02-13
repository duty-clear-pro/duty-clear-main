import streamlit as st

# 1. Configuração do Terminal TradeMind
st.set_page_config(page_title="TradeMind | Intelligence", layout="wide")

# 2. CSS - Estética de Terminal Profissional
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    
    /* Login Page Design */
    .about-box {
        background: linear-gradient(135deg, #020617 0%, #0F172A 100%);
        padding: 40px; border-radius: 20px; color: white; border-right: 5px solid #38BDF8;
        height: 100%; min-height: 500px;
    }
    .art-frame {
        background: #FFFFFF; border-radius: 20px; height: 250px;
        display: flex; align-items: center; justify-content: center;
        border: 2px dashed #E2E8F0; color: #94A3B8; margin-bottom: 20px;
    }

    /* Dashboard Design */
    .hero-card {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 40px; border-radius: 20px; color: white; margin-bottom: 20px;
        border-left: 10px solid #38BDF8;
    }
    .stat-card {
        background: white; padding: 20px; border-radius: 15px;
        border: 1px solid #E2E8F0; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    [data-testid="stSidebar"] { background-color: #020617 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. Lógica de Navegação e Sessão
if 'auth' not in st.session_state: st.session_state.auth = False
if 'aba' not in st.session_state: st.session_state.aba = "Home"

# --- TELA DE ACESSO (DESLOGADO) ---
if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_txt, col_form = st.columns([1.3, 1], gap="large")
    
    with col_txt:
        st.markdown("""
            <div class='about-box'>
                <h1 style='color:#38BDF8; font-size: 40px;'>TRADEMIND</h1>
                <p style='font-size:20px;'><b>A Inteligência que antecede o movimento.</b></p>
                <p>O TradeMind analisa a viabilidade da sua operação internacional <b>antes</b> dela acontecer, garantindo lucro e blindagem fiscal.</p>
                <br>
                <p>✅ <b>NCM Intelligence:</b> Classificação com base legal.</p>
                <p>✅ <b>Land Cost:</b> Simulação de custos reais no destino.</p>
                <p>✅ <b>Compliance:</b> Radar de riscos regulatórios em tempo real.</p>
            </div>
        """, unsafe_allow_html=True)

    with col_form:
        st.markdown("<div class='art-frame'>[ ESPAÇO PARA ARTE TRADEMIND ]</div>", unsafe_allow_html=True)
        u = st.text_input("Usuário Master", key="user_input")
        p = st.text_input("Chave de Acesso", type="password", key="pass_input")
        if st.button("AUTENTICAR SISTEMA", use_container_width=True):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Acesso Negado. Verifique usuário e senha.")

# --- TELA INTERNA (LOGADO) ---
else:
    with st.sidebar:
        st.markdown("<div style='padding:10px; text-align:center;'><h2 style='color:white;'>TRADEMIND</h2></div>", unsafe_allow_html=True)
        if st.button("🏠 Home / Painel", use_container_width=True): 
            st.session_state.aba = "Home"
            st.rerun()
        if st.button("🔍 Inteligência NCM", use_container_width=True): 
            st.session_state.aba = "NCM"
            st.rerun()
        if st.button("🤖 Consultor AI", use_container_width=True): 
            st.session_state.aba = "AI"
            st.rerun()
        st.markdown("<br><br>")
        if st.button("🚪 Encerrar Sessão", use_container_width=True): 
            st.session_state.auth = False
            st.rerun()

    # Conte
