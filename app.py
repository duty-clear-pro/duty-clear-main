import streamlit as st
import pandas as pd

# 1. Configurações e Branding
st.set_page_config(page_title="UAU Logística", page_icon="⚖️", layout="wide")
logo_url = "https://cdn-icons-png.flaticon.com/512/4370/4370714.png"

# 2. Estilo Visual Organizado
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 5px 5px 0px 0px;
        gap: 1px;
        padding-left: 20px;
        padding-right: 20px;
    }
    .stTabs [aria-selected="true"] { background-color: #1A2B48 !important; color: white !important; }
    .title-uau { color: #1A2B48; font-weight: 900; margin-bottom: 0px; }
    .footer { font-size: 12px; color: #666; text-align: center; margin-top: 50px; border-top: 1px solid #eee; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Trava de Segurança
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    # Tela de Login (A mesma que você aprovou)
    col1, _, col2 = st.columns([1.2, 0.2, 1])
    with col1:
        st.image(logo_url, width=70)
        st.markdown("<h1 class='title-uau'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
        st.info("Sistema de Inteligência Operacional e Tributária.")
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        with st.form("login"):
            u = st.text_input("Usuário")
            p = st.text_input("Senha", type="password")
            if st.form_submit_button("ACESSAR"):
                if u == "gestor.vip" and p == "UAU2026":
                    st.session_state['autenticado'] = True
                    st.rerun()
else:
    # --- DASHBOARD ORGANIZADO POR SEÇÕES ---
    st.image(logo_url, width=60)
    st.markdown("<h1 class='title-uau'>Painel de Controle</h1>", unsafe_allow_html=True)
    st.write("---")

    # CRIAÇÃO DAS SEÇÕES (TABS)
    aba_ncm, aba_logistica, aba_frete = st.tabs(["🔍 CONSULTA NCM", "📦 LOGÍSTICA", "💰 CÁLCULO DE FRETE"])

    # --- SEÇÃO 1: NCM ---
    with aba_ncm:
        st.subheader("Base de Inteligência Tributária")
        st.write("Consulte alíquotas e classificações fiscais.")
        busca_ncm = st.text_input("Digite o código NCM ou nome do produto", placeholder="Ex: 1201.90.00")
        
        # Simulação de tabela (Aqui entra sua planilha depois)
        st.info("Resultado da consulta aparecerá abaixo conforme a base de dados.")
        st.dataframe(pd.DataFrame({'NCM': ['1201.90.00'], 'Produto': ['Soja'], 'IPI': ['0%'], 'ICMS': ['12%']}))

    # --- SEÇÃO 2: LOGÍSTICA ---
    with aba_logistica:
        st.subheader("Planejamento de Carga")
        col_a, col_b = st.columns(2)
        with col_a:
            st.selectbox("Tipo de Veículo", ["Bitrem", "Rodotrem", "Vanderleia", "Truck"])
            st.text_input("Local de Origem")
        with col_b:
            st.number_input("Peso Total (Toneladas)", min_value=0.0)
            st.text_input("Destino Final")
        st.button("Salvar Planejamento")

    # --- SEÇÃO 3: FRETE ---
    with aba_frete:
        st.subheader("Simulador de Margem Líquida")
        with st.container(border=True):
            v_carga = st.number_input("Valor da Carga (R$)", key="frete_carga")
            v_frete = st.number_input("Custo do Frete (R$)", key="frete_valor")
            
            if st.button("CALCULAR AGORA"):
                lucro = v_carga - v_frete - (v_carga * 0.12)
                st.metric("Lucro Líquido Estimado", f"R$ {lucro:,.2f}", delta=f"{(lucro/v_carga)*100:.1f}% de Margem")
                st.progress(max(0, min(int((lucro/v_carga)*100), 100)) if v_carga > 0 else 0)

    # Rodapé de Proteção
    st.markdown("""
        <div class='footer'>
            <b>UAU LOGÍSTICA</b> - Sistema de Apoio à Decisão.<br>
            <i>Aviso: Dados referenciais. A decisão final é de responsabilidade do gestor.</i>
        </div>
        """, unsafe_allow_html=True)

    if st.sidebar.button("Sair"):
        st.session_state['autenticado'] = False
        st.rerun()
