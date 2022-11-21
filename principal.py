import streamlit as st
import pandas as pd

st.title('Predição de gravidade COVID a partir de Prontuário')
st.header('(c)2022 - Giane Engel / Mirkos Martins')

genero = st.selectbox('Selecione o gênero do paciente:',('masculino','feminino'))
idade = st.number_input('Digite a idade do paciente:',min_value=1,max_value=150,step=1)
RDW = st.number_input('RDW (%)')
leucocitos = st.number_input('Leucocitos (x109/L)',step=0.1)

