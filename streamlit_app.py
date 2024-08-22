import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

@st.cache_data
def gerar_df():
  df=pd.read_excel(
    io="estrutura_tarifaria_2024.xlsx",
    engine="openpyxl",
    sheet_name="Table 1",
    usecols="A:I",
    nrows=28
  )
  return df
df=gerar_df()
with st.sidebar:
  logo=Image.open('logo_sanesul.png')
  st.image(logo, use_column_width=True)
  
def click_button ():
  print("teste")
  st.write(valor)
  
st.title("Cálculo consumo de água")
st.header("Estrutura tarifária Sanesul")

valor = st.text_input("Informe seu consumo de água")
st.button('Calcular', on_click=click_button)
