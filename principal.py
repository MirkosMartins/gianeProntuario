import streamlit as st
import pandas as pd

st.title('Predição de gravidade COVID a partir de Prontuário')
st.header('(c)2022 - Giane Engel / Mirkos Martins')

genero = st.selectbox('Selecione o gênero do paciente:',('masculino','feminino'))
idade = st.number_input('Digite a idade do paciente:',min_value=1,max_value=150,step=1)
RDW = st.number_input('RDW (%)',min_value=0)
leucocitos = st.number_input('Leucocitos (x109/L)',step=0.1)
monocitos = st.number_input('Monócitos (x109/L)',step=0.001)
linfocitos = st.number_input('Linfócitos (x109/L)',step=0.001)
plaquetas = st.number_input('Plaquetas (x109/L)',step=1000)
neutrofilos = st.number_input('Neutrófilos (x109/L)',step=0.001)
