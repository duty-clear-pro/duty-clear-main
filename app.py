import streamlit as st

# 1. Configuração de Interface Profissional
st.set_page_config(page_title="UAU Logística | ERP", layout="wide")

# 2. CSS Avançado - Menu em Barra Lateral (Sem bolinhas)
st.markdown("""
    <style>
    /* Estilo Landing Page Premium */
    .stApp { background-color: #002B24; color: #FFFFFF; }
    
    /* SIDEBAR: Branca com botões de bloco */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e0e0e0;
    }
    
    /* Customização dos Botões do Menu Lateral */
    .sidebar-btn {
        display: block;
        width: 100%;
        padding: 15px;
        margin-bottom: 5px;
        background-color: #f8f9fa;
        color: #1A2B48;
        border: none;
        border-radius: 4px;
        text-align: left;
        font-weight: bold;
        text-decoration: none;
        transition: 0.2s;
        cursor: pointer;
    }
    .sidebar-btn:hover {
        background-color: #28A745;
        color: white;
    }
    
    /* Títulos e Identidade */
    .main-title { font-size: 52px; font-weight: 900; color: #FFFFFF; margin-bottom: 0px; }
    .sub-title { font-size: 18px; color: #A0C4B8; margin-bottom: 40px; }
    
    /* Cards do Interior */
    .card-boas-vindas {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 10px;
        color: #333;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Navegação
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False
if 'pagina' not in st.session_state:
    st.session_state['pagina'] = "Boas-vindas"

if not st.session_state['autenticado']:
    # --- TELA DE ENTRADA ---
    col_text, _, col_login = st.columns([1.5, 0.2, 1])
    with col_text:
        st.markdown("<h1 class='main-title'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
        st.markdown("<p class='sub-title'>Sistema de Inteligência Operacional e Tributária.</p>", unsafe_allow_html=True)
        st.markdown("""
            <div style='background:white; padding:20px; border-radius:8px; color:#333; border-left:8px solid #28A745;'>
                <b>Gestão de Performance</b><br>Controle total de fretes, rotas e classificação fiscal.
            </div>
        """, unsafe_allow_html=True)
    with col_login:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        with st.form("login"):
            u = st.text_input("Usuário")
            p = st.text_input("Senha", type="password")
            if st.form_submit_button("ACESSAR SERVIDOR"):
                if u == "gestor.vip" and p == "UAU2026":
                    st.session_state['autenticado'] = True
                    st.rerun()
else:
    # --- INTERIOR COM MENU EM BARRA ---
    with st.sidebar:
        st.markdown("<h2 style='color:#1A2B48;'>UAU LOGÍSTICA</h2>", unsafe_allow_html=True)
        st.divider()
        
        # Simulando botões de menu (Barra Lateral Real)
        if st.button("Painel de Boas-vindas", use_container_width=True):
            st.session_state['pagina'] = "Boas-vindas"
        if st.button("Consulta NCM", use_container_width=True):
            st.session_state['pagina'] = "NCM"
        if st.button("Rotas e Mapas", use_container_width=True):
            st.session_state['pagina'] = "Mapas"
        if st.button("Gestão de Fretes", use_container_width=True):
            st.session_state['pagina'] = "Fretes"
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("Sair", type="primary", use_container_width=True):
            st.session_state['autenticado'] = False
            st.rerun()

    # Conteúdo Dinâmico
    st.markdown(f"<h2 style='color:white;'>{st.session_state['pagina']}</h2>", unsafe_allow_html=True)
    
    if st.session_state['pagina'] == "Boas-vindas":
        st.markdown("""
            <div class='card-boas-vindas'>
                <h3>Olá, Igor!</h3>
                <p>O sistema UAU Logística está operando normalmente. Selecione uma opção no menu à esquerda para iniciar.</p>
                <hr>
                <div style='display:flex; justify-content:space-between;'>
                    <div><b>Base NCM:</b> 15.160 itens</div>
                    <div><b>Status Google Maps:</b> Conectado</div>
                    <div><b>Sessão:</b> Administrador</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
