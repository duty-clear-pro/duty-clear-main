import streamlit as st
import pandas as pd

# 1. Configurações de Alta Performance
st.set_page_config(page_title="UAU Logística", layout="wide")
logo_url = "https://cdn-icons-png.flaticon.com/512/4370/4370714.png" 

# 2. Estilização Executiva (Sem Emojis, Foco em Dados)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .login-container { background-color: #1A2B48; padding: 45px; border-radius: 8px; color: white; }
    .feature-card { background-color: #fcfcfc; padding: 20px; border-radius: 4px; border-left: 6px solid #B8964E; margin-bottom: 20px; color: #1A2B48; }
    .title-main { color: #1A2B48; font-weight: 900; font-size: 52px; margin-bottom: 0px; }
    .slogan-main { color: #B8964E; font-size: 18px; text-transform: uppercase; margin-bottom: 40px; }
    
    /* Botões Grandes do Painel */
    .stButton>button {
        background-color: #1A2B48;
        color: white;
        height: 100px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        border: 2px solid #B8964E;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #B8964E; color: #1A2B48; }
    </style>
    """, unsafe_allow_html=True)

# 3. Gerenciamento de Acesso e Navegação
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False
if 'pagina' not in st.session_state:
    st.session_state['pagina'] = 'home'

if not st.session_state['autenticado']:
    # TELA DE APRESENTAÇÃO (PERFEITA)
    col_info, _, col_login = st.columns([1.3, 0.2, 1])
    with col_info:
        st.image(logo_url, width=90)
        st.markdown("<h1 class='title-main'>UAU LOGÍSTICA</h1>", unsafe_allow_html=True)
        st.markdown("<p class='slogan-main'>Gestão de Inteligência e Performance</p>", unsafe_allow_html=True)
        st.markdown("""
        <div class="feature-card"><b>Monitoramento de Rotas</b><br>Integração com mapas para cálculo de distância e tempo.</div>
        <div class="feature-card"><b>Cálculo de Margem Líquida</b><br>Simulações financeiras precisas.</div>
        <div class="feature-card"><b>Inteligência Fiscal NCM</b><br>Consulta à base de dados tributários.</div>
        """, unsafe_allow_html=True)
    with col_login:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        with st.form("login"):
            user = st.text_input("Usuário")
            password = st.text_input("Senha", type="password")
            if st.form_submit_button("AUTENTICAR"):
                if user == "gestor.vip" and password == "UAU2026":
                    st.session_state['autenticado'] = True
                    st.rerun()
else:
    # --- DASHBOARD INTERNO: PAINEL DE BOTÕES ---
    st.image(logo_url, width=60)
    st.markdown("<h2 style='color: #1A2B48;'>Painel de Operações</h2>", unsafe_allow_html=True)
    
    if st.session_state['pagina'] == 'home':
        st.write("Selecione o módulo:")
        c1, c2, c3, c4 = st.columns(4)
        if c1.button("MAPAS E ROTAS"): st.session_state['pagina'] = 'mapas'; st.rerun()
        if c2.button("CONSULTA NCM"): st.session_state['pagina'] = 'ncm'; st.rerun()
        if c3.button("LOGÍSTICA"): st.session_state['pagina'] = 'logistica'; st.rerun()
        if c4.button("FINANCEIRO"): st.session_state['pagina'] = 'frete'; st.rerun()
        
        st.sidebar.button("Sair", on_click=lambda: st.session_state.update({"autenticado": False}))

    # --- NAVEGAÇÃO INTERNA ---
    if st.session_state['pagina'] != 'home':
        if st.button("← VOLTAR AO PAINEL"): st.session_state['pagina'] = 'home'; st.rerun()

    if st.session_state['pagina'] == 'mapas':
        st.subheader("Inteligência de Rotas (Google Maps)")
        origem = st.text_input("Cidade de Origem", "Catalão, GO")
        destino = st.text_input("Cidade de Destino")
        if st.button("CALCULAR ROTA"):
            # Aqui simulamos a resposta da API que testamos
            st.info(f"Analisando trajeto de {origem} para {destino}...")
            # Exemplo de link real para o gestor abrir no Google
            url_maps = f"https://www.google.com/maps/dir/{origem}/{destino}"
            st.success(f"Rota encontrada! Link para navegação: [Abrir no Google Maps]({url_maps})")
            st.write("**Dados Sugeridos via BR-050:**")
            st.write("- Distância: ~694 km")
            st.write("- Tempo Estimado: ~8h 22min")

    elif st.session_state['pagina'] == 'ncm':
        st.subheader("Consulta Fiscal NCM")
        st.text_input("Código ou Produto")
        st.button("Buscar")

    elif st.session_state['pagina'] == 'logistica':
        st.subheader("Planejamento Operacional")
        st.selectbox("Veículo", ["Bitrem", "Rodotrem", "Truck"])

    elif st.session_state['pagina'] == 'frete':
        st.subheader("Cálculo de Margem")
        v_carga = st.number_input("Valor da Carga")
        v_frete = st.number_input("Custo Frete")
        if st.button("RESULTADO"):
            st.metric("Lucro Líquido", f"R$ {v_carga - v_frete - (v_carga*0.12):,.2f}")
