import streamlit as st
import pandas as pd

# 1. Configuração de Página
st.set_page_config(page_title="UAU Logística", layout="wide")

# 2. CSS Profissional (Padrão Aprovado)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F1F5F9; }
    
    /* SIDEBAR MARINHO */
    [data-testid="stSidebar"] { background-color: #0F172A !important; min-width: 300px !important; }
    .sidebar-brand { padding: 30px 20px; text-align: center; color: white; border-bottom: 1px solid #1E293B; margin-bottom: 20px; }
    
    /* BOTÕES MENU */
    div.stButton > button {
        width: 100%; background-color: transparent !important; color: #94A3B8 !important;
        border: none !important; height: 55px; text-align: left; font-weight: 600;
        padding-left: 25px; border-radius: 0px; border-left: 4px solid transparent !important;
    }
    div.stButton > button:hover { background-color: #1E293B !important; color: #F8FAFC !important; border-left: 4px solid #38BDF8 !important; }
    
    /* CARDS */
    .hero-card { background-color: #0F172A; padding: 60px; border-radius: 20px; color: white; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5); }
    .content-card { background: white; padding: 30px; border-radius: 12px; border: 1px solid #E2E8F0; color: #0F172A; margin-bottom: 20px; }
    .section-header { border-left: 5px solid #38BDF8; padding-left: 15px; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

# Inicialização de Sessão
if 'autenticado' not in st.session_state: st.session_state['autenticado'] = False
if 'pagina' not in st.session_state: st.session_state['pagina'] = "Início"

if not st.session_state['autenticado']:
    # --- TELA DE ENTRADA (DESIGN APROVADO) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, space, col2 = st.columns([1.5, 0.1, 1])
    with col1:
        st.markdown("""
            <div class='hero-card'>
                <p style='color: #38BDF8; font-weight: bold; letter-spacing: 2px;'>BEM-VINDO</p>
                <h1 style='font-size: 52px; font-weight: 900; letter-spacing: -2px;'>UAU LOGÍSTICA</h1>
                <p style='font-size: 18px; color: #94A3B8;'>Inteligência de Performance e Blindagem Fiscal NCM.</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown('<div style="background:white; padding:40px; border-radius:20px; border:1px solid #E2E8F0;">', unsafe_allow_html=True)
        st.subheader("Acesso ao Cockpit")
        u = st.text_input("Identificação")
        p = st.text_input("Chave", type="password")
        if st.button("AUTENTICAR", use_container_width=True):
            if u == "gestor.vip" and p == "UAU2026":
                st.session_state['autenticado'] = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
else:
    # --- INTERFACE INTERNA ---
    with st.sidebar:
        st.markdown("<div class='sidebar-brand'><h2>UAU LOGÍSTICA</h2></div>", unsafe_allow_html=True)
        if st.button("📊 Início / Painel"): st.session_state['pagina'] = "Início"; st.rerun()
        if st.button("⚖️ Consulta NCM"): st.session_state['pagina'] = "NCM"; st.rerun()
        if st.button("🗺️ Simulador de Rotas"): st.session_state['pagina'] = "Mapas"; st.rerun()
        if st.button("🚚 Cálculo de Frete"): st.session_state['pagina'] = "Frete"; st.rerun()
        if st.button("🏢 Quem Somos"): st.session_state['pagina'] = "Sobre"; st.rerun()
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("🚪 SAIR"): st.session_state['autenticado'] = False; st.rerun()

    # --- NAVEGAÇÃO ENTRE SEÇÕES ---
    if st.session_state['pagina'] == "Início":
        st.markdown("<div class='content-card'><h1>Dashboard Principal</h1><p>Selecione uma operação no menu lateral para começar.</p></div>", unsafe_allow_html=True)

    elif st.session_state['pagina'] == "NCM":
        st.markdown("<div class='section-header'><h1>Consulta de Inteligência NCM</h1></div>", unsafe_allow_html=True)
        with st.container():
            st.markdown("<div class='content-card'>", unsafe_allow_html=True)
            busca = st.text_input("Pesquisar por Código ou Descrição do Item (Base de 15.160 itens)")
            st.button("Executar Busca Fiscal")
            st.info("Aguardando carregamento da base de dados Duty Clear...")
            st.markdown("</div>", unsafe_allow_html=True)

    elif st.session_state['pagina'] == "Mapas":
        st.markdown("<div class='section-header'><h1>Otimização de Rotas</h1></div>", unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("<div class='content-card'><h3>Origem / Destino</h3>", unsafe_allow_html=True)
            st.text_input("Cidade de Origem")
            st.text_input("Cidade de Destino")
            st.markdown("</div>", unsafe_allow_html=True)
        with col_b:
            st.markdown("<div class='content-card'><h3>Parâmetros</h3>", unsafe_allow_html=True)
            st.selectbox("Tipo de Veículo", ["Bitrem", "Vanderleia", "Truck", "Toco"])
            st.markdown("</div>", unsafe_allow_html=True)

    elif st.session_state['pagina'] == "Sobre":
        st.markdown("<div class='content-card'><h1>Quem Somos</h1><p>A UAU Logística nasceu para transformar o transporte rodoviário.</p></div>", unsafe_allow_html=True)
