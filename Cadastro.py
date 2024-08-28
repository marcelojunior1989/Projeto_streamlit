import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, data_nasc, tipo):          
    erros = []
    
    if not data_nasc or data_nasc > date.today():
        erros.append("Por favor, data de nascimento inválida.")
    
    if not nome:
        erros.append("Por favor, preencha o nome.")
    
    if erros:
        st.session_state["sucesso"] = False
        st.error("\n".join(erros))
    else:
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{data_nasc},{tipo}\n")
        st.session_state["sucesso"] = True

st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="🙎"
)

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digite o nome do Cliente", key="nome_cliente")
dt_nasc = st.date_input("Data de Nascimento", format="DD/MM/YYYY")
tipo = st.selectbox("Tipo do Cliente", ["Pessoa Física", "Pessoa Jurídica"])

btn_Cadastrar = st.button("Cadastrar",
                          on_click=gravar_dados,
                          args=[nome, dt_nasc, tipo])

if "sucesso" in st.session_state:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!", icon="🔥")
    else:
        st.error("Houve algum problema no cadastro")
