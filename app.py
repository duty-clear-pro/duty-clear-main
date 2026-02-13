import streamlit as st

# 1. Configuração de Página
st.set_page_config(page_title="UAU Logística", layout="wide")

# 2. CSS Profissional - Estilo Cockpit Marinho
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F1F5F9; }
    
    /* Inputs com alto contraste */
    .stTextInput input, .stSelectbox select {
        background-color: #F8FAFC !important;
        border: 2px solid #0F172A !important;
        color: #0F172A !important;
        font-weight: 600 !important;
    }

    /* Sidebar Marinho */
    [data-testid="stSidebar"] { background-color: #0F172A !important; }
    
    /* Cards de Logística */
    .log-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        border-top: 5px solid #38BDF8;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        text-align: center;
    }
    .content-card { background: white; padding: 35px; border-radius: 12px; border: 1px solid #E2E8F0; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Sessão
if 'autenticado' not in st.session_state: st.session_state['autenticado'] = False
if 'pagina' not in st.session_state: st.session_state['pagina'] = "Início"

if not st.session_state['autenticado']:
    # --- LOGIN (MANTER PADRÃO APROVADO) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, space, c2 = st.columns([1.5, 0.1, 1])
    with c1:
        st.markdown("<div style='background:#0F172A; padding:50px; border-radius:20px; color:white;'><h1>UAU LOGÍSTICA</h1><p style='color:#38BDF8;'>Inovação e Performance</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div style='background:white; padding:40px; border-radius:20px; border:1px solid #CBD5E1;'>", unsafe_allow_html=True)
        u = st.text_input("Identificação")
        p = st.text_input("Chave", type="password")
        if st.button("ACESSAR COCKPIT", use_container_width=True):
            if u == "gestor.vip" and p == "UAU2026":
                st.session_state['autenticado'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
else:
    # --- MENU LATERAL ---
    with st.sidebar:
        st.markdown("<h2 style='color:white; text-align:center;'>UAU LOGÍSTICA</h2>", unsafe_allow_html=True)
        if st.button("📊 Dashboard"): st.session_state['pagina'] = "Início"; st.rerun()
        if st.button("🚛 Logística & Frota"): st.session_state['pagina'] = "Logistica"; st.rerun()
        if st.button("⚖️ Consulta NCM"): st.session_state['pagina'] = "NCM"; st.rerun()
        if st.button("🏢 Quem Somos"): st.session_state['pagina'] = "Sobre"; st.rerun()
        st.markdown("<br><br>")
        if st.button("SAIR"): st.session_state['autenticado'] = False; st.rerun()

    # --- ÁREA DE LOGÍSTICA ---
    if st.session_state['pagina'] == "Logistica":
        st.markdown("<h1 style='color:#0F172A;'>Monitor Logístico</h1>", unsafe_allow_html=True)
        
        # Grid de Status de Frota
        col1, col2, col3, col4 = st.columns(4)
        with col1: st.markdown("<div class='log-card'><h3>Bitrem</h3><h1 style='color:#38BDF8;'>08</h1><p>Ativos</p></div>", unsafe_allow_html=True)
        with col2: st.markdown("<div class='log-card'><h3>Vanderleia</h3><h1 style='color:#38BDF8;'>12</h1><p>Ativos</p></div>", unsafe_allow_html=True)
        with col3: st.markdown("<div class='log-card'><h3>Truck</h3><h1 style='color:#38BDF8;'>05</h1><p>Em Manutenção</p></div>", unsafe_allow_html=True)
        with col4: st.markdown("<div class='log-card'><h3>Rotas</h3><h1 style='color:#38BDF8;'>24</h1><p>Hoje</p></div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        
        # Simulador de Frete/Rota
        st.markdown("<div class='content-card'><h3>Simulador de Operação</h3>", unsafe_allow_html=True)
        c_origem, c_destino, c_veiculo = st.columns(3)
        with c_origem: st.text_input("Cidade Origem (UF)")
        with c_destino: st.text_input("Cidade Destino (UF)")
        with c_veiculo: st.selectbox("Config
