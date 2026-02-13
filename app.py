import streamlit as st

# 1. Configuração de Página
st.set_page_config(page_title="UAU Logística", layout="wide")

# 2. CSS Avançado - Estilo Software de Elite
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap');
    
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
    .sidebar-brand p { color: #38BDF8; font-size: 11px; font-weight: bold; margin:0; text-transform: uppercase; }

    /* Botões de Navegação */
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
    
    /* Cards de Conteúdo */
    .content-card {
        background: white;
        padding: 40px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .section-title { color: #0F172A; font-weight: 900; font-size: 48px; margin-bottom: 10px; letter-spacing: -2px; }
    .accent-bar { width: 60px; height: 6px; background: #38BDF8; margin-bottom: 30px; }
    
    /* Caixa de Login */
    .login-box {
        background: white;
        padding: 30px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Sessão
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False
if 'pagina' not in st.session_state:
    st.session_state['pagina'] = "Boas-vindas"

if not st.session_state['autenticado']:
    # --- TELA DE ENTRADA (LANDING PAGE + LOGIN) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_info, col_spacer, col_login = st.columns([1.4, 0.2, 1])
    
    with col_info:
        st.markdown("<p style='color: #38BDF8; font-weight: 800; text-transform: uppercase; letter-spacing: 2px;'>Boas-vindas ao</p>", unsafe_allow_html=True)
        st.markdown("<h1 class='section-title'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
        st.markdown("<div class='accent-bar'></div>", unsafe_allow_html=True)
        st.markdown("""
            <h3 style='color: #1E293B;'>Inteligência e Performance Operacional</h3>
            <p style='color: #475569; font-size: 18px; line-height: 1.6;'>
                Transformamos dados fiscais e operacionais em decisões que geram lucro. A plataforma definitiva para quem busca 
                blindagem tributária NCM e otimização máxima de rotas no transporte rodoviário.
            </p>
            <br>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 20px;'>
                <div>
                    <b style='color: #0F172A;'>🛡️ Conformidade Fiscal</b><br>
                    <small style='color: #64748B;'>Base atualizada de 15.160 itens NCM.</small>
                </div>
                <div>
                    <b style='color: #0F172A;'>📈 Máxima Rentabilidade</b><br>
                    <small style='color: #64748B;'>Cálculo de margem líquida por frete.</small>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col_login:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown("<h3 style='margin-top:0; color:#0F172A;'>Acesso Restrito</h3>", unsafe_allow_html=True)
        user_input = st.text_input("Identificação do Gestor", key="user")
        pass_input = st.text_input("Chave de Acesso", type="password", key="pass")
        if st.button("ENTRAR NO SISTEMA", use_container_width=True):
            if user_input == "gestor.vip" and pass_input == "UAU2026":
                st.session_state['autenticado'] = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- INTERFACE INTERNA ---
    with st.sidebar:
        st.markdown("""
            <div class='sidebar-brand'>
                <h2>UAU LOGÍSTICA</h2>
                <p>Intelligence & Performance</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Início / Painel"): 
            st.session_state['pagina'] = "Boas-vindas"
            st.rerun()
        if st.button("Consulta NCM"): 
            st.session_state['pagina'] = "NCM"
            st.rerun()
        if st.button("Simulador de Rotas"): 
            st.session_state['pagina'] = "Mapas"
            st.rerun()
        if st.button("Quem Somos"): 
            st.session_state['pagina'] = "Quem Somos"
            st.rerun()
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if st.button("SAIR"):
            st.session_state['autenticado'] = False
            st.rerun()

    # --- CONTEÚDO ---
    if st.session_state['pagina'] == "Boas-vindas":
        st.markdown("<div class='content-card'><h1 style='margin:0;'>Painel Operacional</h1><p>Bem-vindo de volta, Igor. O sistema está pronto para operar.</p></div>", unsafe_allow_html=True)

    elif st.session_state['pagina'] == "Quem Somos":
        st.markdown("<h1 class='section-title'>Quem Somos</h1><div class='accent-bar'></div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='content-card'>
                <h3>🚛 UAU Logística – Inovação a Serviço da Logística</h3>
                <p style='color:#475569; line-height:1.8;'>
                    A UAU Logística nasceu para resolver um dos maiores desafios do transporte rodoviário: transformar informações fiscais e operacionais em decisões que geram lucro.
                </p>
                <p style='color:#475569; line-height:1.8;'>Nossa plataforma auxilia transportadores e gestores a:</p>
                <ul style='color:#475569; line-height:2;'>
                    <li>Garantir conformidade fiscal nas operações</li>
                    <li>Reduzir riscos de autuações</li>
                    <li>Otimizar rotas com foco em rentabilidade</li>
                    <li>Tomar decisões baseadas em dados reais</li>
                </ul>
                <p style='font-weight:600; color:#0F172A;'>Mais do que um sistema, somos um apoio estratégico para quem vive da logística no Brasil.</p>
            </div>
            <div class='content-card' style='border-left: 5px solid #38BDF8;'>
                <h3 style='color:#38BDF8;'>🎯 Nossa Visão</h3>
                <p style='color:#475569; font-size:18px;'>Ser referência nacional como plataforma inteligente de apoio à decisão, ajudando operações logísticas a crescer com segurança jurídica e máxima eficiência financeira.</p>
            </div>
        """, unsafe_allow_html=True)
