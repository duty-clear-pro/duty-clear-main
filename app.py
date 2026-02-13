import streamlit as st

# 1. Configuração de Página - TRADEMIND GLOBAL
st.set_page_config(page_title="TradeMind | Global Intelligence", layout="wide")

# 2. CSS - Design Profissional de Alto Impacto
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    
    /* Sidebar Dark */
    [data-testid="stSidebar"] { background-color: #020617 !important; border-right: 1px solid #1E293B; }
    
    /* Banner de Boas-Vindas Recheado */
    .hero-banner {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 50px; border-radius: 24px; color: white;
        margin-bottom: 30px; border-left: 10px solid #38BDF8;
        box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1);
    }
    
    /* Cards de Informação */
    .info-card {
        background: white; padding: 30px; border-radius: 16px;
        border: 1px solid #E2E8F0; height: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .info-card h3 { color: #0F172A; font-weight: 700; margin-bottom: 15px; }
    .info-card p { color: #475569; line-height: 1.6; font-size: 15px; }

    /* Indicadores de Mercado */
    .market-stat {
        background: #FFFFFF; padding: 20px; border-radius: 12px;
        text-align: center; border: 1px solid #E2E8F0;
    }
    .market-stat h4 { color: #64748B; font-size: 12px; margin: 0; text-transform: uppercase; }
    .market-stat h2 { color: #0F172A; margin: 5px 0; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

# Inicialização de Sessão
if 'auth' not in st.session_state: st.session_state.auth = False
if 'aba' not in st.session_state: st.session_state.aba = "Home"

if not st.session_state.auth:
    # --- TELA DE LOGIN ---
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.markdown("<div style='text-align:center;'><h1>TRADEMIND</h1><p style='color:#64748B;'>Intelligence for Global Trade</p></div>", unsafe_allow_html=True)
        u = st.text_input("Usuario Master")
        p = st.text_input("Chave de Acesso", type="password")
        if st.button("ACESSAR TERMINAL", use_container_width=True):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Credenciais Inválidas")
else:
    # --- MENU LATERAL ---
    with st.sidebar:
        st.markdown("<div style='padding:20px; text-align:center;'><h2 style='color:white;'>TRADEMIND</h2></div>", unsafe_allow_html=True)
        if st.button("Terminal Principal", use_container_width=True): st.session_state.aba = "Home"; st.rerun()
        if st.button("Consultar NCM", use_container_width=True): st.session_state.aba = "NCM"; st.rerun()
        if st.button("Histórico Ativo", use_container_width=True): st.session_state.aba = "History"; st.rerun()
        st.markdown("<br><br>")
        if st.button("SAIR", use_container_width=True): st.session_state.auth = False; st.rerun()

    # --- HOME (BOAS-VINDAS E EXPLICAÇÃO) ---
    if st.session_state.aba == "Home":
        st.markdown("""
            <div class='hero-banner'>
                <h1 style='font-size: 42px; margin-bottom: 10px;'>Bem-vindo ao TradeMind, Igor.</h1>
                <p style='font-size: 20px; opacity: 0.9;'>A inteligência estratégica que antecede a sua operação aduaneira.</p>
                <hr style='opacity: 0.2; margin: 25px 0;'>
                <p style='max-width: 850px; line-height: 1.6;'>
                    Diferente de sistemas de gestão comuns, o <b>TradeMind</b> atua na fase de decisão. 
                    Nossa plataforma analisa a viabilidade tributária e os riscos regulatórios 
                    antes mesmo da emissão de documentos, garantindo blindagem fiscal e previsibilidade de custos.
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Indicadores de Mercado
        st.markdown("### Monitor Global")
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown("<div class='market-stat'><h4>Dólar (USD)</h4><h2>R$ 5,12</h2></div>", unsafe_allow_html=True)
        with c2: st.markdown("<div class='market-stat'><h4>Euro (EUR)</h4><h2>R$ 5,48</h2></div>", unsafe_allow_html=True)
        with c3: st.markdown("<div class='market-stat'><h4>Base NCM</h4><h2>15.160</h2></div>", unsafe_allow_html=True)
        with c4: st.markdown("<div class='market-stat'><h4>Compliance</h4><h2>Ativo</h2></div>", unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)

        # O que temos no sistema
        st.markdown("### Módulos TradeMind")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.markdown("<div class='info-card'><h3>Classificação NCM</h3><p>Busca inteligente com detalhamento de alíquotas (II, IPI, PIS, COFINS) e exigências de órgãos anuentes.</p></div>", unsafe_allow_html=True)
        with col_b:
            st.markdown("<div class='info-card'><h3>Simulador de Custo</h3><p>Cálculo de nacionalização 'Land Cost' para entender a margem de lucro real da mercadoria posta no Brasil.</p></div>", unsafe_allow_html=True)
        with col_c:
            st.markdown("<div class='info-card'><h3>Radar de Histórico</h3><p>Monitoramento proativo: o sistema salva suas buscas e alerta sobre mudanças súbitas na legislação tributária.</p></div>", unsafe_allow_html=True)

    # --- PÁGINA NCM ---
    elif st.session_state.aba == "NCM":
        st.markdown("<h1>Inteligência NCM</h1>", unsafe_allow_html=True)
        st.text_input("Insira o NCM ou Descrição Técnica para Análise")

    # --- PÁGINA HISTÓRICO ---
    elif st.session_state.aba == "History":
        st.markdown("<h1>Histórico Estratégico</h1>", unsafe_allow_html=True)
        st.info("Suas consultas recentes aparecerão aqui para monitoramento de taxas.")
