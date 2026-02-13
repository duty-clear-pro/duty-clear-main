import streamlit as st

# 1. Configuração de Página
st.set_page_config(page_title="UAU Logística", layout="wide")

# 2. CSS Profissional - Forçando o Contraste e Preenchimento
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F1F5F9; }
    
    /* Inputs com bordas pretas para máxima visão */
    .stTextInput input {
        border: 2px solid #0F172A !important;
        background-color: white !important;
        color: #0F172A !important;
        height: 45px !important;
    }

    /* Sidebar Marinho */
    [data-testid="stSidebar"] { background-color: #0F172A !important; }
    
    /* Card de Boas-vindas Recheado */
    .welcome-banner {
        background: linear-gradient(90deg, #0F172A 0%, #1E293B 100%);
        padding: 40px;
        border-radius: 20px;
        color: white;
        margin-bottom: 30px;
        border-bottom: 5px solid #38BDF8;
    }
    
    /* Cards de Indicadores */
    .metric-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .metric-card h1 { color: #0F172A; margin: 0; font-size: 35px; }
    .metric-card p { color: #64748B; font-weight: 600; margin: 0; }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Sessão
if 'autenticado' not in st.session_state: st.session_state['autenticado'] = False
if 'pagina' not in st.session_state: st.session_state['pagina'] = "Início"

if not st.session_state['autenticado']:
    # --- TELA DE LOGIN (ESTILO IMAGEM DACB82) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, space, c2 = st.columns([1.5, 0.1, 1])
    with c1:
        st.markdown("<div style='background:#0F172A; padding:60px; border-radius:20px; color:white;'><h1>UAU LOGÍSTICA</h1><p style='color:#38BDF8; font-size:20px;'>Inovação e Performance Operacional</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div style='background:white; padding:40px; border-radius:20px; border:1px solid #CBD5E1;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#0F172A; margin-top:0;'>Acesso ao Cockpit</h3>", unsafe_allow_html=True)
        u = st.text_input("Identificação do Gestor", key="u_login")
        p = st.text_input("Chave de Acesso", type="password", key="p_login")
        if st.button("ACESSAR SISTEMA", use_container_width=True):
            if u == "gestor.vip" and p == "UAU2026":
                st.session_state['autenticado'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
else:
    # --- MENU LATERAL ---
    with st.sidebar:
        st.markdown("<div style='text-align:center; padding:20px;'><h2 style='color:white;'>UAU LOGÍSTICA</h2></div>", unsafe_allow_html=True)
        if st.button("📊 Painel Principal"): st.session_state['pagina'] = "Início"; st.rerun()
        if st.button("🚛 Logística & Frota"): st.session_state['pagina'] = "Logistica"; st.rerun()
        if st.button("⚖️ Consulta NCM"): st.session_state['pagina'] = "NCM"; st.rerun()
        if st.button("🏢 Quem Somos"): st.session_state['pagina'] = "Sobre"; st.rerun()
        st.markdown("<br><br>")
        if st.button("SAIR"): st.session_state['autenticado'] = False; st.rerun()

    # --- PÁGINA INICIAL (AGORA RECHEADA) ---
    if st.session_state['pagina'] == "Início":
        st.markdown("""
            <div class='welcome-banner'>
                <h1 style='margin:0;'>Bem-vindo ao Cockpit, Igor!</h1>
                <p style='font-size:18px; opacity:0.8;'>Sistema Duty Clear operando em modo de Máxima Performance.</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Grid de Status
        col1, col2, col3, col4 = st.columns(4)
        with col1: st.markdown("<div class='metric-card'><h1>15.160</h1><p>Itens NCM</p></div>", unsafe_allow_html=True)
        with col2: st.markdown("<div class='metric-card'><h1>100%</h1><p>Servidor Online</p></div>", unsafe_allow_html=True)
        with col3: st.markdown("<div class='metric-card'><h1>24h</h1><p>Monitoramento</p></div>", unsafe_allow_html=True)
        with col4: st.markdown("<div class='metric-card'><h1>ATIVA</h1><p>Mídia Segura</p></div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.success("✅ Todos os módulos de Inteligência Logística e Blindagem Fiscal estão carregados.")

    elif st.session_state['pagina'] == "Sobre":
        st.markdown("<div style='background:white; padding:40px; border-radius:15px; border-left:8px solid #38BDF8;'>", unsafe_allow_html=True)
        st.markdown("<h1>Quem Somos</h1>")
        st.markdown("A UAU Logística nasceu para transformar informações em lucro...")
        st.markdown("</div>", unsafe_allow_html=True)
