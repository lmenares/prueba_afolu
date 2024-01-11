import streamlit as st
import pandas as pd
import altair as alt
from streamlit_dynamic_filters import DynamicFilters

st.set_page_config(
    page_title="Hello",
)

st.write("# Proyecto AFOLU")

st.sidebar.success("Seleccione un sector")

st.markdown(
    """
    En este proyecto se analizaron las trayectorias de emisiones de los sectores
 bla bla...
###### Se consideraron las siguientes medidas de mitigación para Uso de Suelos:

"""
)

st.image('folu_c.jpg')

st.markdown(
    """
###### Y Agricultura:

"""
)

st.image('agro_c.jpg')

st.markdown(
    """
### Para explorar los resultados por sector, ingrese al menú de la izquierda 👈

"""
)

