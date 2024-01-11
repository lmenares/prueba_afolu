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

# st.title("AFOLU")
# bau = pd.read_excel('C:\\Users\\lunam\\Desktop\\Streamlit_afolu\\tableau_p3.xlsx', sheet_name='bau')
# foresta=pd.read_excel('C:\\Users\\lunam\\Desktop\\Streamlit_afolu\\tableau_p3.xlsx', sheet_name='forestacion')
# manejo=pd.read_excel('C:\\Users\\lunam\\Desktop\\Streamlit_afolu\\tableau_p3.xlsx', sheet_name='manejo')

# chart = alt.Chart(bau).mark_line().encode(
#     x='tiempo:O',
#     y='bau:Q',
#     detail='id_futuro:N',
#     #color='grey'  
# ).properties(
#     width=400,  
# )

# chart = chart.configure_legend(
#     title=None,       
#     labelFontSize=0,  
#     symbolSize=0,     
# )


# st.altair_chart(chart, use_container_width=True)



# dynamic_filters = DynamicFilters(bau, filters=['tiempo', 'id_futuro'])

# with st.sidebar:
#     dynamic_filters.display_filters()

# datab= dynamic_filters.display_df()

# # Verificar si los filtros están activos
# if datab is not None:
#     # Crear el gráfico de líneas con Altair usando el DataFrame filtrado
#     chart = alt.Chart(datab.filter_df).mark_line().encode(
#         x='tiempo:O',
#         y='valor:Q',
#         color='id_futuro:N',
#     )

#     # Mostrar el gráfico en Streamlit
#     st.altair_chart(chart, use_container_width=True)
# else:
#     st.warning("No hay datos filtrados. Ajusta los filtros para ver datos.")