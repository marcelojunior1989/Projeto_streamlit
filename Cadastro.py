import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(DATAS,tipo_combustivel,valor, Posto, TotalAbastecimento):          
    erros = []
    
    if not DATAS or DATAS > date.today():
        erros.append("Por favor, DATA inválida.")
    
#    if not nome:
#        erros.append("Por favor, preencha o nome.")

    if not tipo_combustivel:
        erros.append("Por favor, preencha o tipode combustivel.")

    if not valor:
        erros.append("Por favor, preencha o valor por litro.")
        
    if not Posto:
        erros.append("Por favor, preencha o nome do posto.")        
        
    if not TotalAbastecimento:
        erros.append("Por favor, preencha o valor total do abastecimento.")                     
    
    if erros:
        st.session_state["sucesso"] = False
        st.error("\n".join(erros))
    else:
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{DATA},{tipo}\n")
        st.session_state["sucesso"] = True

st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="🙎"
)

st.title("Cadastro de Clientes")
st.divider()

DATAS = st.date_input("Data de Nascimento", format="DD/MM/YYYY")
tipo_combustivel = st.selectbox("Tipo do Combustivel", ["Alcool", "Gasolina"])
valor = st.text_input("Digite o Valor do litro?")
Posto = st.text_input("Qual o posto?")
TotalAbastecimento = st.text_input("Digite o Valor Total do abastecimento?")


btn_Cadastrar = st.button("Cadastrar",
                          on_click=gravar_dados,
                          args=[DATAS, tipo_combustivel,valor, Posto, TotalAbastecimento])

if "sucesso" in st.session_state:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!", icon="🔥")
    else:
        st.error("Houve algum problema no cadastro")
