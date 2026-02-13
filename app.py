import streamlit as st

# Configuração de Página
st.set_page_config(page_title="UAU Logística | Login", page_icon="⚖️", layout="wide")

# CSS Avançado para Apresentação
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .login-container {
        background-color: #1A2B48;
        padding: 40px;
        border-radius: 15px;
        color: white;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
    }
    .feature-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #B8964E;
        margin-bottom: 20px;
        color: #1A2B48;
    }
    .title-main { color: #1A2B48; font-weight: 900; font-size: 45px; margin-bottom: 0px; }
    .slogan-main { color: #B8964E; font-size: 20px; font-style: italic; margin-bottom: 40px; }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Sessão
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    # --- TELA DE APRESENTAÇÃO E LOGIN ---
    
    col_info, col_spacer, col_login = st.columns([1.2, 0.2, 1])
    
    with col_info:
        st.markdown("<h1 class='title-main'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
        st.markdown("<p class='slogan-main'>A precisão que o seu lucro exige.</p>", unsafe_allow_html=True)
        
        st.markdown("### Por que usar o sistema?")
        
        st.markdown("""
        <div class="feature-card">
            <b>🚀 Agilidade Operacional</b><br>
            Consulte margens líquidas em segundos com base em custos de frete reais.
        </div>
        <div class="feature-card">
            <b>📦 Inteligência NCM</b><br>
            Acesso à base referencial de tributação para suporte à decisão.
        </div>
        <div class="feature-card">
            <b>🛡️ Blindagem de Dados</b><br>
            Ambiente seguro para simulações estratégicas de carregamento.
        </div>
        """, unsafe_allow_html=True)

    with col_login:
        st.markdown("<br><br>", unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="login-container">', unsafe_allow_html=True)
            st.subheader("🔐 Área do Gestor")
            user = st.text_input("Usuário VIP")
            password = st.text_input("Chave de Acesso", type="password")
            
            if st.button("AUTENTICAR NO SERVIDOR"):
                if user == "gestor.vip" and password == "UAU2026":
                    st.session_state['autenticado'] = True
                    st.rerun()
                else:
                    st.error("Credenciais inválidas ou acesso não autorizado.")
            st.markdown('</div>', unsafe_allow_html=True)
            st.caption("Acesso restrito a colaboradores autorizados.")

else:
    # --- O CONTEÚDO DO APP APÓS O LOGIN (DASHBOARD) ---
    st.sidebar.title("UAU Logística")
    if st.sidebar.button("Encerrar Sessão"):
        st.session_state['autenticado'] = False
        st.rerun()
        
    st.markdown("<h1 style='color: #1A2B48;'>Bem-vindo ao Dashboard</h1>", unsafe_allow_html=True)
    st.write("O sistema está pronto para operar.")
    # Aqui entra o resto do código de cálculo que já fizemos
