import streamlit as st

# 1. Configuração de Página
st.set_page_config(page_title="UAU Logística", layout="wide")

# 2. CSS - Estilo Cockpit Marinho (Contraste Máximo)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F1F5F9; }
    
    /* Inputs visíveis */
    .stTextInput input {
        border: 2px solid #0F172A !important;
        background-color: white !important;
        color: #0F172A !important;
    }

    /* Sidebar Marinho */
    [data-testid="stSidebar"] { background-color: #0F172A !important; }
    
    /* Cards de Boas-vindas */
    .welcome-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        border-left: 8px solid #38BDF8;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    .stat-box {
        background: #0F172A;
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Sessão
if 'autenticado' not in st.session_state: st.session_state['autenticado'] = False
if 'pagina' not in st.session_state: st.session_state['pagina'] = "Início"

if not st.session_state['autenticado']:
    # --- TELA DE LOGIN (Padrão Aprovado) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, space, c2 = st.columns([1.5, 0.1, 1])
    with c1:
        st.markdown("<div style='background:#0F172A; padding:60px; border-radius:20px; color:white;'><h1 style='font-size:50px;'>UAU LOGÍSTICA</h1><p style='color:#38BDF8; font-size:20px;'>Inovação e Performance Operacional</p></div>", unsafe_allow_html=True)
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
    # --- INTERFACE INTERNA ---
    with st.sidebar:
        st.markdown("<div style='text-align:center; padding:20px;'><h2 style='color:white;'>UAU LOGÍSTICA</h2></div>", unsafe_allow_html=True)
        if st.button("📊 Painel de Controle"): st.session_state['pagina'] = "Início"; st.rerun()
        if st.button("🚛 Gestão de Logística"): st.session_state['pagina'] = "Logistica"; st.rerun()
        if st.button("⚖️ Consulta NCM"): st.session_state['pagina'] = "NCM"; st.rerun()
        if st.button("🏢 Quem Somos"): st.session_state['pagina'] = "Sobre"; st.rerun()
        st.markdown("<br><br>")
        if st.button("🚪 ENCERRAR SESSÃO"): st.session_state['autenticado'] = False; st.rerun()

    # --- PÁGINA INICIAL RECHEADA ---
    if st.session_state['pagina'] == "Início":
        st.markdown("<h1 style='color:#0F172A;'>Cockpit Duty Clear</h1>", unsafe_allow_html=True)
        
        # Seção de Boas-vindas
        st.markdown(f"""
            <div class='welcome-card'>
                <h2 style='margin:0; color:#0F172A;'>Olá, Gestor Igor!</h2>
                <p style='color:#475569; font-size:18px;'>O sistema está operando em regime de <b>Máxima Força</b>. 
                Sua base de inteligência fiscal está pronta para gerar rentabilidade.</p>
            </div>
        """, unsafe_allow_html=True)

        # Indicadores Rápidos
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<div class='stat-box'><h3>Base NCM</h3><h1>15.160</h1><p>Itens Blindados</p></div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='stat-box'><h3>Status</h3><h1>ATIVO</h1><p>Servidor de Alta Performance</p></div>", unsafe_allow_html=True)
        with col3:
            st.markdown("<div class='stat-box'><h3>Segurança</h3><h1>100%</h1><p>Criptografia Duty Clear</p></div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.info("💡 Dica do Dia: Utilize o Módulo de Logística para simular a margem líquida antes de fechar o frete.")

    # (Manter os outros módulos como estão)
    elif st.session_state['pagina'] == "Logistica":
        st.markdown("<h1>Gestão de Logística</h1>", unsafe_allow_html=True)
        st.info("Módulo em operação...")

    elif st.session_state['pagina'] == "Sobre":
        # Aqui entra aquele texto completo que você aprovou
        st.markdown("<div class='welcome-card'><h1>Quem Somos</h1><p>A UAU Logística nasceu para transformar...</p></div>", unsafe_allow_html=True)
