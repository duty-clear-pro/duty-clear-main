import streamlit as st

# 1. Configuração de Página
st.set_page_config(page_title="UAU Logística", layout="wide")
logo_url = "https://cdn-icons-png.flaticon.com/512/4370/4370714.png"

# 2. CSS - Estilo Clean e Minimalista (Software de Luxo)
st.markdown("""
    <style>
    /* Fundo Claro e Moderno */
    .stApp {
        background-color: #F8F9FB;
        color: #2D3436;
    }
    
    /* Sidebar Clean */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E1E8ED;
    }
    
    /* Títulos da Página Inicial */
    .main-title {
        font-size: 48px;
        font-weight: 800;
        color: #1A2B48;
        letter-spacing: -1px;
    }
    .sub-title {
        font-size: 18px;
        color: #B8964E;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Botões da Barra Lateral (Barras Reais) */
    div.stButton > button {
        width: 100%;
        background-color: #FFFFFF !important;
        color: #1A2B48 !important;
        height: 50px;
        border: 1px solid #E1E8ED !important;
        border-radius: 6px;
        font-weight: 600;
        text-align: left;
        padding-left: 20px;
        transition: 0.2s;
        margin-bottom: 10px;
    }
    div.stButton > button:hover {
        background-color: #1A2B48 !important;
        color: #FFFFFF !important;
        border: 1px solid #1A2B48 !important;
    }

    /* Caixa de Boas-vindas */
    .welcome-card {
        background-color: #FFFFFF;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.03);
        border: 1px solid #E1E8ED;
        max-width: 800px;
        margin: auto;
    }

    /* Input de Login */
    input {
        border-radius: 6px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Navegação
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False
if 'pagina' not in st.session_state:
    st.session_state['pagina'] = "Boas-vindas"

if not st.session_state['autenticado']:
    # --- TELA DE ENTRADA CLEAN ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    
    with c2:
        st.markdown("<p class='sub-title' style='text-align:center;'>Plataforma Inteligente</p>", unsafe_allow_html=True)
        st.markdown("<h1 class='main-title' style='text-align:center;'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div style="background:white; padding:40px; border-radius:15px; border:1px solid #E1E8ED;">', unsafe_allow_html=True)
            st.markdown("<h3 style='color:#1A2B48; margin-bottom:20px;'>Acesso ao Sistema</h3>", unsafe_allow_html=True)
            u = st.text_input("Usuário")
            p = st.text_input("Senha", type="password")
            if st.button("AUTENTICAR"):
                if u == "gestor.vip" and p == "UAU2026":
                    st.session_state['autenticado'] = True
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- ÁREA INTERNA COM MENU LATERAL EM BARRA ---
    with st.sidebar:
        st.image(logo_url, width=60)
        st.markdown("<h2 style='color:#1A2B48;'>UAU</h2>", unsafe_allow_html=True)
        st.divider()
        
        # Menu em botões largos (Barras)
        if st.button("Painel de Boas-vindas"): st.session_state['pagina'] = "Boas-vindas"; st.rerun()
        if st.button("Consulta NCM"): st.session_state['pagina'] = "NCM"; st.rerun()
        if st.button("Rotas e Mapas"): st.session_state['pagina'] = "Mapas"; st.rerun()
        if st.button("Financeiro"): st.session_state['pagina'] = "Financeiro"; st.rerun()
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if st.button("SAIR"):
            st.session_state['autenticado'] = False
            st.rerun()

    # Conteúdo
    if st.session_state['pagina'] == "Boas-vindas":
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class='welcome-card'>
                <h1 style='color:#1A2B48;'>Olá, Igor.</h1>
                <p style='color:#636E72; font-size:18px;'>Bem-vindo ao centro de comando da <b>UAU Logística</b>.</p>
                <hr style='border: 0.5px solid #E1E8ED;'>
                <p>Selecione uma das operações na barra lateral para começar a gerenciar suas rotas e tributos.</p>
                <div style='display:flex; gap:20px; margin-top:30px;'>
                    <div style='background:#F8F9FB; padding:15px; border-radius:8px; flex:1;'>
                        <b>NCM</b><br>15.160 itens prontos.
                    </div>
                    <div style='background:#F8F9FB; padding:15px; border-radius:8px; flex:1;'>
                        <b>MAPAS</b><br>Google API Ativa.
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
