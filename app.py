import streamlit as st
import pandas as pd

# 1. Configurações de Alta Performance
st.set_page_config(page_title="UAU Logística", layout="wide")

# Link da Logo Profissional
logo_url = "https://cdn-icons-png.flaticon.com/512/4370/4370714.png" 

# 2. Estilização Executiva (Foco em Sobriedade)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .login-container {
        background-color: #1A2B48;
        padding: 45px;
        border-radius: 8px;
        color: white;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.1);
    }
    .feature-card {
        background-color: #fcfcfc;
        padding: 20px;
        border-radius: 4px;
        border-left: 6px solid #B8964E;
        margin-bottom: 20px;
        color: #1A2B48;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
    }
    .section-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 4px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
        border-top: 4px solid #1A2B48;
    }
    .title-main { color: #1A2B48; font-weight: 900; font-size: 52px; margin-bottom: 0px; letter-spacing: -1px; }
    .slogan-main { color: #B8964E; font-size: 18px; font-weight: 400; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 40px; }
    .sidebar-text { color: white !important; font-weight: 500; }
    </style>
    """, unsafe_allow_html=True)

# 3. Gerenciamento de Acesso
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    # --- TELA DE APRESENTAÇÃO PROFISSIONAL ---
    col_info, _, col_login = st.columns([1.3, 0.2, 1])
    
    with col_info:
        st.image(logo_url, width=90)
        st.markdown("<h1 class='title-main'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
        st.markdown("<p class='slogan-main'>Gestão de Inteligência e Performance</p>", unsafe_allow_html=True)
        
        st.markdown("### Soluções Corporativas")
        st.markdown("""
        <div class="feature-card">
            <b>Cálculo de Margem Líquida</b><br>
            Simulações financeiras precisas baseadas em custos operacionais e fretes.
        </div>
        <div class="feature-card">
            <b>Inteligência Fiscal NCM</b><br>
            Consulta centralizada à base de dados de classificação tributária.
        </div>
        <div class="feature-card">
            <b>Controle de Logística</b><br>
            Módulo dedicado ao planejamento de cargas e tipos de veículos.
        </div>
        """, unsafe_allow_html=True)

    with col_login:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.subheader("Acesso Restrito")
        st.write("Insira suas credenciais para acessar o servidor.")
        user = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        if st.button("AUTENTICAR SISTEMA"):
            if user == "gestor.vip" and password == "UAU2026":
                st.session_state['autenticado'] = True
                st.rerun()
            else:
                st.error("Falha na autenticação.")
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- INTERIOR DO APP: ORGANIZAÇÃO POR SEÇÕES ---
    st.sidebar.image(logo_url, width=70)
    st.sidebar.markdown("<h3 style='color: white;'>Painel de Controle</h3>", unsafe_allow_html=True)
    
    # Navegação por Seção (Sem Emojis)
    secao = st.sidebar.radio(
        "Navegação:",
        ["Consulta NCM", "Planejamento Logístico", "Calculadora Financeira", "Suporte Técnico"]
    )
    
    st.sidebar.divider()
    if st.sidebar.button("Encerrar Sessão"):
        st.session_state['autenticado'] = False
        st.rerun()

    # --- EXIBIÇÃO POR SEÇÃO ---
    if secao == "Consulta NCM":
        st.markdown("<h2 style='color: #1A2B48;'>Base de Dados Fiscal (NCM)</h2>", unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.write("Pesquisa avançada na base de 15.160 itens.")
            busca = st.text_input("Termo de busca (Produto ou Código)")
            st.button("Consultar")
            st.markdown('</div>', unsafe_allow_html=True)

    elif secao == "Planejamento Logístico":
        st.markdown("<h2 style='color: #1A2B48;'>Módulo de Operações Logísticas</h2>", unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            c1.selectbox("Modelo de Veículo", ["Bitrem", "Rodotrem", "Truck", "Carreta"])
            c2.number_input("Capacidade de Carga (Toneladas)", min_value=0.0)
            st.text_input("Ponto de Origem / Ponto de Destino")
            st.markdown('</div>', unsafe_allow_html=True)

    elif secao == "Calculadora Financeira":
        st.markdown("<h2 style='color: #1A2B48;'>Análise de Margem e Resultados</h2>", unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            v_carga = st.number_input("Valor da Nota Fiscal (R$)", min_value=0.0)
            v_frete = st.number_input("Custo de Frete Contratado (R$)", min_value=0.0)
            if st.button("GERAR RESULTADO FINANCEIRO"):
                # Cálculo referencial (12% imposto)
                lucro = v_carga - v_frete - (v_carga * 0.12)
                st.write("---")
                st.metric("Lucro Líquido", f"R$ {lucro:,.2f}")
            st.markdown('</div>', unsafe_allow_html=True)

    elif secao == "Suporte Técnico":
        st.markdown("<h2 style='color: #1A2B48;'>Documentação e Suporte</h2>", unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.write("Sistema UAU Logística v2.0")
            st.info("Aviso Legal: Os dados fornecidos são referenciais para auxílio à decisão.")
            st.write("Contato: suporte@uaulogistica.com")
            st.markdown('</div>', unsafe_allow_html=True)
