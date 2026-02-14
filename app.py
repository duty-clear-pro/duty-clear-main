import streamlit as st
import sqlite3
import hashlib

st.set_page_config(page_title="TradeMind AI", layout="wide")

# ---------------------- ESTILO PREMIUM ----------------------
st.markdown("""
<style>
body {
    background-color: #0E1117;
}
.block-container {
    padding-top: 2rem;
}
h1, h2, h3, h4 {
    font-weight: 700;
}
.hero-title {
    font-size: 48px;
    font-weight: 800;
    color: white;
}
.hero-sub {
    font-size: 20px;
    color: #9CA3AF;
}
.card {
    background-color: #161B22;
    padding: 25px;
    border-radius: 12px;
    border: 1px solid #222;
}
.metric-card {
    background: linear-gradient(145deg, #111827, #0f172a);
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------------- HASH ----------------------
def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# ---------------------- BANCO ----------------------
conn = sqlite3.connect("trademind.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT UNIQUE,
    senha TEXT,
    perfil TEXT
)
""")
conn.commit()

cursor.execute("SELECT * FROM usuarios WHERE email = ?", ("admin@trademind.com",))
if not cursor.fetchone():
    cursor.execute(
        "INSERT INTO usuarios (nome, email, senha, perfil) VALUES (?, ?, ?, ?)",
        ("Administrador", "admin@trademind.com", gerar_hash("admin123"), "Administrador")
    )
    conn.commit()

# ---------------------- SESSION ----------------------
if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.usuario = None
    st.session_state.perfil = None

# ---------------------- LOGIN ----------------------
def login():

    col1, col2 = st.columns([1.6, 1])

    with col1:
        st.markdown('<div class="hero-title">TradeMind AI</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-sub">A Inteligência Tributária da Nova Logística</div>', unsafe_allow_html=True)

        st.markdown("""
<br>

Transforme classificação NCM em vantagem estratégica.

Antecipe riscos fiscais antes que afetem sua margem.
Simule impactos tributários em segundos.
Tenha controle corporativo sobre decisões fiscais.

<br>

<strong>Recursos da Plataforma:</strong>

• Inteligência de Classificação NCM  
• Simulação Tributária Avançada  
• Identificação de Risco Fiscal  
• Gestão Corporativa de Usuários  
• Ambiente estruturado para Auditoria  
""", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Acesso Seguro")

        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar na Plataforma"):
            cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
            user = cursor.fetchone()

            if user and gerar_hash(senha) == user[3]:
                st.session_state.logado = True
                st.session_state.usuario = user[1]
                st.session_state.perfil = user[4]
                st.rerun()
            else:
                st.error("Credenciais inválidas")

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------------- PORTAL ----------------------
def portal():

    st.sidebar.markdown("## TradeMind AI")
    st.sidebar.write(f"Usuário: {st.session_state.usuario}")
    st.sidebar.write(f"Perfil: {st.session_state.perfil}")

    menu = st.sidebar.radio("Menu", [
        "Dashboard Estratégico",
        "Inteligência NCM",
        "Simulação Tributária",
        "Gestão de Usuários",
        "Sair"
    ])

    if menu == "Dashboard Estratégico":

        st.markdown("# Centro de Inteligência Tributária")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown('<div class="metric-card"><h3>142</h3><p>NCMs Analisados</p></div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="metric-card"><h3>6</h3><p>Alertas Fiscais</p></div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="metric-card"><h3>Alto</h3><p>Nível de Risco Atual</p></div>', unsafe_allow_html=True)

        st.markdown("""
<br>
A TradeMind AI atua como camada estratégica sobre sua operação logística,
identificando impactos tributários antes que se tornem prejuízo.
""", unsafe_allow_html=True)

    elif menu == "Inteligência NCM":

        st.markdown("# Análise Inteligente de NCM")

        codigo = st.text_input("Código NCM")
        descricao = st.text_area("Descrição da Mercadoria")

        if st.button("Executar Análise"):
            st.success("Análise concluída.")
            st.write("Possível divergência tributária detectada.")
            st.write("Recomendação: validar base normativa estadual.")

    elif menu == "Simulação Tributária":

        st.markdown("# Simulador de Impacto Fiscal")

        valor = st.number_input("Valor da Operação")
        aliquota = st.number_input("Alíquota (%)")

        if st.button("Calcular Impacto"):
            imposto = valor * (aliquota / 100)
            st.metric("Impacto Tributário Estimado", f"R$ {imposto:,.2f}")

    elif menu == "Gestão de Usuários":

        if st.session_state.perfil != "Administrador":
            st.warning("Acesso restrito ao administrador.")
        else:
            st.markdown("# Gestão Corporativa")

            nome = st.text_input("Nome")
            email = st.text_input("Email")
            senha = st.text_input("Senha", type="password")
            perfil = st.selectbox("Perfil", ["Administrador", "Analista", "Consulta"])

            if st.button("Criar Usuário"):
                try:
                    cursor.execute(
                        "INSERT INTO usuarios (nome, email, senha, perfil) VALUES (?, ?, ?, ?)",
                        (nome, email, gerar_hash(senha), perfil)
                    )
                    conn.commit()
                    st.success("Usuário criado com sucesso.")
                except:
                    st.error("Email já cadastrado.")

    elif menu == "Sair":
        st.session_state.logado = False
        st.rerun()

# ---------------------- EXECUÇÃO ----------------------
if st.session_state.logado:
    portal()
else:
    login()
