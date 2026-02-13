import streamlit as st

# 1. Configuração do Terminal TradeMind
st.set_page_config(page_title="TradeMind | Intelligence", layout="wide")

# 2. CSS - Estética de Terminal Profissional
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    
    /* Login Page Design */
    .about-box {
        background: linear-gradient(135deg, #020617 0%, #0F172A 100%);
        padding: 40px; border-radius: 20px; color: white; border-right: 5px solid #38BDF8;
    }
    .art-frame {
        background: #FFFFFF; border-radius: 20px; height: 300px;
        display: flex; align-items: center; justify-content: center;
        border: 2px dashed #E2E8F0; color: #94A3B8; margin-bottom: 20px;
    }

    /* Dashboard Design (Parte de Dentro) */
    .hero-card {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 40px; border-radius: 20px; color: white; margin-bottom: 20px;
    }
    .stat-card {
        background: white; padding: 20px; border-radius: 15px;
        border: 1px solid #E2E8F0; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Navegação
if 'auth' not in st.session_state: st.session_state.auth = False
if 'aba' not in st.session_state: st.session_state.aba = "Home"

if not st.session_state.auth:
    # --- TELA DE LOGIN COM QUEM SOMOS ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_txt, col_form = st.columns([1.2, 1], gap="large")
    
    with col_txt:
        st.markdown("""
            <div class='about-box'>
                <h1 style='color:#38BDF8;'>TRADEMIND</h1>
                <p style='font-size:20px;'><b>A Inteligência que antecede o movimento.</b></p>
                <p>O TradeMind analisa a viabilidade da sua operação internacional <b>antes</b> dela acontecer, garantindo lucro e blindagem fiscal.</p>
                <br>
                <p>✅ Blindagem Fiscal (NCM Intelligence)</p>
                <p>✅ Simulação de Land Cost (Custo Real)</p>
                <p>✅ Radar de Riscos Regulatórios</p>
            </div>
        """, unsafe_allow_html=True)

    with col_form:
        st.markdown("<div class='art-frame'>ESPAÇO PARA ARTE TRADEMIND</div>", unsafe_allow_html=True)
        u = st.text_input("Usuário Master")
        p = st.text_input("Chave de Acesso", type="password")
        if st.button("AUTENTICAR SISTEMA", use_container_width=True):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True
                st.rerun()
else:
    # --- PARTE DE DENTRO (RECHEADA) ---
    with st.sidebar:
        st.markdown("<h2 style='text-align:center;'>TRADEMIND</h2>", unsafe_allow_html=True)
        if st.button("Painel Principal", use_container_width=True): st.session_state.aba = "Home"; st.rerun()
        if st.button("Consultar NCM", use_container_width=True): st.session_state.aba = "NCM"; st.rerun()
        st.markdown("<br><br>")
        if st.button("Sair", use_container_width=True): st.session_state.auth = False; st.rerun()

    if st.session_state.aba == "Home":
        st.markdown("""
            <div class='hero-card'>
                <h1>Bem-vindo ao Centro de Inteligência, Igor.</h1>
                <p>Seu terminal estratégico está ativo. Monitore o mercado e simule operações abaixo.</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Cards para preencher a tela
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown("<div class='stat-card'><h4>Dólar</h4><h2>R$ 5,12</h2></div>", unsafe_allow_html=True)
        with c2: st.markdown("<div class='stat-card'><h4>Euro</h4><h2>R$ 5,48</h2></div>", unsafe_allow_html=True)
        with c3: st.markdown("<div class='stat-card'><h4>Base NCM</h4><h2>15.160</h2></div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("Utilize o menu lateral para acessar a ferramenta de Classificação NCM e análise de impostos.")

    elif st.session_state.aba == "NCM":
        st.header("Classificação NCM Inteligente")
        st.text_input("Descreva o produto ou insira o código NCM...")
