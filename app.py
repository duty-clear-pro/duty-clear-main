import streamlit as st

# 1. Configuração de Página
st.set_page_config(page_title="UAU Logística", layout="wide")

# 2. CSS Profissional - Cores Sólidas e Fontes de Sistema
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    
    /* Fundo Principal */
    .stApp { background-color: #F1F5F9; }
    
    /* SIDEBAR MARINHO */
    [data-testid="stSidebar"] { 
        background-color: #0F172A !important; 
        min-width: 300px !important;
    }
    
    /* CABEÇALHO SIDEBAR */
    .sidebar-brand {
        padding: 30px 20px;
        text-align: center;
        color: white;
        border-bottom: 1px solid #1E293B;
        margin-bottom: 20px;
    }
    .sidebar-brand h2 { font-weight: 900; letter-spacing: -1px; margin:0; }

    /* MENU LATERAL */
    div.stButton > button {
        width: 100%;
        background-color: transparent !important;
        color: #94A3B8 !important;
        border: none !important;
        height: 55px;
        text-align: left;
        font-weight: 600;
        font-size: 15px;
        padding-left: 25px;
        border-radius: 0px;
        border-left: 4px solid transparent !important;
    }
    div.stButton > button:hover {
        background-color: #1E293B !important;
        color: #F8FAFC !important;
        border-left: 4px solid #38BDF8 !important;
    }
    
    /* CARD DE ENTRADA MARINHO (A que você gostou) */
    .hero-card {
        background-color: #0F172A;
        padding: 60px;
        border-radius: 20px;
        color: white;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }
    .hero-title { font-size: 52px; font-weight: 900; letter-spacing: -2px; line-height: 1; }
    .hero-accent { color: #38BDF8; font-weight: 800; }
    
    /* CARDS INTERNOS */
    .content-card {
        background: white;
        padding: 40px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        color: #0F172A;
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Sessão
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False
if 'pagina' not in st.session_state:
    st.session_state['pagina'] = "Boas-vindas"

if not st.session_state['autenticado']:
    # --- TELA DE ENTRADA IMPACTANTE (AZUL MARINHO) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_left, col_spacer, col_right = st.columns([1.5, 0.1, 1])
    
    with col_left:
        st.markdown(f"""
            <div class='hero-card'>
                <p style='color: #38BDF8; font-weight: bold; letter-spacing: 2px;'>BEM-VINDO</p>
                <h1 class='hero-title'>UAU LOGÍSTICA</h1>
                <p style='font-size: 20px; margin-top: 20px; color: #94A3B8;'>
                    Inteligência de Performance e Blindagem Fiscal NCM.
                </p>
                <hr style='border: 0.1px solid #1E293B; margin: 30px 0;'>
                <p style='font-size: 16px; line-height: 1.6;'>
                    O cockpit definitivo para transportadores que buscam conformidade e lucro real no frete.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div style="background:white; padding:40px; border-radius:20px; border:1px solid #E2E8F0;">', unsafe_allow_html=True)
        st.markdown("<h3 style='color:#0F172A; margin-top:0;'>Acesso ao Cockpit</h3>", unsafe_allow_html=True)
        user_in = st.text_input("Identificação", key="login_u")
        pass_in = st.text_input("Chave", type="password", key="login_p")
        if st.button("AUTENTICAR", use_container_width=True):
            if user_in == "gestor.vip" and pass_in == "UAU2026":
                st.session_state['autenticado'] = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- INTERFACE INTERNA ---
    with st.sidebar:
        st.markdown("<div class='sidebar-brand'><h2>UAU LOGÍSTICA</h2></div>", unsafe_allow_html=True)
        if st.button("Página Inicial"): st.session_state['pagina'] = "Boas-vindas"; st.rerun()
        if st.button("Consulta NCM"): st.session_state['pagina'] = "NCM"; st.rerun()
        if st.button("Quem Somos"): st.session_state['pagina'] = "Quem Somos"; st.rerun()
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("SAIR"): st.session_state['autenticado'] = False; st.rerun()

    if st.session_state['pagina'] == "Boas-vindas":
        st.markdown("<div class='content-card'><h1>Painel Operacional</h1><p>Sistema pronto para uso, Igor.</p></div>", unsafe_allow_html=True)
    
    elif st.session_state['pagina'] == "Quem Somos":
        st.markdown("""
            <div class='content-card'>
                <h1 style='color:#0F172A; font-weight:900;'>Quem Somos</h1>
                <p style='color:#475569; font-size:18px;'>A <b>UAU Logística</b> nasceu para transformar o transporte rodoviário.</p>
                <ul style='line-height:2.5;'>
                    <li>Garantir conformidade fiscal.</li>
                    <li>Reduzir riscos de autuações.</li>
                    <li>Otimizar rotas com foco em rentabilidade.</li>
                </ul>
                <div style='background:#F1F5F9; padding:20px; border-radius:10px; border-left: 6px solid #38BDF8;'>
                    <h4 style='margin:0; color:#0F172A;'>🎯 Nossa Visão</h4>
                    <p style='margin:0; color:#475569;'>Referência nacional em inteligência logística e segurança jurídica.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
