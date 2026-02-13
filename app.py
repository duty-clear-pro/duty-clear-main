import streamlit as st

# 1. Configuração do Terminal
st.set_page_config(page_title="TradeMind | Global Intelligence", layout="wide")

# 2. CSS - Estética de Autoridade e Design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    
    /* Login Page - Boas Vindas */
    .welcome-container {
        background: linear-gradient(135deg, #020617 0%, #0F172A 100%);
        padding: 60px; border-radius: 30px; color: white;
        border-right: 6px solid #38BDF8; height: 100%; min-height: 550px;
    }
    .welcome-container h1 { font-size: 55px; font-weight: 900; color: #38BDF8; margin-bottom: 10px; }
    .welcome-container p { font-size: 20px; opacity: 0.9; line-height: 1.6; }
    
    /* Botões e Inputs */
    .stButton > button { background-color: #38BDF8; color: white; font-weight: 700; border-radius: 10px; }
    
    /* Interno */
    [data-testid="stSidebar"] { background-color: #020617 !important; }
    .hero-banner { background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); padding: 40px; border-radius: 20px; color: white; border-left: 10px solid #38BDF8; }
    .legal-footer { font-size: 11px; color: #94A3B8; text-align: center; padding: 20px; border-top: 1px solid #E2E8F0; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Estado da Sessão
if 'auth' not in st.session_state: st.session_state.auth = False
if 'aba' not in st.session_state: st.session_state.aba = "Home"
if 'chat_history' not in st.session_state: st.session_state.chat_history = []

# --- TELA DE ACESSO (O QUE ESTAVA VAZIO) ---
if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_info, col_login = st.columns([1.5, 1], gap="large")
    
    with col_info:
        st.markdown("""
            <div class='welcome-container'>
                <h1>TRADEMIND</h1>
                <p><b>Seja bem-vindo ao futuro do Comércio Exterior.</b></p>
                <br>
                <p>O TradeMind é uma plataforma de inteligência preditiva projetada para agir <b>antes</b> da execução do seu ERP. Analisamos viabilidade fiscal, custos reais e riscos regulatórios com precisão cirúrgica.</p>
                <br>
                <div style='font-size: 18px;'>
                    <p>🚀 <b>Inteligência NCM:</b> Classificações baseadas em dados históricos.</p>
                    <p>⚖️ <b>Compliance Ativo:</b> Blindagem jurídica para sua operação.</p>
                    <p>📊 <b>Land Cost:</b> Simulação de valores referenciais de mercado.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col_login:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.subheader("Login de Operador")
        u = st.text_input("Identificação Master", placeholder="Ex: admin")
        p = st.text_input("Chave de Segurança", type="password", placeholder="••••••••")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("ACESSAR TERMINAL", use_container_width=True):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Credenciais Invál
