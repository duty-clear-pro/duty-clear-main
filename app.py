import streamlit as st

# 1. Configuração de Página
st.set_page_config(page_title="UAU Logística", layout="wide")

# 2. CSS Avançado - Estilo Software de Elite
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    
    /* SIDEBAR PROFISSIONAL */
    [data-testid="stSidebar"] { 
        background-color: #0F172A !important; 
        min-width: 300px !important;
    }
    
    /* Branding no Menu */
    .sidebar-brand {
        padding: 30px 20px;
        text-align: center;
        color: white;
        border-bottom: 1px solid #1E293B;
        margin-bottom: 20px;
    }
    .sidebar-brand h2 { font-weight: 900; letter-spacing: -1px; margin:0; }
    .sidebar-brand p { color: #38BDF8; font-size: 12px; font-weight: bold; margin:0; }

    /* Botões de Navegação Estilo 'Tabs' */
    div.stButton > button {
        width: 100%;
        background-color: transparent !important;
        color: #94A3B8 !important;
        border: none !important;
        height: 50px;
        text-align: left;
        font-weight: 500;
        font-size: 15px;
        padding-left: 25px;
        border-radius: 0px;
        border-left: 4px solid transparent !important;
        transition: 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #1E293B !important;
        color: #F8FAFC !important;
        border-left: 4px solid #38BDF8 !important;
    }
    
    /* Estilo dos Cards de Conteúdo */
    .content-card {
        background: white;
        padding: 40px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }
    .section-title { color: #0F172A; font-weight: 800; font-size: 32px; margin-bottom: 10px; }
    .accent-bar { width: 50px; height: 4px; background: #38BDF8; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Sessão
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False
if 'pagina' not in st.session_state:
    st.session_state['pagina'] = "Boas-vindas"

if not st.session_state['autenticado']:
    # --- TELA DE ACESSO CLEAN ---
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.markdown("<br><br><br><br>", unsafe_allow_html=True)
        with st.container():
            st.markdown("<h1 style='text-align:center; color:#0F172A; font-weight:900;'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
            u = st.text_input("Identificação do Gestor")
            p = st.text_input("Chave de Acesso", type="password")
            if st.button("AUTENTICAR NO SERVIDOR", use_container_width=True):
                if u == "gestor.vip" and p == "UAU2026":
                    st.session_state['autenticado'] = True
                    st.rerun()
else:
    # --- SIDEBAR PROFISSIONAL ---
    with st.sidebar:
        st.markdown("""
            <div class='sidebar-brand'>
                <h2>UAU LOGÍSTICA</h2>
                <p>INTELLIGENCE & PERFORMANCE</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Página Inicial"): st.session_state['pagina'] = "Boas-vindas"; st.rerun()
        if st.button("Consulta NCM"): st.session_state['pagina'] = "NCM"; st.rerun()
        if st.button("Simulador de Rotas"): st.session_state['pagina'] = "Mapas"; st.rerun()
        if st.button("Cálculo de Frete"): st.session_state['pagina'] = "Financeiro"; st.rerun()
        if st.button("Quem Somos"): st.session_state['pagina'] = "Quem Somos"; st.rerun()
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if st.button("ENCERRAR SESSÃO"):
            st.session_state['autenticado'] = False
            st.rerun()

    # --- ÁREA DE CONTEÚDO ---
    if st.session_state['pagina'] == "Boas-vindas":
        st.markdown("""
            <div class='content-card'>
                <h1 class='section-title'>Bem-vindo à sua Central de Inteligência.</h1>
                <div class='accent-bar'></div>
                <p style='color:#475569; font-size:18px;'>O sistema UAU Logística integra automação de rotas e blindagem fiscal NCM em um único cockpit.</p>
                <br>
                <h4>Operações Disponíveis:</h4>
                <p>• Gestão de frotas e planejamento de carga.<br>• Consulta instantânea de alíquotas NCM.<br>• Simulação de rentabilidade líquida.</p>
            </div>
        """, unsafe_allow_html=True)

    elif st.session_state['pagina'] == "Quem Somos":
        st.markdown("""
            <div class='content-card'>
                <h1 class='section-title'>Quem Somos</h1>
                <div class='accent-bar'></div>
                <h3>Inovação a Serviço da Logística</h3>
                <p style='color:#475569; line-height:1.8;'>
                    A <b>UAU Logística</b> nasceu da necessidade de transformar dados brutos em decisões estratégicas. 
                    Nossa missão é fornecer aos transportadores e gestores uma ferramenta de alta performance que garanta a 
                    conformidade fiscal e a otimização máxima de rotas no território nacional.
                </p>
                <br>
                <h3>Nossa Visão</h3>
                <p style='color:#475569;'>Ser a
