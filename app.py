import streamlit as st

# 1. Configurações de Elite
st.set_page_config(page_title="UAU Logística", page_icon="⚖️", layout="wide")

# Link da Logo (Substitua pelo seu link se tiver um específico)
logo_url = "https://cdn-icons-png.flaticon.com/512/4370/4370714.png" 

# 2. Estilo Visual (Branding UAU)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .login-box {
        background-color: #1A2B48;
        padding: 40px;
        border-radius: 15px;
        color: white;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.3);
    }
    .feature-item {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #B8964E;
        margin-bottom: 15px;
        color: #1A2B48;
    }
    .title-main { color: #1A2B48; font-weight: 900; font-size: 48px; margin-bottom: 0px; line-height: 1;}
    .slogan-main { color: #B8964E; font-size: 20px; font-style: italic; margin-bottom: 30px; }
    .footer-text { font-size: 12px; color: #666; text-align: center; margin-top: 50px; border-top: 1px solid #eee; padding-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Gerenciamento de Acesso
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    # --- TELA DE APRESENTAÇÃO COM LOGO ---
    col_info, _, col_login = st.columns([1.2, 0.2, 1])
    
    with col_info:
        st.image(logo_url, width=80) # LOGO AQUI
        st.markdown("<h1 class='title-main'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
        st.markdown("<p class='slogan-main'>A precisão que o seu lucro exige.</p>", unsafe_allow_html=True)
        
        st.markdown("### Inteligência para Gestão de Fretes")
        st.markdown("""
        <div class="feature-item">
            <b>📊 Simulador de Margem Líquida</b><br>
            Cálculos instantâneos de lucratividade por carga.
        </div>
        <div class="feature-item">
            <b>🔍 Base Referencial NCM</b><br>
            Consulta rápida de tributação e classificação.
        </div>
        <div class="feature-item">
            <b>📄 Relatórios Executivos</b><br>
            Geração de dados para suporte à decisão rápida.
        </div>
        """, unsafe_allow_html=True)

    with col_login:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.subheader("🔑 Acesso ao Servidor")
        user = st.text_input("Usuário VIP")
        password = st.text_input("Chave de Segurança", type="password")
        if st.button("AUTENTICAR"):
            if user == "gestor.vip" and password == "UAU2026":
                st.session_state['autenticado'] = True
                st.rerun()
            else:
                st.error("Credenciais incorretas.")
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- DASHBOARD COM LOGO NO MENU ---
    st.sidebar.image(logo_url, width=100) # LOGO NO MENU
    st.sidebar.title("UAU Logística")
    st.sidebar.write(f"Usuário: **Gestor VIP**")
    
    if st.sidebar.button("Sair do Sistema"):
        st.session_state['autenticado'] = False
        st.rerun()

    st.markdown(f"<h1 style='color: #1A2B48;'>Dashboard de Operações</h1>", unsafe_allow_html=True)
    st.write("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        with st.container(border=True):
            st.subheader("🚀 Simulador de Carga")
            produto = st.text_input("Produto ou NCM", placeholder="Ex: Milho, Soja, 1201.90.00")
            
            c1, c2 = st.columns(2)
            v_carga = c1.number_input("Valor da Carga (R$)", min_value=0.0)
            v_frete = c2.number_input("Custo do Frete (R$)", min_value=0.0)
            
            if st.button("CALCULAR MARGEM LÍQUIDA"):
                imposto = v_carga * 0.12
                lucro = v_carga - v_frete - imposto
                
                st.markdown(f"""
                    <div style='background-color: #1A2B48; padding: 20px; border-radius: 10px; text-align: center; color: white;'>
                        <h3 style='margin:0;'>Lucro Líquido Estimado</h3>
                        <h1 style='color: #B8964E; margin:0;'>R$ {lucro:,.2f}</h1>
                    </div>
                """, unsafe_allow_html=True)

    with col2:
        st.subheader("🛠️ Ações Rápidas")
        st.button("📄 Baixar PDF do Relatório")
        st.button("💬 Enviar via WhatsApp")
        st.divider()
        st.info("**Nota Técnica:** Alíquotas baseadas em 12% (Referencial).")

    st.markdown("""
        <div class='footer-text'>
            <b>AVISO DE CONSULTA:</b> O UAU LOGÍSTICA é uma ferramenta de consulta baseada em dados referenciais. 
            A decisão final é de total responsabilidade do gestor.<br>
            Suporte: <b>suporte@uaulogistica.com</b>
        </div>
        """, unsafe_allow_html=True)
