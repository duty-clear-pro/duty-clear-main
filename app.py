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
    
    /* Estilo do Login */
    .login-box {
        background: white;
        padding: 40px;
        border-radius: 15px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Sessão
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False
if 'pagina' not in st.session_state:
    st.session_state['pagina'] = "Boas-vindas"

if not st.session_state['autenticado']:
    # --- TELA DE ENTRADA ROBUSTA (LANDING PAGE + LOGIN) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_info, col_spacer, col_login = st.columns([1.4, 0.2, 1])
    
    with col_info:
        st.markdown("<p style='color: #38BDF8; font-weight: 800; text-transform: uppercase; letter-spacing: 2px;'>Boas-vindas ao</p>", unsafe_allow_html=True)
        st.markdown("<h1 class='section-title'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
        st.markdown("<div class='accent-bar'></div>", unsafe_allow_html=True)
        st.markdown("""
            <h3 style='color: #1E293B;'>Inteligência e Performance Operacional</h3>
            <p style='color: #475569; font-size: 18px; line-height: 1.6;'>
                Transformamos dados fiscais e operacionais em lucro real. A plataforma definitiva para quem busca 
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
                <div>
                    <b style='color: #0F172A;'>🗺️ Rotas Inteligentes</b><br>
                    <small style='color: #64748B;'>Integração avançada com Google Maps.</small>
                </div>
                <div>
                    <b style='color: #0F172A;'>⚡ Decisão em Tempo Real</b><br>
                    <small style='color: #64748B;'>Painéis de dados diretos e precisos.</small>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col_login:
