import streamlit as st

# 1. Configuração de Interface Profissional
st.set_page_config(page_title="UAU Logística | ERP", layout="wide")

# 2. CSS - Estilo Aegro / Software de Elite (Zero Emojis)
st.markdown("""
    <style>
    /* Fundo Dark Moderno (Landing Page) */
    .stApp {
        background-color: #002B24;
        color: #FFFFFF;
    }
    
    /* Barra Lateral Fixa e Visível */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e0e0e0;
        min-width: 260px !important;
    }
    
    /* Texto da Sidebar (Preto para contraste no fundo branco) */
    [data-testid="stSidebar"] * {
        color: #1A2B48 !important;
        font-weight: 600;
    }

    /* Títulos da Página Inicial */
    .main-title {
        font-size: 52px;
        font-weight: 900;
        line-height: 1.1;
        color: #FFFFFF;
        margin-bottom: 10px;
    }
    .sub-title {
        font-size: 18px;
        color: #A0C4B8;
        margin-bottom: 40px;
    }
    
    /* Cards de Funcionalidade */
    .feature-card {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 8px;
        color: #333333;
        border-left: 8px solid #28A745;
        margin-bottom: 20px;
    }
    .feature-title {
        font-size: 20px;
        font-weight: 800;
        color: #002B24;
        margin-bottom: 10px;
        text-transform: uppercase;
    }

    /* Botões e Inputs */
    div.stButton > button {
        width: 100%;
        background-color: #28A745 !important;
        color: white !important;
        height: 50px;
        border-radius: 4px;
        border: none;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Login
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    # --- INTERFACE DE ENTRADA (ESTILO SOFTWARE PREMIUM) ---
    col_text, col_spacer, col_login = st.columns([1.5, 0.2, 1])

    with col_text:
        st.markdown("<p style='color: #28A745; font-weight: bold; letter-spacing: 2px;'>DUTY CLEAR</p>", unsafe_allow_html=True)
        st.markdown("<h1 class='main-title'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
        st.markdown("<p class='sub-title'>Plataforma de inteligência para gestão de frotas, fretes e conformidade tributária NCM.</p>", unsafe_allow_html=True)
        
        # Cards de demonstração de módulos
        st.markdown("""
            <div class='feature-card'>
                <div class='feature-title'>Inteligência Fiscal</div>
                <p style='color: #666;'>Base de dados atualizada com 15.160 itens para classificação e cálculo tributário.</p>
            </div>
            <div class='feature-card'>
                <div class='feature-title'>Monitoramento de Rotas</div>
                <p style='color: #666;'>Integração com mapas para cálculo preciso de distância, tempo e custo operacional.</p>
            </div>
        """, unsafe_allow_html=True)

    with col_login:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        with st.container():
            st.markdown('<div style="background:white; padding:40px; border-radius:10px; color:#333;">', unsafe_allow_html=True)
            st.markdown("<h3 style='margin:0 0 20px 0;'>Acesso ao Servidor</h3>", unsafe_allow_html=True)
            user = st.text_input("Usuário")
            password = st.text_input("Senha", type="password")
            if st.button("Autenticar"):
                if user == "gestor.vip" and password == "UAU2026":
                    st.session_state['autenticado'] = True
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- ÁREA INTERNA COM BARRA LATERAL FIXA ---
    # Mudando o fundo interno para branco/cinza claro para parecer sistema
    st.markdown("<style>.stApp { background-color: #F8F9FA; color: #333; }</style>", unsafe_allow_html=True)
    
    with st.sidebar:
        st.markdown("<h2 style='color:#1A2B48; margin-bottom:0;'>UAU</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#28A745; font-size:12px; font-weight:bold;'>LOGÍSTICA</p>", unsafe_allow_html=True)
        st.divider()
        
        # Menu em lista visível, sem ícones amadores
        secao = st.radio(
            "MENU DE OPERAÇÕES",
            ["Painel Geral", "Consulta NCM", "Rotas e Mapas", "Gestão de Fretes", "Configurações"],
            label_visibility="visible"
        )
        
        st.divider()
        if st.button("Encerrar Sessão"):
            st.session_state['autenticado'] = False
            st.rerun()

    # Conteúdo das Seções
    st.markdown(f"<h1 style='color:#1A2B48;'>{secao}</h1>", unsafe_allow_html=True)
    
    if secao == "Painel Geral":
        st.write("Visão consolidada da operação.")
        c1, c2, c3 = st.columns(3)
        with c1: st.metric("Consultas NCM", "1.240")
        with c2: st.metric("Rotas Calculadas", "42")
        with c3: st.metric("Status do Sistema", "Estável")
