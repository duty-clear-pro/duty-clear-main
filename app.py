import streamlit as st

# 1. Configuração de Página
st.set_page_config(page_title="UAU Logística", layout="wide")

# 2. CSS Profissional - Estilo Cockpit Marinho
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F1F5F9; }
    
    /* Inputs com alto contraste para não sumir no fundo */
    .stTextInput input, .stSelectbox [data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border: 2px solid #0F172A !important;
        color: #0F172A !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }

    /* Sidebar Marinho */
    [data-testid="stSidebar"] { background-color: #0F172A !important; }
    
    /* Cards de Logística (Status da Frota) */
    .log-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        border-top: 5px solid #38BDF8;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        text-align: center;
    }
    .log-card h3 { color: #0F172A; font-size: 16px; margin-bottom: 5px; }
    .log-card h1 { color: #38BDF8; font-size: 32px; margin: 0; font-weight: 800; }
    
    /* Content Card */
    .content-card { 
        background: white; 
        padding: 35px; 
        border-radius: 12px; 
        border: 1px solid #E2E8F0; 
        margin-bottom: 20px; 
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Sessão
if 'autenticado' not in st.session_state: st.session_state['autenticado'] = False
if 'pagina' not in st.session_state: st.session_state['pagina'] = "Início"

if not st.session_state['autenticado']:
    # --- LOGIN ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, space, c2 = st.columns([1.5, 0.1, 1])
    with c1:
        st.markdown("<div style='background:#0F172A; padding:50px; border-radius:20px; color:white;'><h1>UAU LOGÍSTICA</h1><p style='color:#38BDF8; font-weight:bold;'>Inovação e Performance Operacional</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div style='background:white; padding:40px; border-radius:20px; border:1px solid #CBD5E1;'>", unsafe_allow_html=True)
        u = st.text_input("Identificação do Gestor", key="u_login")
        p = st.text_input("Chave de Acesso", type="password", key="p_login")
        if st.button("ACESSAR COCKPIT", use_container_width=True):
            if u == "gestor.vip" and p == "UAU2026":
                st.session_state['autenticado'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
else:
    # --- MENU LATERAL ---
    with st.sidebar:
        st.markdown("<div style='padding:20px; text-align:center;'><h2 style='color:white;'>UAU LOGÍSTICA</h2></div>", unsafe_allow_html=True)
        if st.button("📊 Dashboard"): st.session_state['pagina'] = "Início"; st.rerun()
        if st.button("🚛 Logística & Frota"): st.session_state['pagina'] = "Logistica"; st.rerun()
        if st.button("⚖️ Consulta NCM"): st.session_state['pagina'] = "NCM"; st.rerun()
        if st.button("🏢 Quem Somos"): st.session_state['pagina'] = "Sobre"; st.rerun()
        st.markdown("<br><br>")
        if st.button("SAIR"): st.session_state['autenticado'] = False; st.rerun()

    # --- PÁGINAS ---
    if st.session_state['pagina'] == "Logistica":
        st.markdown("<h1 style='color:#0F172A;'>Monitor Logístico</h1>", unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1: st.markdown("<div class='log-card'><h3>Bitrem</h3><h1>08</h1><p>Ativos</p></div>", unsafe_allow_html=True)
        with col2: st.markdown("<div class='log-card'><h3>Vanderleia</h3><h1>12</h1><p>Ativos</p></div>", unsafe_allow_html=True)
        with col3: st.markdown("<div class='log-card'><h3>Truck</h3><h1>05</h1><p>Manutenção</p></div>", unsafe_allow_html=True)
        with col4: st.markdown("<div class='log-card'><h3>Rotas</h3><h1>24</h1><p>Hoje</p></div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.container():
            st.markdown("<div class='content-card'><h3>Simulador de Operação</h3>", unsafe_allow_html=True)
            c_origem, c_destino, c_veiculo = st.columns(3)
            with c_origem: st.text_input("Cidade Origem (UF)", key="origem")
            with c_destino: st.text_input("Cidade Destino (UF)", key="destino")
            with c_veiculo: st.selectbox("Configuração", ["9 Eixos", "7 Eixos", "Vanderleia", "Toco"], key="config")
            if st.button("CALCULAR VIABILIDADE", use_container_width=True):
                st.info("Processando dados de rota e custos fixos...")
            st.markdown("</div>", unsafe_allow_html=True)

    elif st.session_state['pagina'] == "Início":
        st.markdown("<div class='content-card'><h1>Dashboard Principal</h1><p>Bem-vindo ao cockpit Duty Clear. Servidor operando em 100%.</p></div>", unsafe_allow_html=True)

    elif st.session_state['pagina'] == "NCM":
        st.markdown("<div class='content-card'><h2>Busca Inteligente Duty Clear</h2><p>Base de 15.160 itens disponível para consulta.</p></div>", unsafe_allow_html=True)
    
    elif st.session_state['pagina'] == "Sobre":
        st.markdown("""
            <div class='content-card'>
                <h1 style='color:#0F172A; font-weight:900;'>Quem Somos</h1>
                <p>A UAU Logística nasceu para transformar informações em lucro real no transporte rodoviário.</p>
                <ul style='line-height:2;'>
                    <li>Garantir conformidade fiscal.</li>
                    <li>Reduzir riscos de autuações.</li>
                    <li>Otimizar rotas com foco em rentabilidade.</li>
                </ul>
                <div style='background:#F1F5F9; padding:20px; border-radius:10px; border-left:6px solid #38BDF8; margin-top:20px;'>
                    <h3 style='margin:0; color:#38BDF8;'>🎯 Nossa Visão</h3>
                    <p>Ser referência nacional em inteligência logística e segurança jurídica.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
