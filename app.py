import streamlit as st
import pandas as pd

# 1. Configuração de Sistema
st.set_page_config(page_title="TradeMind | Intelligence", layout="wide")

# 2. CSS Profissional (Clean Corporate)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #FFFFFF; color: #1E293B; }
    
    /* Disclaimer Padrão em todas as telas */
    .disclaimer-box {
        font-size: 11px; color: #64748B; text-align: justify;
        padding: 20px; border-top: 1px solid #E2E8F0; margin-top: 50px;
        line-height: 1.5;
    }
    
    /* Marca D'Água no fundo da página */
    .watermark {
        position: fixed; bottom: 100px; right: 20px;
        font-size: 40px; color: rgba(0,0,0,0.03);
        transform: rotate(-15deg); font-weight: 800; pointer-events: none;
    }
    
    .stButton > button {
        background-color: #0F172A; color: white; border-radius: 4px;
        border: none; padding: 10px; font-weight: 600;
    }
    
    .card-report {
        border: 1px solid #E2E8F0; padding: 30px; border-radius: 8px;
        background: #F8FAFC;
    }
    </style>
    """, unsafe_allow_html=True)

# Função para o Disclaimer Obrigatório
def mostrar_disclaimer():
    st.markdown(f"""
        <div class="disclaimer-box">
            As informações disponibilizadas pela <b>TradeMind</b> possuem caráter exclusivamente informativo e de apoio à decisão. 
            Não substituem consultoria jurídica, contábil ou aduaneira. A responsabilidade pelo uso dos dados 
            e pelo cumprimento da legislação vigente é integralmente do usuário.
        </div>
    """, unsafe_allow_html=True)

# 3. Gerenciamento de Estado
if 'auth' not in st.session_state: st.session_state.auth = False
if 'aba' not in st.session_state: st.session_state.aba = "Dashboard"

# Marca d'água persistente
st.markdown("<div class='watermark'>TRADEMIND CONFIDENCIAL</div>", unsafe_allow_html=True)

if not st.session_state.auth:
    # TELA DE LOGIN CORPORATIVA
    _, col, _ = st.columns([1, 0.8, 1])
    with col:
        st.markdown("<br><br><h1 style='text-align:center;'>TRADEMIND</h1>", unsafe_allow_html=True)
        u = st.text_input("Usuário")
        p = st.text_input("Chave de Acesso", type="password")
        if st.button("AUTENTICAR", use_container_width=True):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True; st.rerun()
    mostrar_disclaimer()

else:
    # SIDEBAR UNIFICADA
    with st.sidebar:
        st.markdown("<h1>TRADEMIND</h1>", unsafe_allow_html=True)
        st.markdown("---")
        if st.button("Dashboard Estratégico"): st.session_state.aba = "Dashboard"; st.rerun()
        if st.button("Simulador de Tributos"): st.session_state.aba = "Simul"; st.rerun()
        if st.button("Quem Somos"): st.session_state.aba = "About"; st.rerun()
        st.markdown("<br><br>")
        if st.button("Sair"): st.session_state.auth = False; st.rerun()

    # CONTEÚDO
    if st.session_state.aba == "Dashboard":
        st.title("Painel de Controle")
        st.info("Sistema operando em modo de conformidade total.")
        # Simulação de dados
        c1, c2 = st.columns(2)
        c1.metric("Câmbio PTAX", "R$ 5,12")
        c2.metric("NCMs Mapeadas", "12.400")

    elif st.session_state.aba == "Simul":
        st.title("Simulador de Viabilidade")
        with st.container():
            fob = st.number_input("Valor FOB (USD)", min_value=0.0)
            taxa = st.number_input("Câmbio (R$)", value=5.12)
            
            if st.button("GERAR ANÁLISE"):
                cif = fob * taxa
                st.markdown(f"""
                    <div class="card-report">
                        <h3>RELATÓRIO DE CUSTOS REFERENCIAIS</h3>
                        <p>Base de Cálculo (BRL): R$ {cif:,.2f}</p>
                        <p><b>Atenção:</b> Sujeito a variações de alíquotas por NCM.</p>
                    </div>
                """, unsafe_allow_html=True)

    elif st.session_state.aba == "About":
        st.title("Quem Somos")
        st.write("A TradeMind é uma plataforma de inteligência aduaneira focada em prover dados estratégicos para o comércio exterior.")

    mostrar_disclaimer()
