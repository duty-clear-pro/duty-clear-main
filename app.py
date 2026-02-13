import streamlit as st

# 1. Configuração TradeMind
st.set_page_config(page_title="TradeMind | Intelligence", layout="wide")

# 2. CSS - Estética e Rodapé Legal
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    
    /* Sidebar Dark */
    [data-testid="stSidebar"] { background-color: #020617 !important; }
    
    /* Banner e Cards */
    .hero-banner {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 40px; border-radius: 20px; color: white; margin-bottom: 20px;
        border-left: 10px solid #38BDF8;
    }
    .stat-card {
        background: white; padding: 20px; border-radius: 15px;
        border: 1px solid #E2E8F0; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    /* RODAPÉ LEGAL - BLINDAGEM JURÍDICA */
    .legal-footer {
        font-size: 11px; color: #94A3B8; text-align: center;
        padding: 20px; border-top: 1px solid #E2E8F0; margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Navegação
if 'auth' not in st.session_state: st.session_state.auth = False
if 'aba' not in st.session_state: st.session_state.aba = "Home"
if 'chat_history' not in st.session_state: st.session_state.chat_history = []

# --- TELA DE LOGIN ---
if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_txt, col_form = st.columns([1.3, 1], gap="large")
    with col_txt:
        st.markdown("<h1 style='color:#0F172A; font-size: 50px;'>TRADEMIND</h1>", unsafe_allow_html=True)
        st.markdown("### A inteligência que antecede o movimento.")
        st.write("Analise viabilidade e riscos antes da operação começar.")
    with col_form:
        u = st.text_input("Usuário Master")
        p = st.text_input("Chave de Acesso", type="password")
        if st.button("ENTRAR NO TERMINAL", use_container_width=True):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Credenciais incorretas.")

# --- TELA INTERNA ---
else:
    with st.sidebar:
        st.markdown("<h2 style='color:white; text-align:center;'>TRADEMIND</h2>", unsafe_allow_html=True)
        if st.button("🏠 Home / Dashboard", use_container_width=True): st.session_state.aba = "Home"; st.rerun()
        if st.button("📖 Quem Somos", use_container_width=True): st.session_state.aba = "About"; st.rerun()
        if st.button("🔍 Inteligência NCM", use_container_width=True): st.session_state.aba = "NCM"; st.rerun()
        if st.button("🤖 Assistente IA", use_container_width=True): st.session_state.aba = "AI"; st.rerun()
        st.markdown("<br><hr style='opacity:0.2;'><br>", unsafe_allow_html=True)
        if st.button("🚪 Sair", use_container_width=True): st.session_state.auth = False; st.rerun()

    # HOME
    if st.session_state.aba == "Home":
        st.markdown("<div class='hero-banner'><h1>Painel de Controle</h1><p>Monitoramento Global Ativo.</p></div>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown("<div class='stat-card'><h4>Dólar</h4><h2>R$ 5,12</h2></div>", unsafe_allow_html=True)
        with c2: st.markdown("<div class='stat-card'><h4>Euro</h4><h2>R$ 5,48</h2></div>", unsafe_allow_html=True)
        with c3: st.markdown("<div class='stat-card'><h4>Compliance</h4><h2>Auditado</h2></div>", unsafe_allow_html=True)

    # QUEM SOMOS + DISCLAIMER
    elif st.session_state.aba == "About":
        st.header("Sobre o TradeMind")
        st.info("**Nota de Isenção de Responsabilidade:** Os valores, alíquotas e cálculos apresentados são baseados em dados históricos e estimativas referenciais. O TradeMind não substitui a conferência aduaneira oficial nem o parecer de um despachante habilitado.")
        st.write("""
        O **TradeMind** é uma ferramenta de inteligência de dados. Trabalhamos com **valores baseados em médias de mercado e legislações vigentes**, servindo como um guia de viabilidade. 
        A responsabilidade final pela classificação e declaração de mercadorias é exclusiva do usuário/importador.
        """)

    # IA COM AVISO LEGAL
    elif st.session_state.aba == "AI":
        st.header("🤖 Assistente IA TradeMind")
        st.caption("⚠️ As respostas da IA são baseadas em modelos de linguagem e bases de dados estatísticas. Sempre valide as informações com a legislação oficial (Siscomex/TEC).")
        
        for msg in st.session_state.chat_history:
