import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DE ALTO NÍVEL
st.set_page_config(page_title="TradeMind Intelligence", layout="wide", initial_sidebar_state="expanded")

# 2. CSS CUSTOMIZADO (VISUAL ESCURO PREMIUM - SEM EMOJIS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&family=Inter:wght@400;700;900&display=swap');
    
    /* Fundo e Texto */
    .stApp { background-color: #0A0A0B; color: #E4E4E7; }
    
    /* Sidebar Fixa e Sóbria */
    [data-testid="stSidebar"] {
        background-color: #121214 !important;
        border-right: 1px solid #27272A;
    }

    /* Cards Estilo Dashboard de Dados */
    .stat-card {
        background-color: #18181B;
        padding: 24px;
        border: 1px solid #27272A;
        border-radius: 4px;
        margin-bottom: 16px;
    }
    
    /* Disclaimer Obrigatório Padronizado */
    .disclaimer-text {
        font-size: 11px;
        color: #71717A;
        line-height: 1.6;
        padding: 20px;
        border-top: 1px solid #27272A;
        margin-top: 40px;
        text-align: justify;
    }

    /* Estilo de Botões Corporativos */
    .stButton > button {
        background-color: #27272A;
        color: #FFFFFF;
        border: 1px solid #3F3F46;
        border-radius: 2px;
        font-family: 'Roboto Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 1px;
        width: 100%;
    }
    .stButton > button:hover { background-color: #3F3F46; border-color: #52525B; }

    /* Inputs */
    input { background-color: #18181B !important; color: white !important; border: 1px solid #27272A !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE DISCLAIMER (REUTILIZÁVEL)
def render_disclaimer():
    st.markdown("""
        <div class="disclaimer-text">
            As informações disponibilizadas pela TradeMind possuem caráter exclusivamente informativo e de apoio à decisão. 
            Não substituem consultoria jurídica, contábil ou aduaneira. A responsabilidade pelo uso dos dados e pelo 
            cumprimento da legislação vigente é integralmente do usuário.
        </div>
    """, unsafe_allow_html=True)

# 4. CONTROLE DE ACESSO
if 'auth' not in st.session_state: st.session_state.auth = False
if 'page' not in st.session_state: st.session_state.page = "Dashboard"

# --- FLUXO DE TELAS ---

if not st.session_state.auth:
    # TELA DE ENTRADA (PREMIUM TECH)
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size: 64px; font-weight: 900; letter-spacing: -2px;'>TRADEMIND AI</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #A1A1AA;'>Inteligência em Classificação Fiscal e Gestão de Risco NCM</h3>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 18px; color: #71717A; max-width: 500px;'>
                Plataforma estratégica para antecipação de risco aduaneiro e otimização de margem operacional 
                em operações de comércio exterior de alta complexidade.
            </p>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        with st.form("Login"):
            st.markdown("AUTENTICAÇÃO DE ACESSO")
            user = st.text_input("USUÁRIO")
            pw = st.text_input("CHAVE", type="password")
            if st.form_submit_button("ACESSAR TERMINAL"):
                if user == "admin" and pw == "trade2026":
                    st.session_state.auth = True
                    st.rerun()
    render_disclaimer()

else:
    # BARRA LATERAL (SIDEBAR)
    with st.sidebar:
        st.markdown("<h2 style='letter-spacing: -1px;'>TRADEMIND</h2>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 10px; color: #52525B;'>SISTEMA DE APOIO À DECISÃO</p>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("DASHBOARD ESTRATÉGICO"): st.session_state.page = "Dashboard"; st.rerun()
        if st.button("INTELIGÊNCIA NCM"): st.session_state.page = "NCM"; st.rerun()
        if st.button("SIMULAÇÃO TRIBUTÁRIA"): st.session_state.page = "Simul"; st.rerun()
        if st.button("QUEM SOMOS"): st.session_state.page = "About"; st.rerun()
        st.markdown("<br><br>")
        if st.button("LOGOUT"): st.session_state.auth = False; st.rerun()

    # 1️⃣ DASHBOARD ESTRATÉGICO
    if st.session_state.page == "Dashboard":
        st.markdown("<h1>DASHBOARD EXECUTIVO</h1>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown("<div class='stat-card'><small>NCM ANALISADAS</small><h2>1,248</h2></div>", unsafe_allow_html=True)
        with c2: st.markdown("<div class='stat-card'><small>ALERTAS FISCAIS</small><h2 style='color: #F87171;'>03</h2></div>", unsafe_allow_html=True)
        with c3: st.markdown("<div class='stat-card'><small>SCORE DE RISCO</small><h2 style='color: #4ADE80;'>MÍNIMO</h2></div>", unsafe_allow_html=True)
        
        st.markdown("<div class='stat-card'><h3>DIRETRIZES OPERACIONAIS</h3>"
                    "<p style='color: #A1A1AA;'>O foco atual do sistema é a antecipação de risco de canal e a preservação "
                    "da margem operacional através da precisão técnica na classificação de mercadorias.</p></div>", unsafe_allow_html=True)

    # 2️⃣ INTELIGÊNCIA NCM
    elif st.session_state.page == "NCM":
        st.markdown("<h1>INTELIGÊNCIA NCM</h1>", unsafe_allow_html=True)
        ncm_code = st.text_input("CÓDIGO NCM", placeholder="0000.00.00")
        ncm_desc = st.text_area("DESCRIÇÃO TÉCNICA DA MERCADORIA")
        if st.button("INICIAR ANÁLISE ESTRATÉGICA"):
            st.info("SISTEMA EM PROCESSAMENTO: CRUZAMENTO DE DADOS COM BANCO DE LEGISLAÇÃO FEDERAL.")

    # 3️⃣ SIMULAÇÃO TRIBUTÁRIA (MOTOR DE CÁLCULO)
    elif st.session_state.page == "Simul":
        st.markdown("<h1>SIMULAÇÃO TRIBUTÁRIA</h1>", unsafe_allow_html=True)
        col_f, col_a = st.columns(2)
        fob = col_f.number_input("VALOR DA OPERAÇÃO (USD)", min_value=0.0)
        aliq = col_a.number_input("ALÍQUOTA ESTIMADA (%)", min_value=0.0)
        
        if fob > 0:
            taxa = 5.12 # Valor fixo para simulação
            impacto = (fob * taxa) * (aliq / 100)
            st.markdown(f"<div class='stat-card'><h3>RESULTADO DA PROJEÇÃO</h3>"
                        f"<p>BASE DE CÁLCULO: R$ {(fob * taxa):,.2f}</p>"
                        f"<h2>IMPOSTO ESTIMADO: R$ {impacto:,.2f}</h2></div>", unsafe_allow_html=True)

    # 4️⃣ QUEM SOMOS (TOP)
    elif st.session_state.page == "About":
        st.markdown("<h1>QUEM SOMOS</h1>", unsafe_allow_html=True)
        st.markdown("""
            <div class='stat-card'>
                <p style='font-size: 20px; font-weight: 700;'>TRADE MIN INTELLIGENCE</p>
                <p style='color: #A1A1AA;'>Somos uma solução focada em inteligência aduaneira e governança tributária. 
                Nossa arquitetura foi desenhada para atender a alta demanda de precisão no Comércio Exterior, 
                eliminando a subjetividade na classificação fiscal e garantindo segurança jurídica no pré-embarque.</p>
            </div>
        """, unsafe_allow_html=True)

    render_disclaimer()
