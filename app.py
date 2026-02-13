import streamlit as st
import pandas as pd

# 1. Configurações de Interface
st.set_page_config(page_title="UAU Logística | Cockpit", layout="wide")
logo_url = "https://cdn-icons-png.flaticon.com/512/4370/4370714.png"

# 2. CSS Avançado (Hover, Cards e Sombras)
st.markdown("""
    <style>
    /* Estilo Geral */
    .stApp { background-color: #F4F7F9; }
    
    /* Header Profissional */
    .main-header {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 25px;
    }
    
    /* Cards de Indicadores */
    .kpi-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        border-bottom: 4px solid #B8964E;
        text-align: center;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.03);
    }
    
    /* Botões com Efeito Hover */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 60px;
        background-color: #ffffff;
        color: #1A2B48;
        border: 1px solid #e0e0e0;
        transition: all 0.3s ease;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #1A2B48;
        color: #ffffff;
        border: 1px solid #1A2B48;
        transform: translateY(-2px);
        box-shadow: 0px 5px 15px rgba(26, 43, 72, 0.2);
    }
    
    /* Sidebar Customizada */
    [data-testid="stSidebar"] { background-color: #1A2B48; color: white; }
    .sidebar-user { text-align: center; padding: 20px 0; border-bottom: 1px solid #2c3e50; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Lógica de Acesso
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False
if 'secao' not in st.session_state:
    st.session_state['secao'] = 'Dashboard'

# --- TELA DE LOGIN (Mantida conforme aprovado) ---
if not st.session_state['autenticado']:
    col_info, _, col_login = st.columns([1.3, 0.2, 1])
    with col_info:
        st.image(logo_url, width=90)
        st.markdown("<h1 style='color: #1A2B48; font-size: 52px; font-weight: 900;'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color: #B8964E; letter-spacing: 2px;'>DUTY CLEAR | INTELIGÊNCIA TRIBUTÁRIA</p>", unsafe_allow_html=True)
        st.markdown("<div style='background-color:#f8f9fa; padding:20px; border-left:6px solid #B8964E;'><b>Controle de Operações Externas</b><br>Acesso restrito para gestão de frotas e tributação NCM.</div>", unsafe_allow_html=True)
    with col_login:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        with st.form("login"):
            u = st.text_input("Usuário")
            p = st.text_input("Senha", type="password")
            if st.form_submit_button("ENTRAR NO SISTEMA"):
                if u == "gestor.vip" and p == "UAU2026":
                    st.session_state['autenticado'] = True
                    st.rerun()

else:
    # --- MENU LATERAL ROBUSTO ---
    with st.sidebar:
        st.markdown(f"""
            <div class='sidebar-user'>
                <img src='{logo_url}' width='60'><br>
                <b style='color:white;'>Gestor: Igor</b><br>
                <small style='color:#B8964E;'>Nível: Administrador</small>
            </div>
        """, unsafe_allow_html=True)
        
        st.session_state['secao'] = st.radio(
            "NAVEGAÇÃO PRINCIPAL",
            ["Dashboard", "Mapas e Rotas", "Consulta NCM", "Logística", "Financeiro", "Configurações"]
        )
        st.divider()
        if st.button("Encerrar Sessão"):
            st.session_state['autenticado'] = False
            st.rerun()

    # --- HEADER DE STATUS ---
    st.markdown(f"""
        <div class='main-header'>
            <div style='display:flex; align-items:center; gap:15px;'>
                <img src='{logo_url}' width='40'>
                <span style='font-size:20px; font-weight:bold; color:#1A2B48;'>UAU LOGÍSTICA - {st.session_state['secao'].upper()}</span>
            </div>
            <div style='color:#666; font-size:14px;'>
                Servidor: <b>Ativo</b> | Data: 13/02/2026
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- CONTEÚDO DINÂMICO ---
    
    if st.session_state['secao'] == "Dashboard":
        # KPIs - Preenchendo o espaço vazio com números
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown("<div class='kpi-card'><small>CONSULTAS NCM</small><h2>1,240</h2></div>", unsafe_allow_html=True)
        with c2: st.markdown("<div class='kpi-card'><small>ROTAS ATIVAS</small><h2>42</h2></div>", unsafe_allow_html=True)
        with c3: st.markdown("<div class='kpi-card'><small>MARGEM MÉDIA</small><h2>18.5%</h2></div>", unsafe_allow_html=True)
        with c4: st.markdown("<div class='kpi-card'><small>STATUS SERVER</small><h2 style='color:green;'>ON</h2></div>", unsafe_allow_html=True)
        
        st.write("<br>", unsafe_allow_html=True)
        
        # Área Central
        col_main, col_side = st.columns([2, 1])
        with col_main:
            with st.container(border=True):
                st.subheader("Atividades Recentes")
                st.info("Simulação de Frete: Catalão -> São Paulo (Margem 14%)")
                st.success("Consulta NCM: Milho em Grão (Alíquota 12%)")
                st.warning("Alerta: Reajuste de Frete sugerido para rota Sul.")
        with col_side:
            with st.container(border=True):
                st.subheader("Acesso Rápido")
                st.button("Gerar Relatório Diário")
                st.button("Ver Tabela de Impostos")

    elif st.session_state['secao'] == "Mapas e Rotas":
        st.subheader("Roteirização e Distâncias")
        with st.container(border=True):
            st.text_input("Origem")
            st.text_input("Destino")
            st.button("Calcular Rota via Google")

    elif st.session_state['secao'] == "Consulta NCM":
        st.subheader("Base de Inteligência NCM")
        st.text_input("Busca por produto ou código")
        st.button("Localizar Item")
