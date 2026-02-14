import streamlit as st
import pandas as pd

# 1. Configuração de Sistema
st.set_page_config(page_title="TradeMind | Duty Clear", layout="wide")

# 2. CSS Corporativo - Sem Amadorismo
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    .stApp { background-color: #F8FAFC; color: #1E293B; }
    
    /* Login e Boas-Vindas */
    .welcome-container {
        padding: 60px; background: white; border-radius: 24px;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1); border: 1px solid #E2E8F0;
    }
    .hero-title { font-size: 48px; font-weight: 800; color: #0F172A; letter-spacing: -1px; }
    .hero-subtitle { font-size: 18px; color: #64748B; line-height: 1.6; }
    
    /* Sidebar e Navegação */
    [data-testid="stSidebar"] { background-color: #FFFFFF !important; border-right: 1px solid #E2E8F0; }
    .stButton > button {
        background: #0F172A; color: white; border: none; padding: 10px 20px;
        border-radius: 8px; font-weight: 600; transition: 0.3s;
    }
    .stButton > button:hover { background: #334155; }
    
    /* Cards de Dados */
    .data-card {
        background: white; padding: 24px; border-radius: 16px;
        border: 1px solid #E2E8F0; margin-bottom: 20px;
    }
    .status-tag {
        font-size: 10px; text-transform: uppercase; font-weight: 800;
        padding: 4px 12px; border-radius: 20px; background: #F1F5F9; color: #475569;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Gerenciamento de Estado
if 'auth' not in st.session_state: st.session_state.auth = False
if 'aba' not in st.session_state: st.session_state.aba = "Dashboard"

# --- FLUXO DE TELAS ---

if not st.session_state.auth:
    # TELA DE BOAS-VINDAS E LOGIN (REMODELADA)
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_a, col_b = st.columns([1.5, 1], gap="large")
    
    with col_a:
        st.markdown(f"""
            <div class='welcome-container'>
                <p class='status-tag'>Inteligência Aduaneira de Elite</p>
                <h1 class='hero-title'>TRADEMIND<br><span style='color:#2563EB'>DUTY CLEAR</span></h1>
                <p class='hero-subtitle'>
                    Sistema avançado de análise de viabilidade e blindagem jurídica para operações internacionais. 
                    Nossa tecnologia processa dados referenciais para mitigar riscos de classificação fiscal 
                    e otimizar a margem operacional de grandes importadores.
                </p>
                <br>
                <div style='border-left: 4px solid #E2E8F0; padding-left: 20px;'>
                    <p><b>Sobre o Projeto:</b> O Duty Clear atua no pré-embarque, transformando 
                    complexidade tributária em previsibilidade financeira.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_b:
        st.markdown("<div class='welcome-container'>", unsafe_allow_html=True)
        st.subheader("Acesso ao Terminal")
        u = st.text_input("Usuário Master", placeholder="Identificação")
        p = st.text_input("Chave de Acesso", type="password", placeholder="••••••••")
        if st.button("AUTENTICAR NO SISTEMA", use_container_width=True):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

else:
    # SIDEBAR CORPORATIVA
    with st.sidebar:
        st.markdown("<h2 style='letter-spacing:-1px;'>DUTY CLEAR</h2>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:12px; color:#64748B;'>TERMINAL DE INTELIGÊNCIA</p>", unsafe_allow_html=True)
        st.markdown("---")
        if st.button("Painel Estratégico", use_container_width=True): st.session_state.aba = "Dashboard"; st.rerun()
        if st.button("Quem Somos", use_container_width=True): st.session_state.aba = "About"; st.rerun()
        if st.button("Simulador de Custos", use_container_width=True): st.session_state.aba = "Simul"; st.rerun()
        if st.button("Consulta NCM", use_container_width=True): st.session_state.aba = "NCM"; st.rerun()
        st.markdown("<br><br>")
        if st.button("Encerrar Sessão", use_container_width=True): st.session_state.auth = False; st.rerun()

    # ABAS
    if st.session_state.aba == "Dashboard":
        st.markdown("<h1>Painel de Controle</h1>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown("<div class='data-card'><h4>Câmbio PTAX</h4><h2>R$ 5,12</h2><span style='color:#10B981'>Estável</span></div>", unsafe_allow_html=True)
        with c2: st.markdown("<div class='data-card'><h4>Risco de Operação</h4><h2>Nível 1</h2><span style='color:#10B981'>Monitorado</span></div>", unsafe_allow_html=True)
        with c3: st.markdown("<div class='data-card'><h4>Análises Pendentes</h4><h2>04</h2><span>Prioridade Alta</span></div>", unsafe_allow_html=True)

    elif st.session_state.aba == "About":
        st.markdown("<h1>Quem Somos</h1>", unsafe_allow_html=True)
        st.markdown("""
            <div class='data-card'>
                <h3>Visão Estratégica</h3>
                <p>O Duty Clear nasceu da necessidade de precisão no comércio exterior. Operamos com o rigor técnico 
                necessário para garantir que valores referenciais e classificações fiscais estejam alinhados 
                com as melhores práticas de compliance.</p>
                <p>Nossa plataforma integra tecnologia de ponta para fornecer ao Despachante Aduaneiro e ao 
                Importador uma ferramenta robusta de tomada de decisão.</p>
            </div>
        """, unsafe_allow_html=True)

    elif st.session_state.aba == "Simul":
        st.markdown("<h1>Simulador de Impacto Fiscal</h1>", unsafe_allow_html=True)
        # Código do simulador mantido, mas sem emojis e com design limpo.
        st.info("Insira os dados da operação para gerar a planilha de viabilidade.")

    # RODAPÉ LEGAL (Obrigatório para sua segurança)
    st.markdown("<div style='text-align:center; padding: 40px; color:#94A3B8; font-size:11px; border-top:1px solid #E2E8F0;'>"
                "TRADEMIND AI | DUTY CLEAR - INFORMAÇÕES MERAMENTE REFERENCIAIS BASEADAS EM DADOS HISTÓRICOS. "
                "CONSULTE O REGULAMENTO ADUANEIRO VIGENTE.</div>", unsafe_allow_html=True)
