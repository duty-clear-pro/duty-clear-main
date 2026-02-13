import streamlit as st

# 1. Configuração de Alta Performance
st.set_page_config(page_title="UAU Logística | Gestão de Elite", layout="wide")

# 2. O CSS para criar o "Site Foda" (Estilo Aegro)
st.markdown("""
    <style>
    /* Fundo Dark Moderno */
    .stApp {
        background-color: #002B24; /* Verde escuro premium inspirado no exemplo */
        color: #FFFFFF;
    }
    
    /* Títulos Imponentes */
    .main-title {
        font-size: 56px;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 20px;
        color: #FFFFFF;
    }
    .sub-title {
        font-size: 20px;
        color: #A0C4B8;
        margin-bottom: 40px;
        max-width: 600px;
    }
    
    /* Cards de Funcionalidades (Estilo Aegro) */
    .feature-card {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 12px;
        color: #333333;
        height: 100%;
        border-bottom: 6px solid #28A745;
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-10px);
    }
    .feature-icon {
        font-size: 40px;
        margin-bottom: 15px;
    }
    .feature-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 15px;
        color: #002B24;
    }
    .feature-text {
        font-size: 15px;
        color: #666;
        line-height: 1.6;
    }

    /* Formulário de Login VIP */
    .login-box {
        background-color: #FFFFFF;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0px 20px 40px rgba(0,0,0,0.4);
        color: #333;
    }
    
    /* Botão Estilo Software Real */
    div.stButton > button {
        width: 100%;
        background-color: #28A745 !important;
        color: white !important;
        font-weight: bold;
        height: 50px;
        border-radius: 8px;
        border: none;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Login
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    # --- INTERFACE DE LANDING PAGE PREMIUM ---
    col_text, col_spacer, col_login = st.columns([1.5, 0.2, 1])

    with col_text:
        st.markdown("<p style='color: #28A745; font-weight: bold; text-transform: uppercase;'>Tudo em um só lugar</p>", unsafe_allow_html=True)
        st.markdown("<h1 class='main-title'>Conheça o melhor software de gestão logística e NCM</h1>", unsafe_allow_html=True)
        st.markdown("<p class='sub-title'>O UAU Logística é um sistema inteligente que ajuda a gerenciar suas atividades operacionais, desde a carga até o controle tributário preciso.</p>", unsafe_allow_html=True)
        
        # Grid de Funcionalidades (Preenchendo a tela com valor)
        f1, f2 = st.columns(2)
        with f1:
            st.markdown("""
                <div class='feature-card'>
                    <div class='feature-title'>📦 Controle de Cargas</div>
                    <p class='feature-text'>Gerencie volumes, pesos e tipos de veículos em uma interface intuitiva e rápida.</p>
                </div>
            """, unsafe_allow_html=True)
        with f2:
            st.markdown("""
                <div class='feature-card'>
                    <div class='feature-title'>⚖️ Inteligência Fiscal</div>
                    <p class='feature-text'>Acesso direto à base SEFAZ para classificação NCM e cálculos tributários automáticos.</p>
                </div>
            """, unsafe_allow_html=True)

    with col_login:
        st.markdown("<br><br>", unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="login-box">', unsafe_allow_html=True)
            st.markdown("<h3 style='margin-top:0;'>Acesse a Plataforma</h3>", unsafe_allow_html=True)
            user = st.text_input("Seu Usuário")
            password = st.text_input("Sua Senha", type="password")
            if st.button("Entrar no Sistema"):
                if user == "gestor.vip" and password == "UAU2026":
                    st.session_state['autenticado'] = True
                    st.rerun()
            st.markdown("<p style='font-size:12px; color:#999; margin-top:20px; text-align:center;'>Esqueceu sua senha? Entre em contato com o suporte técnico.</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- DASHBOARD INTERNO (ESTILO ERP PREMIUM) ---
    st.sidebar.markdown("<h2 style='color:white;'>UAU LOGÍSTICA</h2>", unsafe_allow_html=True)
    menu = st.sidebar.radio("Navegação", ["Dashboard", "Gestão NCM", "Rotas Inteligentes", "Financeiro"])
    
    st.markdown(f"<h1>{menu}</h1>", unsafe_allow_html=True)
    st.write("Bem-vindo ao centro de comando, Igor.")
