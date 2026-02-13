import streamlit as st

# 1. Configuração de Interface de Elite
st.set_page_config(page_title="UAU Logística", page_icon="⚖️", layout="centered")

# 2. Estilização CSS (Identidade Visual UAU)
st.markdown("""
    <style>
    .main { background-color: #F4F4F4; }
    .stButton>button { 
        background-color: #1A2B48; 
        color: white; 
        width: 100%; 
        border-radius: 8px; 
        height: 3em; 
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover { border: 1px solid #B8964E; color: #B8964E; }
    .title-text { color: #1A2B48; text-align: center; font-family: 'Arial'; margin-bottom: 0px; font-weight: bold; }
    .slogan-text { color: #B8964E; text-align: center; font-style: italic; font-size: 18px; margin-bottom: 30px; }
    .footer-box { 
        font-size: 12px; 
        color: #666; 
        text-align: center; 
        margin-top: 50px; 
        padding: 20px; 
        border-top: 1px solid #ccc; 
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sistema de Segurança (Login) [cite: 2026-02-08]
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    st.markdown("<h1 class='title-text'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
    with st.container():
        st.write("---")
        st.subheader("🔐 Acesso ao Servidor VIP")
        usuario = st.text_input("Usuário do Gestor")
        senha = st.text_input("Senha de Acesso", type="password")
        
        if st.button("ACESSAR SISTEMA"):
            if usuario == "gestor.vip" and senha == "UAU2026":
                st.session_state['autenticado'] = True
                st.rerun()
            else:
                st.error("Acesso negado. Verifique as credenciais.")
else:
    # 4. Dashboard Principal
    st.markdown("<h1 class='title-text'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
    st.markdown("<p class='slogan-text'>A precisão que o seu lucro exige.</p>", unsafe_allow_html=True)

    with st.expander("📊 Simulador de Margem Líquida", expanded=True):
        st.write("Preencha os dados abaixo para consulta referencial:")
        
        busca = st.text_input("Produto ou NCM", placeholder="Ex: Milho, Soja, Ferro...")
        
        c1, c2 = st.columns(2)
        with c1:
            valor_carga = st.number_input("Valor da Carga (R$)", min_value=0.0, step=100.0)
        with c2:
            custo_frete = st.number_input("Custo do Frete (R$)", min_value=0.0, step=50.0)

        if st.button("CALCULAR LUCRO LÍQUIDO"):
            # Lógica: Valor - Frete - 12% de impostos (Base Referencial)
            imposto_est = valor_carga * 0.12
            resultado = valor_carga - custo_frete - imposto_est
            
            st.markdown(f"""
                <div style='background-color: #1A2B48; padding: 20px; border-radius: 10px; text-align: center;'>
                    <h2 style='color: #B8964E; margin: 0;'>Lucro Líquido Estimado</h2>
                    <h1 style='color: white; margin: 0;'>R$ {resultado:,.2f}</h1>
                </div>
            """, unsafe_allow_html=True)
            st.caption("⚠️ O cálculo utiliza uma base de 12% de impostos estimados.")

    # 5. Blindagem Jurídica e Suporte (Sua Proteção como Auxiliar)
    st.markdown(f"""
        <div class='footer-box'>
            <b>TERMO DE USO E RESPONSABILIDADE:</b><br>
            O <b>UAU LOGÍSTICA</b> é uma ferramenta de consulta baseada em dados referenciais. 
            As simulações são estimativas e não substituem a análise técnica, fiscal ou contábil oficial. 
            A decisão final sobre carregamentos, produção e fretes é de total responsabilidade do usuário gestor.<br><br>
            <b>SUPORTE TÉCNICO:</b> suporte@uaulogistica.com<br>
            <i>Prazo de resposta: Até 24 horas úteis.</i>
        </div>
        """, unsafe_allow_html=True)

    if st.sidebar.button("Sair do Sistema"):
        st.session_state['autenticado'] = False
        st.rerun()
