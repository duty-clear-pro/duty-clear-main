import streamlit as st

# 1. Setup TradeMind
st.set_page_config(page_title="TradeMind | Intelligence", layout="wide")

# 2. CSS Total - Login e Interno
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    [data-testid="stSidebar"] { background-color: #020617 !important; }
    
    .welcome-box {
        background: linear-gradient(135deg, #020617 0%, #0F172A 100%);
        padding: 50px; border-radius: 25px; color: white; border-right: 6px solid #38BDF8;
    }
    .hero-banner {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 40px; border-radius: 20px; color: white; border-left: 10px solid #38BDF8;
    }
    .legal-footer {
        font-size: 11px; color: #94A3B8; text-align: center; padding: 20px;
        border-top: 1px solid #E2E8F0; margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Gestão de Sessão
if 'auth' not in st.session_state: st.session_state.auth = False
if 'aba' not in st.session_state: st.session_state.aba = "Home"
if 'chat_history' not in st.session_state: st.session_state.chat_history = []

# --- TELA DE ACESSO ---
if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_info, col_login = st.columns([1.4, 1], gap="large")
    
    with col_info:
        st.markdown("""
            <div class='welcome-box'>
                <h1 style='color:#38BDF8; font-size:45px;'>TRADEMIND</h1>
                <p style='font-size:22px;'><b>A inteligência que antecede o movimento.</b></p>
                <p>O TradeMind analisa a viabilidade da sua operação internacional <b>antes</b> dela acontecer, garantindo lucro e blindagem fiscal.</p>
                <hr style='opacity:0.1;'>
                <p>✅ <b>Valores Baseados em Dados:</b> Inteligência referencial de mercado.</p>
                <p>✅ <b>Compliance Ativo:</b> Radar de riscos regulatórios em tempo real.</p>
            </div>
        """, unsafe_allow_html=True)

    with col_login:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.subheader("Login de Operador")
        u = st.text_input("Usuário Master")
        p = st.text_input("Chave de Acesso", type="password")
        if st.button("ACESSAR TERMINAL", use_container_width=True):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Credenciais Inválidas. Tente novamente.")

# --- TELA INTERNA ---
else:
    with st.sidebar:
        st.markdown("<h2 style='color:white; text-align:center;'>TRADEMIND</h2>", unsafe_allow_html=True)
        if st.button("🏠 Home Dashboard", use_container_width=True): st.session_state.aba = "Home"; st.rerun()
        if st.button("📖 Quem Somos", use_container_width=True): st.session_state.aba = "About"; st.rerun()
        if st.button("🔍 Inteligência NCM", use_container_width=True): st.session_state.aba = "NCM"; st.rerun()
        if st.button("🤖 Assistente IA", use_container_width=True): st.session_state.aba = "AI"; st.rerun()
        st.markdown("<br><hr style='opacity:0.2;'><br>", unsafe_allow_html=True)
        if st.button("🚪 Sair", use_container_width=True): st.session_state.auth = False; st.rerun()

    if st.session_state.aba == "Home":
        st.markdown("<div class='hero-banner'><h1>Terminal TradeMind Ativo</h1><p>Bem-vindo, Igor. Monitoramento global iniciado.</p></div>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1: st.metric("Dólar", "R$ 5,12", "+0.12%")
        with c2: st.metric("Euro", "R$ 5,48", "-0.05%")
        with c3: st.metric("Base NCM", "15.160", "Auditada")

    elif st.session_state.aba == "About":
        st.header("📖 Quem Somos")
        st.markdown("""
            O **TradeMind** é uma plataforma de inteligência preditiva. Nosso trabalho é baseado em **valores referenciais e dados históricos**, 
            atuando na estratégia de pré-embarque para mitigar riscos e maximizar lucros.
        """)
        st.info("Atenção: Somos uma ferramenta de apoio à decisão baseada em dados.")

    elif st.session_state.aba == "AI":
        st.header("🤖 Consultor AI")
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])
        if prompt := st.chat_input("Pergunte algo..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
