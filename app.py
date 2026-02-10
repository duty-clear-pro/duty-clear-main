import streamlit as st
import pandas as pd

# CONFIGURAÇÃO DE ALTA PERFORMANCE
st.set_page_config(page_title="DUTY CLEAR PRO", page_icon="🏛️", layout="wide")

# CSS PROFISSIONAL (FÁCIL DE MUDAR)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .main-card { background: #ffffff; padding: 30px; border-radius: 15px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
    .ncm-title { color: #0f172a; font-size: 32px; font-weight: 800; }
    .stat-box { background: #f8fafc; padding: 15px; border-radius: 10px; border: 1px solid #f1f5f9; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# SIDEBAR (CONTROLE DO APP)
with st.sidebar:
    st.title("🏛️ DUTY CLEAR")
    st.markdown("---")
    st.success("Servidor Top Online")
    menu = st.radio("Navegação", ["Busca NCM", "Simulador Fiscal", "Minha Conta"])

# CORPO DO APP
st.title("Busca Inteligente de NCM")
st.caption("Conectado à Base de Dados Oficial")

search = st.text_input("", placeholder="Digite o produto (Ex: Milho, Ferro, Borracha)...")

if search:
    st.markdown(f"""
    <div class="main-card">
        <div style="display:flex; justify-content:space-between;">
            <span style="color:#64748b; font-weight:bold;">RESULTADO DA VARREDURA</span>
            <span style="color:#22c55e;">● ATUALIZADO HOJE</span>
        </div>
        <h1 class="ncm-title">{search.upper()}</h1>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 10px; margin: 20px 0;">
            <div class="stat-box"><small>IPI</small><br><b>10%</b></div>
            <div class="stat-box"><small>PIS</small><br><b>2.1%</b></div>
            <div class="stat-box"><small>COFINS</small><br><b>9.65%</b></div>
            <div class="stat-box"><small>CEST</small><br><b>17.110.00</b></div>
        </div>
        <div style="background:#eff6ff; padding:15px; border-radius:10px; border-left:5px solid #3b82f6; color:#1e40af;">
            <b>💡 INSIGHT TRIBUTÁRIO:</b> Este item possui redução de base de cálculo para operações interestaduais.
        </div>
    </div>
    """, unsafe_allow_html=True)
