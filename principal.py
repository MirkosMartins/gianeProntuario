import streamlit as st
import pandas as pd

st.title('Predição de gravidade COVID a partir de Prontuário')
st.header('(c)2022 - Giane Engel / Mirkos Martins')

genero = st.selectbox('Selecione o gênero do paciente:',('masculino','feminino'))
idade = st.number_input('Digite a idade do paciente:',min_value=1,max_value=150,step=1)
