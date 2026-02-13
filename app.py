import streamlit as st

# 1. Configuração do Terminal
st.set_page_config(page_title="TradeMind | Intelligence", layout="wide")

# 2. CSS - Design de Elite e Rodapé Legal
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    [data-testid="stSidebar"] { background-color: #020617 !important; }
    
    .hero-banner {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 40px; border-radius: 20px; color: white; border-left: 10px solid #38BDF8;
    }
    .stat-card {
        background: white; padding: 20px; border-radius: 15px;
        border: 1px solid #E2E8F0; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .legal-footer {
        font-size: 11px; color: #94A3B8; text-align: center;
        padding: 20px; border-top: 1px solid #E2E8F0; margin-top: 50px;
    }
    .about-card {
        background: white; padding: 30px; border-radius: 20px;
        border-top: 4px solid #38BDF8; margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Estado da Sessão
if 'auth' not in st.session_state: st.session_state.auth = False
if 'aba' not in st.session_state: st.session_state.aba = "Home"
if 'chat_history' not in st.session_state: st.session_state.chat_history = []

# --- TELA DE ACESSO ---
if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    _, col_form, _ = st.columns([1, 1, 1])
    with col_form:
        st.markdown("<h1 style='text-align:center;'>TRADEMIND</h1>", unsafe_allow_html=True)
        u = st.text_input("Usuário Master")
        p = st.text_input("Chave de Acesso", type="password")
        if st.button("AUTENTICAR", use_container_width=True):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Credenciais incorretas.")

# --- TELA INTERNA ---
else:
    with st.sidebar:
        st.markdown("<h2 style='color:white; text-align:center;'>TRADEMIND</h2>", unsafe_allow_html=True)
        if st.button("🏠 Home Dashboard", use_container_width=True): st.session_state.aba = "Home"; st.rerun()
        if st.button("📖 Quem Somos", use_container_width=True): st.session_state.aba = "About"; st.rerun()
        if st.button("🔍 Inteligência NCM", use_container_width=True): st.session_state.aba = "NCM"; st.rerun()
        if st.button("🤖 Assistente IA", use_container_width=True): st.session_state.aba = "AI"; st.rerun()
        st.markdown("<br><br>")
        if st.button("🚪 Sair", use_container_width=True): st.session_state.auth = False; st.rerun()

    # ABAS
    if st.session_state.aba == "Home":
        st.markdown("<div class='hero-banner'><h1>Terminal de Inteligência Ativo</h1><p>Bem-vindo, Igor. O mercado global está sob seu comando.</p></div>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown("<div class='stat-card'><h4>USD/BRL</h4><h2>R$ 5,12</h2></div>", unsafe_allow_html=True)
        with c2: st.markdown("<div class='stat-card'><h4>EUR/BRL</h4><h2>R$ 5,48</h2></div>", unsafe_allow_html=True)
        with c3: st.markdown("<div class='stat-card'><h4>Status Base</h4><h2>Compliance OK</h2></div>", unsafe_allow_html=True)

    elif st.session_state.aba == "About":
        st.markdown("<h1>📖 Quem Somos</h1>", unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
                <div class='about-card'>
                    <h3>O que é o TradeMind?</h3>
                    <p>O <b>TradeMind</b> é o cérebro estratégico do Comércio Exterior. Diferente de um ERP comum, nós operamos na fase de <b>pré-embarque</b>.</p>
                    <p>Nossa missão é fornecer previsibilidade financeira e segurança jurídica para importadores e exportadores.</p>
                </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
                <div class='about-card'>
                    <h3>Trabalho Baseado em Dados</h3>
                    <p>Trabalhamos exclusivamente com <b>valores baseados em médias de mercado e legislações vigentes</b>.</p>
                    <p>O TradeMind utiliza algoritmos avançados para sugerir o caminho mais eficiente, servindo como uma poderosa ferramenta de apoio à decisão.</p>
                </div>
            """, unsafe_allow_html=True)
        st.warning("**Aviso de Isenção:** Todas as informações são referenciais. A decisão final e a responsabilidade jurídica pelas declarações aduaneiras permanecem com o usuário.")

    elif st.session_state.aba == "AI":
        st.header("🤖 Consultor AI")
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])
        if prompt := st.chat_input("Pergunte algo..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            resp = f"Analisando '{prompt}' com base em referências históricas... Recomendamos validar com a Receita Federal."
            st.session_state.chat_history.append({"role": "assistant", "content": resp})
            with st.chat_message("assistant"): st.markdown(resp)

    elif st.session_state.aba == "NCM":
        st.header("🔍 Consulta NCM")
        st.text_input("Código ou descrição...")

    # RODAPÉ DE BLINDAGEM JURÍDICA
    st.markdown("""
        <div class='legal-footer'>
            <b>AVISO LEGAL:</b> O TradeMind fornece informações baseadas em dados históricos e modelos estatísticos. 
            Não garantimos a imutabilidade de taxas ou aceitação governamental. O uso destes dados é meramente referencial 
            e de inteira responsabilidade do operador.
        </div>
    """, unsafe_allow_html=True)
