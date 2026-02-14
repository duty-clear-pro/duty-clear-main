import streamlit as st
import sqlite3
import bcrypt
from datetime import datetime

# ==============================
# CONFIGURAÇÃO INICIAL
# ==============================

st.set_page_config(page_title="TradeMind", layout="wide")

conn = sqlite3.connect("trademind.db", check_same_thread=False)
cursor = conn.cursor()

# ==============================
# CRIAÇÃO DAS TABELAS
# ==============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS empresas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    plano TEXT,
    status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT UNIQUE,
    senha TEXT,
    perfil TEXT,
    empresa_id INTEGER,
    status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    empresa_id INTEGER,
    acao TEXT,
    data_hora TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS analises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa_id INTEGER,
    usuario_id INTEGER,
    produto TEXT,
    ncm_sugerida TEXT,
    risco TEXT,
    data_hora TEXT
)
""")

conn.commit()

# ==============================
# FUNÇÕES AUXILIARES
# ==============================

def registrar_log(usuario_id, empresa_id, acao):
    cursor.execute("""
    INSERT INTO logs (usuario_id, empresa_id, acao, data_hora)
    VALUES (?, ?, ?, ?)
    """, (usuario_id, empresa_id, acao, datetime.now()))
    conn.commit()


def criar_empresa_padrao():
    cursor.execute("SELECT * FROM empresas")
    if not cursor.fetchone():
        cursor.execute("""
        INSERT INTO empresas (nome, plano, status)
        VALUES ('Empresa Demo', 'Pro', 'ativo')
        """)
        conn.commit()


def criar_admin_padrao():
    cursor.execute("SELECT * FROM usuarios")
    if not cursor.fetchone():
        senha_hash = bcrypt.hashpw("admin123".encode(), bcrypt.gensalt())
        cursor.execute("""
        INSERT INTO usuarios (nome, email, senha, perfil, empresa_id, status)
        VALUES (?, ?, ?, ?, ?, ?)
        """, ("Administrador", "admin@trademind.com", senha_hash,
              "Administrador", 1, "ativo"))
        conn.commit()


criar_empresa_padrao()
criar_admin_padrao()

# ==============================
# LOGIN
# ==============================

if "usuario" not in st.session_state:
    st.title("TradeMind")
    st.subheader("Plataforma de Inteligência Fiscal")

    email = st.text_input("E-mail")
    senha = st.text_input("Senha", type="password")

    if st.button("Acessar Plataforma"):
        cursor.execute("SELECT * FROM usuarios WHERE email=?", (email,))
        user = cursor.fetchone()

        if user:
            if bcrypt.checkpw(senha.encode(), user[3]):
                st.session_state.usuario = {
                    "id": user[0],
                    "nome": user[1],
                    "perfil": user[4],
                    "empresa_id": user[5]
                }
                registrar_log(user[0], user[5], "Login realizado")
                st.rerun()
            else:
                st.error("Senha incorreta")
        else:
            st.error("Usuário não encontrado")

    st.stop()

# ==============================
# PORTAL PRINCIPAL
# ==============================

usuario = st.session_state.usuario

st.sidebar.title("TradeMind")
st.sidebar.write(f"Usuário: {usuario['nome']}")
st.sidebar.write(f"Perfil: {usuario['perfil']}")

menu = st.sidebar.radio("Menu", [
    "Dashboard",
    "Inteligência NCM",
    "Histórico",
    "Gestão de Usuários",
    "Auditoria",
    "Sair"
])

# ==============================
# DASHBOARD
# ==============================

if menu == "Dashboard":
    st.title("Centro de Inteligência Tributária")
    st.write("Ambiente corporativo de análise fiscal.")

# ==============================
# INTELIGÊNCIA NCM
# ==============================

if menu == "Inteligência NCM":
    st.title("Análise de Classificação Fiscal")

    produto = st.text_area("Descreva tecnicamente o produto")

    if st.button("Analisar"):
        # Simulação de IA
        ncm = "0000.00.00"
        risco = "Moderado"

        cursor.execute("""
        INSERT INTO analises (empresa_id, usuario_id, produto, ncm_sugerida, risco, data_hora)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (usuario["empresa_id"], usuario["id"],
              produto, ncm, risco, datetime.now()))
        conn.commit()

        registrar_log(usuario["id"], usuario["empresa_id"],
                      "Nova análise criada")

        st.success("Análise registrada")
        st.write("NCM sugerida:", ncm)
        st.write("Nível de risco:", risco)

# ==============================
# HISTÓRICO
# ==============================

if menu == "Histórico":
    st.title("Histórico de Análises")

    cursor.execute("""
    SELECT produto, ncm_sugerida, risco, data_hora
    FROM analises
    WHERE empresa_id=?
    """, (usuario["empresa_id"],))

    dados = cursor.fetchall()

    for row in dados:
        st.write("Produto:", row[0])
        st.write("NCM:", row[1])
        st.write("Risco:", row[2])
        st.write("Data:", row[3])
        st.divider()

# ==============================
# GESTÃO DE USUÁRIOS
# ==============================

if menu == "Gestão de Usuários":

    if usuario["perfil"] != "Administrador":
        st.warning("Acesso restrito ao Administrador")
    else:
        st.title("Gestão de Usuários")

        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        perfil = st.selectbox("Perfil", [
            "Administrador", "Analista", "Consulta"
        ])

        if st.button("Criar Usuário"):
            senha_hash = bcrypt.hashpw(
                senha.encode(), bcrypt.gensalt())
            try:
                cursor.execute("""
                INSERT INTO usuarios (nome, email, senha, perfil, empresa_id, status)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (nome, email, senha_hash, perfil,
                      usuario["empresa_id"], "ativo"))
                conn.commit()

                registrar_log(usuario["id"],
                              usuario["empresa_id"],
                              "Usuário criado")

                st.success("Usuário criado com sucesso")
            except:
                st.error("E-mail já cadastrado")

# ==============================
# AUDITORIA
# ==============================

if menu == "Auditoria":
    st.title("Log de Atividades")

    cursor.execute("""
    SELECT acao, data_hora
    FROM logs
    WHERE empresa_id=?
    ORDER BY data_hora DESC
    """, (usuario["empresa_id"],))

    logs = cursor.fetchall()

    for log in logs:
        st.write(log[0], "-", log[1])

# ==============================
# SAIR
# ==============================

if menu == "Sair":
    st.session_state.clear()
    st.rerun()
