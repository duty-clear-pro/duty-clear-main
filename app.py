import streamlit as st
import pandas as pd

# 1. SETUP PREMIUM
st.set_page_config(page_title="TradeMind | Intelligence", layout="wide")

# 2. DESIGN LIGHT TECH (SISTEMA RICO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    .stApp { background-color: #F8FAFC; }
    
    /* Cards com Glassmorphism Light */
    .card-motor {
        background: white; padding: 25px; border-radius: 20px;
        border: 1px solid #E2E8F0; box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        margin-bottom: 20px;
    }
    .badge-dev {
        background: #FEF3C7; color: #92400E; padding: 4px 12px;
        border-radius: 10px; font-size: 10px; font-weight: bold;
    }
    .stButton > button {
        background: linear-gradient(90deg, #2563EB, #3B82F6);
        color: white; border-radius: 12px; border: none; font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. MOTOR DE DADOS (BASE REAL MOCK)
ncm_data = {
    "85171300": {"nome": "Smartphone", "ii": 11.2, "ipi": 15, "pis": 2.1, "cofins": 9.65},
    "84713012": {"nome": "Notebook", "ii": 0.0, "ipi": 0, "pis": 2.1, "cofins": 9.65},
    "87032310": {"nome": "Veículo > 1500cm³", "ii": 35.0, "ipi": 25, "pis": 2.1, "cofins": 9.65}
}

# 4. LÓGICA DE NAVEGAÇÃO
if 'auth' not in st.session_state: st.session_state.auth = False
if 'aba' not in st.session_state: st.session_state.aba = "Dashboard"

# --- TELA DE LOGIN ---
if not st.session_state.auth:
    _, col, _ = st.columns([1, 1, 1])
    with col:
        st.markdown("<div class='card-motor' style='text-align:center;'>", unsafe_allow_html=True)
        st.title("TRADEMIND")
        u = st.text_input("Usuário")
        p = st.text_input("Senha", type="password")
        if st.button("ACESSAR TERMINAL"):
            if u == "admin" and p == "trade2026":
                st.session_state.auth = True; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

else:
    # SIDEBAR CORPORATIVA
    with st.sidebar:
        st.markdown("<h2>Duty Clear</h2>", unsafe_allow_html=True)
        if st.button("📊 Painel Estratégico"): st.session_state.aba = "Dashboard"; st.rerun()
        if st.button("🔍 Inteligência NCM"): st.session_state.aba = "NCM"; st.rerun()
        if st.button("💰 Simulador de Custos"): st.session_state.aba = "Simul"; st.rerun()
        if st.button("🤖 IA Consultora"): st.session_state.aba = "IA"; st.rerun()
        st.markdown("---")
        if st.button("🚪 Sair"): st.session_state.auth = False; st.rerun()

    # --- ABA: DASHBOARD ---
    if st.session_state.aba == "Dashboard":
        st.markdown("<h1>Dashboard Executivo</h1>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown("<div class='card-motor'><h4>Score de Risco</h4><h2 style='color:#10B981;'>BAIXO</h2></div>", unsafe_allow_html=True)
        with c2: st.markdown("<div class='card-motor'><h4>NCMs Auditadas</h4><h2>15.162</h2></div>", unsafe_allow_html=True)
        with c3: st.markdown("<div class='card-motor'><h4>Economia Potencial</h4><h2 style='color:#2563EB;'>R$ 42.1k</h2></div>", unsafe_allow_html=True)

    # --- ABA: NCM ---
    elif st.session_state.aba == "NCM":
        st.markdown("<h1>Inteligência NCM <span class='badge-dev'>MOTOR ATIVO</span></h1>", unsafe_allow_html=True)
        codigo = st.text_input("Consulte uma NCM (8 dígitos)")
        if codigo in ncm_data:
            item = ncm_data[codigo]
            st.markdown(f"""
                <div class='card-motor'>
                    <h3>{item['nome']} (NCM {codigo})</h3>
                    <p><b>Alíquotas de Importação:</b></p>
                    <ul>
                        <li>II: {item['ii']}%</li>
                        <li>IPI: {item['ipi']}%</li>
                        <li>PIS/COFINS: {item['pis'] + item['cofins']}%</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        elif codigo:
            st.warning("NCM não encontrada na base local. Buscando em banco externo...")
            st.info("Status: Aguardando integração com API do Governo Federal <span class='badge-dev'>EM DEV</span>", unsafe_allow_html=True)

    # --- ABA: SIMULADOR (O MOTOR REAL) ---
    elif st.session_state.aba == "Simul":
        st.markdown("<h1>Simulador de Custo Landed</h1>", unsafe_allow_html=True)
        with st.form("calc"):
            col1, col2 = st.columns(2)
            fob = col1.number_input("Valor FOB (USD)", min_value=0.0)
            frete = col2.number_input("Frete/Seguro (USD)", min_value=0.0)
            taxa = st.number_input("Câmbio (R$)", value=5.12)
            submit = st.form_submit_button("PROCESSAR CÁLCULO TRIBUTÁRIO")
            
            if submit:
                cif = (fob + frete) * taxa
                ii = cif * 0.14
                ipi = (cif + ii) * 0.15
                total = cif + ii + ipi
                
                st.markdown("<div class='card-motor'>", unsafe_allow_html=True)
                st.write(f"**Base de Cálculo (CIF):** R$ {cif:,.2f}")
                st.write(f"**Imposto de Importação (II):** R$ {ii:,.2f}")
                st.write(f"**IPI (Estimado):** R$ {ipi:,.2f}")
                st.markdown(f"### Custo Total Estimado: R$ {total:,.2f}")
                st.markdown("</div>", unsafe_allow_html=True)
                st.download_button("GERAR RELATÓRIO DE VIABILIDADE", "Relatorio TradeMind...", file_name="viabilidade.txt")

    # --- ABA: IA ---
    elif st.session_state.aba == "IA":
        st.markdown("<h1>Assistente de Legislação <span class='badge-dev'>EM DESENVOLVIMENTO</span></h1>", unsafe_allow_html=True)
        st.markdown("<div class='card-motor'>Aguardando conexão com banco de dados de legislação federal e API GPT-4.</div>", unsafe_allow_html=True)
        st.chat_input("Pergunte algo sobre o Regulamento Aduaneiro (Inativo no momento)...")

    # RODAPÉ
    st.markdown("<br><hr><center><small>TradeMind AI © 2026 - Valores Referenciais. Blindagem Jurídica Ativa.</small></center>", unsafe_allow_html=True)
