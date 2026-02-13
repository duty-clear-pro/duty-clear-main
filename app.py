import streamlit as st

# 1. Configuração de Software de Performance
st.set_page_config(page_title="UAU Logística", layout="wide")

# 2. CSS Profissional (Inspirado no template, mas focado em Logística)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    
    /* SIDEBAR: Barra Sólida de Ferramentas */
    [data-testid="stSidebar"] { 
        background-color: #0F172A !important; 
        min-width: 260px !important; 
    }
    
    /* Botões da Barra Lateral */
    div.stButton > button {
        width: 100%;
        background-color: transparent !important;
        color: #94A3B8 !important;
        border: none !important;
        height: 55px;
        text-align: left;
        font-weight: 600;
        border-left: 4px solid transparent !important;
        padding-left: 20px;
        border-radius: 0px;
    }
    div.stButton > button:hover {
        background-color: #1E293B !important;
        color: #F8FAFC !important;
        border-left: 4px solid #38BDF8 !important;
    }

    /* Estilo do Conteúdo de Boas-Vindas */
    .welcome-container {
        background: white;
        padding: 50px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
    }
    .main-title { color: #0F172A; font-size: 48px; font-weight: 900; letter-spacing: -1px; }
    .accent-line { width: 60px; height: 5px; background: #38BDF8; margin: 20px 0; }
    .description-text { color: #475569; font-size: 18px; line-height: 1.6; max-width: 700px; }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Navegação
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False
if 'pagina' not in st.session_state:
    st.session_state['pagina'] = "Boas-vindas"

if not st.session_state['autenticado']:
    # --- TELA DE ACESSO ---
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        with st.container():
            st.markdown("<h1 style='text-align:center; color:#0F172A;'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
            u = st.text_input("Identificação")
            p = st.text_input("Chave de Acesso", type="password")
            if st.button("ACESSAR SISTEMA", use_container_width=True):
                if u == "gestor.vip" and p == "UAU2026":
                    st.session_state['autenticado'] = True
                    st.rerun()

else:
    # --- INTERFACE DE OPERAÇÃO ---
    with st.sidebar:
        st.markdown("<div style='padding:20px 0;'><h2 style='color:white; text-align:center;'>UAU LOGÍSTICA</h2></div>", unsafe_allow_html=True)
        st.divider()
        if st.button("Página Inicial"): st.session_state['pagina'] = "Boas-vindas"; st.rerun()
        if st.button("Consulta NCM"): st.session_state['pagina'] = "NCM"; st.rerun()
        if st.button("Simulador de Rotas"): st.session_state['pagina'] = "Mapas"; st.rerun()
        if st.button("Cálculo de Frete"): st.session_state['pagina'] = "Financeiro"; st.rerun()
        st.divider()
        if st.button("Sair"):
            st.session_state['autenticado'] = False
            st.rerun()

    # ÁREA DE CONTEÚDO
    if st.session_state['pagina'] == "Boas-vindas":
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
            <div class='welcome-container'>
                <h1 class='main-title'>Bem-vindo à sua Central de Inteligência.</h1>
                <div class='accent-line'></div>
                <p class='description-text'>
                    O <b>UAU Logística</b> foi desenvolvido para otimizar operações complexas, unindo o cálculo de rotas dinâmicas à precisão fiscal da base NCM.
                </p>
                <br>
                <h4 style='color:#0F172A;'>O que você pode fazer agora:</h4>
                <ul style='color:#475569; line-height:2;'>
                    <li><b>Consultar NCM:</b> Pesquisa rápida na base de 15.160 itens tributários.</li>
                    <li><b>Planejar Rotas:</b> Integração com mapas para definição de trajetos e tempos.</li>
                    <li><b>Cálculo de Margem:</b> Simulação financeira de fretes com foco em lucro líquido.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
