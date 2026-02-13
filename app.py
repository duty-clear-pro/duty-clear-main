import streamlit as st

# Configuração TradeMind
st.set_page_config(page_title="TradeMind | Global Intelligence", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    
    /* Painel Esquerdo - Inteligência */
    .about-section {
        background: linear-gradient(135deg, #020617 0%, #0F172A 100%);
        padding: 50px; border-radius: 24px; color: white;
        height: 100%; min-height: 600px;
    }
    .about-section h1 { font-size: 45px; font-weight: 900; color: #38BDF8; }
    
    /* Painel Direito - Arte e Login */
    .login-box {
        background: white; padding: 40px; border-radius: 24px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.05);
    }
    
    /* Quadrado da Arte (Onde vamos colocar sua imagem) */
    .art-placeholder {
        background: #F1F5F9; border-radius: 16px;
        height: 250px; display: flex; align-items: center; justify-content: center;
        margin-bottom: 30px; border: 2px dashed #CBD5E1;
        color: #64748B; font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_info, col_login = st.columns([1.2, 1], gap="large")

    with col_info:
        st.markdown("""
            <div class='about-section'>
                <h1>TRADEMIND</h1>
                <p style='font-size:18px;'><b>A Inteligência que antecede o movimento.</b></p>
                <p>O TradeMind é o cérebro estratégico que analisa a viabilidade da sua operação internacional antes dela acontecer.</p>
                <br>
                <div style='margin-bottom:10px;'>✅ <b>Blindagem Fiscal</b> (NCM Intelligence)</div>
                <div style='margin-bottom:10px;'>✅ <b>Simulação de Land Cost</b> (Custo Real)</div>
                <div style='margin-bottom:10px;'>✅ <b>Radar de Riscos Regulatórios</b></div>
                <div style='margin-bottom:10px;'>✅ <b>Monitoramento de Alíquotas</b></div>
            </div>
        """, unsafe_allow_html=True)

    with col_login:
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)
        
        # AQUI É O ESPAÇO DA SUA ARTE
        st.markdown("""
            <div class='art-placeholder'>
                ESPAÇO PARA ARTE TRADEMIND (IMAGEM/VÍDEO)
            </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Acesse o Terminal")
        u = st.text_input("Usuário Master", placeholder="admin")
        p = st.text_input("Chave de Acesso", type="password", placeholder="••••••••")
        
        if st.button("AUTENTICAR SISTEMA", use_container_width=True):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Credenciais Inválidas")
        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.sidebar.title("TRADEMIND")
    if st.sidebar.button("Logout"): st.session_state.auth = False; st.rerun()
    st.success("Acesso Garantido. Bem-vindo ao Centro de Inteligência.")
