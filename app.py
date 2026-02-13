import streamlit as st

# 1. Configurações de Software Corporativo
st.set_page_config(page_title="UAU Logística | ERP System", layout="wide")

# 2. O Motor de Design (Inspirado no Total ERP)
st.markdown("""
    <style>
    /* Importando Fonte Profissional */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    /* Fundo do Sistema */
    .stApp {
        background-color: #F3F6F9;
    }
    
    /* SIDEBAR PROFISSIONAL (TOTAL ERP STYLE) */
    [data-testid="stSidebar"] {
        background-color: #1E1E2D !important; /* Azul quase preto, muito sério */
        min-width: 280px !important;
    }
    
    /* Botões do Menu Lateral em Barra */
    div.stButton > button {
        width: 100%;
        background-color: transparent !important;
        color: #A2A3B7 !important; /* Texto cinza suave antes de clicar */
        border: none !important;
        height: 55px;
        text-align: left;
        font-size: 15px;
        font-weight: 500;
        border-radius: 0px;
        border-left: 4px solid transparent !important;
        transition: 0.3s;
        padding-left: 25px;
    }
    div.stButton > button:hover {
        background-color: #1B1B28 !important;
        color: #FFFFFF !important;
        border-left: 4px solid #3699FF !important; /* Azul brilhante de destaque */
    }

    /* Header e Títulos */
    .erp-header {
        background-color: #FFFFFF;
        padding: 20px 30px;
        border-radius: 8px;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 25px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .erp-title { color: #181C32; font-weight: 800; font-size: 24px; }
    
    /* Cards de Boas-Vindas */
    .welcome-card {
        background-color: #FFFFFF;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.02);
        border: 1px solid #EBEDF3;
    }
    
    /* Botão de Login */
    .login-btn button {
        background-color: #3699FF !important;
        color: white !important;
        border-radius: 6px !important;
        height: 50px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Sessão
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False
if 'pagina' not in st.session_state:
    st.session_state['pagina'] = "Boas-vindas"

if not st.session_state['autenticado']:
    # --- TELA DE ACESSO (MANTENDO O FOCO NO PRODUTO) ---
    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("""
            <div style='background:white; padding:50px; border-radius:15px; box-shadow:0px 20px 50px rgba(0,0,0,0.1);'>
                <h1 style='color:#181C32; text-align:center; font-weight:800;'>UAU LOGÍSTICA</h1>
                <p style='color:#7E8299; text-align:center; margin-bottom:40px;'>Sistema de Gestão de Transportes e NCM</p>
        """, unsafe_allow_html=True)
        
        u = st.text_input("Usuário")
        p = st.text_input("Senha", type="password")
        
        st.markdown("<div class='login-btn'>", unsafe_allow_html=True)
        if st.button("ACESSAR PAINEL DE CONTROLE"):
            if u == "gestor.vip" and p == "UAU2026":
                st.session_state['autenticado'] = True
                st.rerun()
        st.markdown("</div></div>", unsafe_allow_html=True)

else:
    # --- INTERFACE ERP (INTERNA) ---
    with st.sidebar:
        st.markdown("<div style='padding:20px;'><h2 style='color:white; letter-spacing:1px;'>UAU ERP</h2></div>", unsafe_allow_html=True)
        
        # Menu em Barra Estilo Total ERP
        if st.button("📊  Início / Boas-vindas"): st.session_state['pagina'] = "Boas-vindas"; st.rerun()
        if st.button("🚚  Módulo Logística"): st.session_state['pagina'] = "Logística"; st.rerun()
        if st.button("⚖️  Inteligência NCM"): st.session_state['pagina'] = "NCM"; st.rerun()
        if st.button("💰  Financeiro & Fretes"): st.session_state['pagina'] = "Financeiro"; st.rerun()
        if st.button("🗺️  Mapas e Rotas"): st.session_state['pagina'] = "Mapas"; st.rerun()
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if st.button("🚪 Sair do Sistema"):
            st.session_state['autenticado'] = False
            st.rerun()

    # ÁREA DE CONTEÚDO
    st.markdown(f"""
        <div class='erp-header'>
            <span class='erp-title'>{st.session_state['pagina']}</span>
            <span style='color:#B5B5C3;'>Gestor: <b>Igor</b> | Unidade: Catalão-GO</span>
        </div>
    """, unsafe_allow_html=True)

    if st.session_state['pagina'] == "Boas-vindas":
        st.markdown(f"""
            <div class='welcome-card'>
                <h2 style='color:#181C32;'>Bem-vindo ao UAU Logística, Igor.</h2>
                <p style='color:#7E8299;'>Sua plataforma está configurada e pronta para gerenciar os 15.160 itens da base tributária.</p>
                <hr style='border: 0.5px solid #EBEDF3; margin: 30px 0;'>
                <div style='display:flex; gap:30px;'>
                    <div style='flex:1; background:#F3F6F9; padding:20px; border-radius:8px;'>
                        <b style='color:#3699FF;'>Atalhos Rápidos:</b><br>
                        <small>Utilize o menu lateral para acessar as ferramentas de cálculo e consulta.</small>
                    </div>
                    <div style='flex:1; background:#F3F6F9; padding:20px; border-radius:8px;'>
                        <b style='color:#3699FF;'>Status do Servidor:</b><br>
                        <small>Conexão estável com Google Maps API e Base SEFAZ.</small>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
