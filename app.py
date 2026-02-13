import streamlit as st

# 1. Configuracao de Pagina - TRADEMIND
st.set_page_config(page_title="TradeMind | Global Intelligence", layout="wide")

# 2. CSS - Design Corporativo de Alta Performance
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    
    /* Sidebar Profissional */
    [data-testid="stSidebar"] { background-color: #020617 !important; border-right: 1px solid #1E293B; }
    
    /* Banner de Boas-Vindas */
    .welcome-banner {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 40px; border-radius: 20px; color: white;
        margin-bottom: 30px; border-left: 8px solid #38BDF8;
    }

    /* Cards de Dados */
    .data-card {
        background: white; padding: 25px; border-radius: 16px;
        border: 1px solid #E2E8F0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }
    .data-card h3 { color: #64748B; font-size: 14px; margin-bottom: 10px; text-transform: uppercase; }
    .data-card h1 { color: #0F172A; margin: 0; font-size: 28px; font-weight: 700; }

    /* Estilo de Inputs */
    .stTextInput input {
        border: 2px solid #0F172A !important; border-radius: 10px !important;
        height: 50px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Sessão
if 'auth' not in st.session_state: st.session_state.auth = False
if 'aba' not in st.session_state: st.session_state.aba = "Home"

if not st.session_state.auth:
    # --- TELA DE LOGIN ---
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.markdown("<div style='text-align:center;'><h1>TRADEMIND</h1><p style='color:#64748B;'>Intelligence for Global Trade</p></div>", unsafe_allow_html=True)
        u = st.text_input("Identificação")
        p = st.text_input("Senha", type="password")
        if st.button("ACESSAR TERMINAL", use_container_width=True):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True
                st.rerun()
else:
    # --- SIDEBAR ---
    with st.sidebar:
        st.markdown("<div style='padding:20px; text-align:center;'><h2 style='color:white;'>TRADEMIND</h2></div>", unsafe_allow_html=True)
        if st.button("Terminal de Inteligência", use_container_width=True): st.session_state.aba = "Home"; st.rerun()
        if st.button("Classificação NCM", use_container_width=True): st.session_state.aba = "NCM"; st.rerun()
        if st.button("Histórico de Consultas", use_container_width=True): st.session_state.aba = "History"; st.rerun()
        if st.button("TradeMind AI Chat", use_container_width=True): st.session_state.aba = "AI"; st.rerun()
        st.markdown("<br><br>")
        if st.button("Encerrar Sessão", use_container_width=True): st.session_state.auth = False; st.rerun()

    # --- HOME RECHEADA (BOAS-VINDAS) ---
    if st.session_state.aba == "Home":
        st.markdown(f"""
            <div class='welcome-banner'>
                <h1 style='margin:0;'>Bem-vindo ao TradeMind, Igor!</h1>
                <p style='font-size:18px; opacity:0.8;'>Seu status de conta: <b>Global Intelligence Premium</b></p>
            </div>
        """, unsafe_allow_html=True)

        # Seção de Mercado em Tempo Real
        st.markdown("### Panorama do Mercado Global")
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown("<div class='data-card'><h3>Dólar Comercial</h3><h1>R$ 5,12</h1><p style='color:green; font-size:12px;'>+0.12%</p></div>", unsafe_allow_html=True)
        with c2: st.markdown("<div class='data-card'><h3>Euro</h3><h1>R$ 5,48</h1><p style='color:red; font-size:12px;'>-0.05%</p></div>", unsafe_allow_html=True)
        with c3: st.markdown("<div class='data-card'><h3>Base NCM</h3><h1>15.160</h1><p style='color:blue; font-size:12px;'>Atualizada hoje</p></div>", unsafe_allow_html=True)
        with c4: st.markdown("<div class='data-card'><h3>Consultas Mês</h3><h1>342</h1><p style='color:blue; font-size:12px;'>Sua atividade</p></div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Colunas Inferiores para Preencher Espaço
        col_left, col_right = st.columns([2, 1])
        
        with col_left:
            st.
