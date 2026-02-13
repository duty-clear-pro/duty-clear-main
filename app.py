import streamlit as st

# 1. Configuração TradeMind
st.set_page_config(page_title="TradeMind | Global Intelligence", layout="wide")

# 2. CSS - Design de Terminal de Elite
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    
    /* Painel de Login (Lado Esquerdo - Quem Somos) */
    .about-section {
        background: linear-gradient(135deg, #020617 0%, #0F172A 100%);
        padding: 60px; border-radius: 24px 0 0 24px; color: white;
        height: 100%; min-height: 550px; border-right: 4px solid #38BDF8;
    }
    .about-section h1 { font-size: 45px; font-weight: 900; color: #38BDF8; margin-bottom: 20px; }
    .about-section p { font-size: 18px; line-height: 1.6; opacity: 0.9; }
    .bullet { margin-bottom: 15px; display: flex; align-items: center; gap: 10px; font-weight: 600; }
    
    /* Painel de Login (Lado Direito - Form) */
    .login-section {
        background: white; padding: 60px; border-radius: 0 24px 24px 0;
        height: 100%; min-height: 550px; display: flex; flex-direction: column; justify-content: center;
        box-shadow: 20px 20px 60px rgba(0,0,0,0.05);
    }

    /* Banner Interno (Pós-Login) */
    .hero-banner {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 40px; border-radius: 20px; color: white; border-left: 10px solid #38BDF8;
    }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    # --- TELA DE ACESSO COM "QUEM SOMOS" ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_info, col_login = st.columns([1.5, 1], gap="small")

    with col_info:
        st.markdown("""
            <div class='about-section'>
                <h1>TRADEMIND</h1>
                <p><b>A Inteligência que antecede o movimento.</b></p>
                <p>Diferente de sistemas de gestão (ERP) que apenas registram o passado, o TradeMind é o cérebro estratégico que analisa a viabilidade da sua operação internacional <b>antes</b> dela acontecer.</p>
                <br>
                <div class='bullet'>✅ Blindagem Fiscal (NCM Intelligence)</div>
                <div class='bullet'>✅ Simulação de Land Cost (Custo Real)</div>
                <div class='bullet'>✅ Radar de Riscos Regulatórios</div>
                <div class='bullet'>✅ Monitoramento de Alíquotas em Tempo Real</div>
                <br>
                <p style='font-size: 14px; color: #94A3B8;'>Utilizado por importadores e exportadores de alta performance para garantir previsibilidade e lucro no mercado global.</p>
            </div>
        """, unsafe_allow_html=True)

    with col_login:
        st.markdown("<div class='login-section'>", unsafe_allow_html=True)
        st.subheader("Acesse o Terminal")
        u = st.text_input("Usuário Master", placeholder="Ex: admin")
        p = st.text_input("Chave de Acesso", type="password", placeholder="••••••••")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("AUTENTICAR SISTEMA", use_container_width=True):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Acesso Negado")
        st.markdown("</div>", unsafe_allow_html=True)

else:
    # --- ÁREA LOGADA (AQUI ESTÁ TUDO PERFEITO) ---
    with st.sidebar:
        st.markdown("<h2 style='color:white; text-align:center;'>TRADEMIND</h2>", unsafe_allow_html=True)
        if st.button("Sair"): st.session_state.auth = False; st.rerun()

    st.markdown("""
        <div class='hero-banner'>
            <h1>Painel de Controle TradeMind</h1>
            <p>Sua inteligência global está ativa e monitorada.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Cards de Mercado rápidos para não ficar vazio
    c1, c2, c3 = st.columns(3)
    with c1: st.metric("Dólar", "R$ 5,12", "+0.12%")
    with c2: st.metric("Euro", "R$ 5,48", "-0.05%")
    with c3: st.metric("Base NCM", "15.160", "Atualizada")
    
    st.info("Selecione um módulo no menu lateral para iniciar sua análise estratégica.")
