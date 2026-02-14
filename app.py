import streamlit as st
from datetime import datetime

# CONFIG
st.set_page_config(
    page_title="TradeMind",
    layout="wide"
)

# SIDEBAR
with st.sidebar:
    st.title("TRADEMIND")
    menu = st.radio(
        "Navegação",
        ["Dashboard", "Inteligência NCM", "Assistente IA", "Quem Somos"]
    )
    st.divider()
    st.caption("© 2026 TradeMind")

# DASHBOARD
if menu == "Dashboard":
    st.title("Terminal TradeMind")
    st.write("Bem-vindo, Igor •", datetime.now().strftime("%d/%m/%Y"))

    col1, col2, col3 = st.columns(3)

    col1.metric("Dólar", "R$ 5,12", "+0.12%")
    col2.metric("Euro", "R$ 5,48", "-0.05%")
    col3.metric("Base NCM", "15.160", "Auditada")

# INTELIGÊNCIA NCM
elif menu == "Inteligência NCM":
    st.title("Classificação Fiscal NCM")

    busca = st.text_input("Digite descrição ou código NCM")

    if busca:
        st.subheader("Resultado da Análise")
        st.write("NCM: 8471.30.12")
        st.write("Descrição: Máquinas automáticas para processamento de dados")
        st.write("Nível de Risco: Baixo")
        st.write("Observação: Confirmar enquadramento conforme NESH")

        if st.button("Gerar Relatório Técnico"):
            st.success("Relatório gerado com sucesso (simulação)")

# ASSISTENTE IA
elif menu == "Assistente IA":
    st.title("Consultor Tributário TradeMind")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.chat_input("Digite sua dúvida fiscal")

    if user_input:
        st.session_state.messages.append(("user", user_input))
        resposta = "Recomendamos validar a NCM com base na descrição técnica detalhada."
        st.session_state.messages.append(("assistant", resposta))

    for role, msg in st.session_state.messages:
        with st.chat_message(role):
            st.write(msg)

# QUEM SOMOS
elif menu == "Quem Somos":
    st.title("Nossa Inteligência Estratégica")

    st.write("Missão:")
    st.write("Oferecer inteligência fiscal aplicada à classificação NCM com segurança jurídica.")

    st.write("Visão:")
    st.write("Ser referência nacional em tecnologia para classificação fiscal estratégica.")

    st.write("Valores:")
    st.write("Conformidade • Precisão • Responsabilidade Técnica")
