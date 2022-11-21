import streamlit as st
import pandas as pd

st.title('Predição de gravidade COVID a partir de Prontuário')
st.header('(c)2022 - Giane Engel / Mirkos Martins')

genero = st.select_box('Selecione o gênero do paciente:',('masculino','feminino'))
