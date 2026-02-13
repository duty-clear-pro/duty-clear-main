import streamlit as st

# 1. Configurações de Interface
st.set_page_config(page_title="UAU Logística | Cockpit", layout="wide")
logo_url = "https://cdn-icons-png.flaticon.com/512/4370/4370714.png"

# 2. CSS Avançado (CORREÇÃO DE CORES E CONTRASTE)
st.markdown("""
    <style>
    /* Estilo Geral */
    .stApp { background-color: #F4F7F9; }
    
    /* CORREÇÃO DA SIDEBAR (TEXTO BRANCO SOBRE AZUL) */
    [data-testid="stSidebar"] { 
        background-color: #1A2B48 !important; 
    }
    [data-testid="stSidebar"] * { 
        color: #FFFFFF !important; 
    }
    
    /* Ajuste específico para os botões de rádio (Menu) */
    div[data-testid="stSidebarNav"] span { color: white !important; }
    label[data-testid="stWidgetLabel"] { color: white !important; font-size: 1.1rem; }
    
    /* Marcador Dourado para a Opção Selecionada */
    .st-emotion-cache-17l695n { color: #B8964E !important; font-weight: bold; }

    /* Header Profissional */
    .main-header {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 25px;
    }
    
    /* Cards de Indicadores */
    .kpi-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        border-bottom: 4px solid #B8964E;
        text-align: center;
        color: #1A2B48 !important;
    }
    .kpi-card h2 { color: #1A2B48 !important; margin: 0; }
    .kpi-card small { color: #666 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. Gerenciamento de Acesso
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    # TELA DE LOGIN (MANTIDA)
    col_info, _, col_login = st.columns([1.3, 0.2, 1])
    with col_info:
        st.image(logo_url, width=90)
        st.markdown("<h1 style='color: #1A2B48; font-size: 52px; font-weight: 900;'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color: #B8964E;'>DUTY CLEAR | INTELIGÊNCIA TRIBUTÁRIA</p>", unsafe_allow_html=True)
    with col_login:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        with st.form("login"):
            u = st.text_input("Usuário")
            p = st.text_input("Senha", type="password")
            if st.form_submit_button("ENTRAR NO SISTEMA"):
                if u == "gestor.vip" and p == "UAU2026":
                    st.session_state['autenticado'] = True
                    st.rerun()
else:
    # --- BARRA LATERAL COM CORES CORRIGIDAS ---
    with st.sidebar:
        st.image(logo_url, width=80)
        st.markdown("<h3 style='text-align:center;'>Gestor: Igor</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#B8964E !important;'>Nível: Administrador</p>", unsafe_allow_html=True)
        st.divider()
        
        secao = st.radio(
            "NAVEGAÇÃO PRINCIPAL",
            ["Dashboard", "Mapas e Rotas", "Consulta NCM", "Logística", "Financeiro", "Configurações"]
        )
        st.divider()
        if st.button("Sair do Sistema"):
            st.session_state['autenticado'] = False
            st.rerun()

    # --- ÁREA PRINCIPAL ---
    st.markdown(f"<div class='main-header'><span style='font-size:20px; font-weight:bold; color:#1A2B48;'>{secao.upper()}</span></div>", unsafe_allow_html=True)

    if secao == "Dashboard":
        c1, c2, c3, c4 = st.columns(4)
        c1.markdown("<div class='kpi-card'><small>CONSULTAS NCM</small><h2>1.240</h2></div>", unsafe_allow_html=True)
        c2.markdown("<div class='kpi-card'><small>ROTAS ATIVAS</small><h2>42</h2></div>", unsafe_allow_html=True)
        c3.markdown("<div class='kpi-card'><small>MARGEM MÉDIA</small><h2>18.5%</h2></div>", unsafe_allow_html=True)
        c4.markdown("<div class='kpi-card'><small>STATUS SERVER</small><h2 style='color:green !important;'>ON</h2></div>", unsafe_allow_html=True)
        
        st.write("<br>", unsafe_allow_html=True)
        with st.container(border=True):
            st.subheader("Atividades em Tempo Real")
            st.info("Simulação: Catalão (GO) para São Paulo (SP) - Rota via BR-050.")
