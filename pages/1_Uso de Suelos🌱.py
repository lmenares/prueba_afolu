import streamlit as st
import pandas as pd
import altair as alt

st.title("Uso de Suelos 🌱")

st.markdown('El sector uso de suelos bla bla... ')
st.markdown('''
            :violet[***Seleccione el nivel de implementación de cada medida en las barras de la izquierda***]''')
st.markdown('A continuación se muestran los resultados segun los siguientes niveles seleccionados para cada medida:')


bau = pd.read_csv('https://raw.githubusercontent.com/lmenares/prueba_afolu/main/tableau_p3.csv')
foresta=pd.read_excel('https://github.com/lmenares/prueba_afolu/blob/main/tableau_p3.xlsx', sheet_name='forestacion')
manejo=pd.read_excel('https://github.com/lmenares/prueba_afolu/blob/main/tableau_p3.xlsx', sheet_name='manejo')
areas=pd.read_excel('https://github.com/lmenares/prueba_afolu/blob/main/tableau_p3.xlsx', sheet_name='areas')
incendios=pd.read_excel('https://github.com/lmenares/prueba_afolu/blob/main/tableau_p3.xlsx', sheet_name='incendios')


imp_forest = st.sidebar.select_slider(
    'Nivel de implementación de Forestación',
    options=[0,0.1,0.5,1])
st.write('Forestación:',imp_forest*100,'%', 'de implementacion de la medida')

imp_manejo = st.sidebar.select_slider(
    'Nivel de implementación de Planes de manejo',
    options=[0,0.1,0.5,1])
st.write('Planes de Manejo:', imp_manejo*100,'%', 'de implementacion de la medida')

imp_areas = st.sidebar.select_slider(
    'Nivel de implementación de Áreas protegidas',
    options=[0,0.1,0.5,1])
st.write('Áreas protegidas:', imp_manejo*100,'%', 'de implementacion de la medida')

imp_incendios = st.sidebar.select_slider(
    'Nivel de implementación de Reducción de incendios',
    options=[0,0.1,0.5,1])
st.write('Reducción de incendios:', imp_manejo*100,'%', 'de implementacion de la medida')

mit_forest=foresta[foresta['i_forestacion']==imp_forest]
mit_manejo=manejo[manejo['i_manejo']==imp_manejo]
mit_areas=areas[areas['i_areas']==imp_areas]
mit_incendios=incendios[incendios['i_incendios']==imp_incendios]

medidas=pd.merge(mit_forest,mit_manejo,on='tiempo')
medidas=pd.merge(medidas,mit_areas, on='tiempo')
medidas=pd.merge(medidas,mit_incendios, on='tiempo')

df_mit=pd.merge(bau,medidas,on='tiempo')
df_mit['emis_mit']=df_mit['bau']-df_mit['m_forestacion']-df_mit['m_manejo']-df_mit['m_areas']-df_mit['m_incendios']

#st.write(df_mit)


chart_bau = alt.Chart(bau).mark_line().encode(
    x='tiempo:O',
    y=alt.Y('bau:Q',title='Emisiones (Mt CO2eq)'),
    detail='id_futuro:N',
).properties(
    width=400,
).configure_mark(color='grey')

chart_bau = chart_bau.configure_legend(
    title=None,
    labelFontSize=0,
    symbolSize=0,
)


chart_mit = alt.Chart(df_mit).mark_line().encode(
    x='tiempo:O',
    y=alt.Y('emis_mit:Q',title='Emisiones (Mt CO2eq)'),
    detail='id_futuro:N',
).properties(
    width=400,
).configure_mark(color='teal')

chart_mit = chart_mit.configure_legend(
    title=None,
    labelFontSize=0,
    symbolSize=0,
)



tab1, tab2= st.tabs(["Línea Base","Escenario Mitigación"])

with tab1:
   #st.header("A cat")
   st.altair_chart(chart_bau, use_container_width=True)

with tab2:
   #st.header("A dog")
   st.altair_chart(chart_mit, use_container_width=True)

mit_forest_b=mit_forest.rename(columns={'m_forestacion':'mitigacion'}).drop(columns=['i_forestacion'])
mit_forest_b['medida']='forestacion'

mit_manejo_b=mit_manejo.rename(columns={'m_manejo':'mitigacion'}).drop(columns=['i_manejo'])
mit_manejo_b['medida']='manejo'

mit_areas_b=mit_areas.rename(columns={'m_areas':'mitigacion'}).drop(columns=['i_areas'])
mit_areas_b['medida']='areas'

mit_incendios_b=mit_incendios.rename(columns={'m_incendios':'mitigacion'}).drop(columns=['i_incendios'])
mit_incendios_b['medida']='incendios'

df_medidas=pd.concat([mit_forest_b,mit_manejo_b,mit_areas_b,mit_incendios_b],axis=0)
df_medidas=df_medidas[df_medidas['tiempo']>2020]

#st.write(df_medidas)

medidas_names=['forestacion','manejo']
colors = ["#aa423a","#f6b404"]

med_selec=alt.selection_single(fields=["medida"], empty='all')

region_pie = (
    (
        alt.Chart(df_medidas).mark_bar().encode(
           alt.X('sum(mitigacion):Q'),
           alt.Y('medida:N'),
           alt.Color('medida:N'),
           opacity=alt.condition(med_selec, alt.value(1), alt.value(0.25)),
        )
    )
    .add_selection(med_selec)
    .properties(title="Mitigación por medida")
)

anual= (
     (
         alt.Chart(df_medidas).mark_bar().encode(
            alt.X('tiempo:Q'),
            alt.Y('mitigacion:Q'),
            alt.Color('medida:N'),
#            #opacity=alt.condition(med_selec, alt.value(1), alt.value(0.25)),
         )
     )
#     #.add_selection(med_selec)
#     #.properties(title="Mitigación por medida")
 )


# anual= (alt.Chart(df_medidas).mark_bar().encode(
#     alt.X('tiempo:Q'),
#     alt.Y('mitigacion:Q'),
#     alt.Color('medida:N'))
#     ).transform_filter(med_selec)

# region_summary = (
#     (
#         alt.Chart(df_medidas)
#         .mark_bar()
#         .encode(
#             x=alt.X(
#                 "tiempo",
#                 type="temporal",
#             ),
#             y=alt.Y(
#                 'mitigacion',
#                 type="quantitative",
#                 title="Total mitigacion",
#             ),
#             color=alt.Color(
#                 "medida",
#                 type="nominal",
#                 title="Medidas",
#                 scale=alt.Scale(domain=regions, range=colors),
#                 legend=alt.Legend(
#                     direction="vertical",
#                     symbolType="triangle-left",
#                     tickCount=2,
#                 ),
#             ),
#         )
#     )
#    .transform_filter(med_selec)
#    .properties(width=700, title="Monthly Sales")
# )

st.altair_chart(region_pie,use_container_width=True)

st.altair_chart(anual,use_container_width=True)
