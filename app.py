import streamlit as st

# 1. Configuracao de Pagina
st.set_page_config(page_title="UAU Logistica", layout="wide")

# 2. CSS Profissional - Estilo Cockpit Marinho
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F1F5F9; }
    
    /* Inputs com bordas pretas para maxima visao */
    .stTextInput input {
        border: 2px solid #0F172A !important;
        background-color: white !important;
        color: #0F172A !important;
        height: 45px !important;
    }

    /* Sidebar Marinho */
    [data-testid="stSidebar"] { background-color: #000B1D !important; }
    
    /* Banner Superior */
    .welcome-banner {
        background: #0F172A;
        padding: 40px;
        border-radius: 15px;
        color: white;
        margin-bottom: 25px;
        border-left: 10px solid #38BDF8;
    }
    
    /* Cards de Informacao */
    .info-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #E2E8F0;
        margin-bottom: 20px;
    }

    .vision-box {
        background: #F8FAFC;
        padding: 25px;
        border-radius: 10px;
        border-left: 5px solid #38BDF8;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Logica de Sessao
if 'autenticado' not in st.session_state: st.session_state['autenticado'] = False
if 'pagina' not in st.session_state: st.session_state['pagina'] = "Inicio"

if not st.session_state['autenticado']:
    # --- LOGIN ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, space, c2 = st.columns([1.5, 0.1, 1])
    with c1:
        st.markdown("<div style='background:#0F172A; padding:60px; border-radius:20px; color:white;'><h1>UAU LOGISTICA</h1><p style='color:#38BDF8; font-size:20px;'>Inovacao e Performance Operacional</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div style='background:white; padding:40px; border-radius:20px; border:1px solid #CBD5E1;'>", unsafe_allow_html=True)
        u = st.text_input("Identificacao do Gestor", key="u_login")
        p = st.text_input("Chave de Acesso", type="password", key="p_login")
        if st.button("ACESSAR COCKPIT", use_container_width=True):
            if u == "gestor.vip" and p == "UAU2026":
                st.session_state['autenticado'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
else:
    # --- MENU LATERAL (SEM EMOJIS) ---
    with st.sidebar:
        st.markdown("<div style='text-align:center; padding:20px;'><h2 style='color:white;'>UAU LOGISTICA</h2></div>", unsafe_allow_html=True)
        if st.button("Painel Principal", use_container_width=True): st.session_state['pagina'] = "Inicio"; st.rerun()
        if st.button("Logistica e Frota", use_container_width=True): st.session_state['pagina'] = "Logistica"; st.rerun()
        if st.button("Consulta NCM", use_container_width=True): st.session_state['pagina'] = "NCM"; st.rerun()
        if st.button("Quem Somos", use_container_width=True): st.session_state['pagina'] = "Sobre"; st.rerun()
        st.markdown("<br><br>")
        if st.button("SAIR", use_container_width=True): st.session_state['autenticado'] = False; st.rerun()

    # --- PAGINA INICIAL ---
    if st.session_state['pagina'] == "Inicio":
        st.markdown("""
            <div class='welcome-banner'>
                <h1 style='margin:0;'>Bem-vindo ao Cockpit, Igor!</h1>
                <p style='font-size:18px; opacity:0.8;'>Sistema Duty Clear operando em modo de Maxima Performance.</p>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1: st.info("Base NCM: 15.160 itens ativos")
        with col2: st.success("Servidor: Online e Seguro")
        with col3: st.warning("Monitoramento: Ativo 24h")

    # --- QUEM SOMOS (CORRIGIDO) ---
    elif st.session_state['pagina'] == "Sobre":
        st.markdown("<h1 style='color:#0F172A;'>Quem Somos</h1>", unsafe_allow_html=True)
        
        st.markdown("""
            <div class='info-card'>
                <h3 style='color:#0F172A;'>UAU Logistica - Inovacao a Servico da Logistica</h3>
                <p style='font-size:17px; color:#475569;'>
                    A UAU Logistica nasceu para resolver um dos maiores desafios do transporte rodoviario: 
                    transformar informacoes fiscais e operacionais em decisoes que geram lucro.
                </p>
                <p>Nossa plataforma auxilia transportadores e gestores a:</p>
                <ul style='line-height:1.8; color:#475569;'>
                    <li>Garantir conformidade fiscal nas operacoes</li>
                    <li>Reduzir riscos de autuacoes</li>
                    <li>Otimizar rotas com foco em rentabilidade</li>
                    <li>Tomar decisoes baseadas em dados reais</li>
                </ul>
                <p><b>Mais do que um sistema, somos um apoio estrategico para quem vive da logistica no Brasil.</b></p>
            </div>
            
            <div class='vision-box'>
                <h3 style='color:#38BDF8; margin-top:0;'>Nossa Visao</h3>
                <p style='font-size:18px; color:#0F172A;'>
                    Ser referencia nacional como plataforma inteligente de apoio a decisao, ajudando operacoes logisticas 
                    a crescer com seguranca juridica e maxima eficiencia financeira.
                </p>
            </div>
        """, unsafe_allow_html=True)

    # --- OUTRAS PAGINAS ---
    elif st.session_state['pagina'] == "Logistica":
        st.markdown("<h1>Logistica e Frota</h1>", unsafe_allow_html=True)
        st.write("Modulo de gestao de frota em operacao.")

    elif st.session_state['pagina'] == "NCM":
        st.markdown("<h1>Consulta NCM</h1>", unsafe_allow_html=True)
        st.write("Base de 15.160 itens disponivel para busca.")
