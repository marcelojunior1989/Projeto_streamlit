import streamlit as st
import pandas as pd 
from datetime import date

def gravar_dados(nome,data_nasc,tipo):          
    erros = []   
    if ((data_nasc <= date.today()) or (data_nasc is none)):
        erros.append("Por favor, preencha a data de nascimento.")

    if not nome:
        erros.append("Por favor, preencha o nome.")

    if dt_nasc is not None and dt_nasc > date.today():
        erros.append("A data de nascimento não pode ser no futuro.")
    
    if nome and data_nasc <= date.today():
        with open("clientes.csv","a",encoding="utf-8") as file:
            file.write(f"{nome},{data_nasc},{tipo}\n")
        st.session_state["sucesso"]=True
    else:
        st.session_state["sucesso"]=False    

st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="🙎"
)

st.title("cadastro de clientes")
st.divider()

nome = st.text_input("Digite o nome do Cliente",key="nome_cliente")

dt_nasc=st.date_input("Data Nascimento",format="DD/MM/YYYY")
tipo=st.selectbox("Tipo do cliente",
                  ["Pessoa Fisica","Pessoa Juridica"])

btn_Cadastrar = st.button("Cadastrar",
                          on_click=gravar_dados,
                          args=[nome, dt_nasc, tipo])

if btn_Cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="🔥")
    else:
        st.error("Houve algum problema no cadastro")    