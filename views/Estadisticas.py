import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
import numpy as np
from local_components import card_container
from streamlit_shadcn_ui import slider, input, textarea, radio_group, switch


st.header("Trabajos presentados al CEI (2019 a 2024)")

import pandas as pd

# Especifica la ruta del archivo CSV
file_path = 'comite-etl-all.csv'

# Leer el archivo CSV y convertirlo en un DataFrame
df = pd.read_csv(file_path)

# Eliminar las filas con valores nulos
df = df.dropna()

# Crear un selector de año
ano_seleccionado = st.selectbox("Seleccione el año", options=df['Año'].unique())

# Filtrar el DataFrame según el año seleccionado
df_filtrado = df[df['Año'] == ano_seleccionado]

# Mostrar el DataFrame filtrado en la interfaz de usuario
st.subheader(f"Datos para el año {ano_seleccionado}")

# Opción para mostrar todos los valores
mostrar_todos = st.checkbox("Mostrar todos los valores")

# Mostrar los primeros 5 valores o todos según la selección del usuario
if mostrar_todos:
    ui.table(data=df_filtrado, maxHeight=300)
else:
    ui.table(data=df_filtrado.head(), maxHeight=300)



data = {
    'Proyecto/tesis/Resumen': ['Tesis', 'Proyecto', 'Trabajo de Investigacion', 'Tesis Maestria', 'Resumen', 'Ensayo Clinico', 'Tesis Doctoral', 'Tesis Especialidad'],
    'Cantidad': [174, 68, 64, 22, 7, 3, 2, 1]
}
# Crear el DataFrame
df1 = pd.DataFrame(data)

# Ordenar los datos por 'Cantidad' de mayor a menor
df1 = df1.sort_values(by='Cantidad', ascending=False)

# Obtener el orden de categorías
category_order = df1['Proyecto/tesis/Resumen'].tolist()

# Mostrar el gráfico basado en Proyecto/tesis/Resumen
st.subheader("Distribución de Proyecto/tesis/Resumen")
with card_container(key="chart2"):
    st.vega_lite_chart(df1, {
        'mark': {'type': 'bar', 'tooltip': True, 'fill': 'rgb(173, 250, 29)', 'cornerRadiusEnd': 4 },
        'encoding': {
            'x': {'field': 'Proyecto/tesis/Resumen', 'type': 'ordinal', 'axis': {'title': 'Proyecto/tesis/Resumen'}, 'sort': category_order},
            'y': {'field': 'Cantidad', 'type': 'quantitative', 'axis': {'title': 'Cantidad', 'grid': False}},
        },
    }, use_container_width=True)



# Calcular la cantidad para cada combinación única de 'Año' y 'Politica'
cantidad_por_ano_politica = df.groupby(['Año', 'Politica']).size().reset_index(name='Cantidad')

# Ordenar los datos por 'Año' y 'Cantidad'
cantidad_por_ano_politica = cantidad_por_ano_politica.sort_values(by=['Año', 'Cantidad'], ascending=[True, False])

# Obtener los años únicos
anos_unicos = cantidad_por_ano_politica['Año'].unique().tolist()

# Mostrar el gráfico de barras agrupadas
st.subheader("Temas Prioritarios")
with card_container(key="chart5"):
    st.vega_lite_chart(cantidad_por_ano_politica, {
        "mark": "bar",
        "encoding": {
            "x": {"field": "Año", "type": "ordinal", "title": "Año"},
            "y": {"field": "Cantidad", "type": "quantitative", "title": "Cantidad"},
            "color": {"field": "Politica", "type": "nominal", "title": "Politica"}
        },
    }, use_container_width=True)


## nube de palabras

import streamlit as st
import streamlit_shadcn_ui as ui

value = ui.tabs(options=['2019','2020','2021','2022','2023','2024'], default_value='2019', key="kanaries")

with ui.card(key="image"):
    if value == "2019":
        st.image("nube2019.png", caption="PyGWalker", use_column_width=True)
        ui.element("link_button", text=value + " Github",className="mt-2", key="btn2")
    elif value == "2024":
        st.image("nube2024.png", caption="PyGWalker", use_column_width=True)
        #ui.element("img", src="https://pub-8e7aa5bf51e049199c78b4bc744533f8.r2.dev/graphic-walker-banner.png", className="w-full")
        ui.element("link_button", text=value + " Github", url="https://github.com/Kanaries/graphic-walker", className="mt-2", key="btn2")
    elif value == '2020':
        st.image("nube2020.png",caption="PyGWalker", use_column_width=True )
        ui.element("link_button", text=value + " Github", url="https://github.com/Kanaries/pygwalker", className="mt-2", key="btn2")
    elif value == '2021':
        st.image("nube2021.png",caption="PyGWalker", use_column_width=True )
        ui.element("link_button", text=value + " Github", url="https://github.com/Kanaries/pygwalker", className="mt-2", key="btn2")
    elif value == '2022':
        st.image("nube2022.png",caption="PyGWalker", use_column_width=True )
        ui.element("link_button", text=value + " Github", url="https://github.com/Kanaries/pygwalker", className="mt-2", key="btn2")
    elif value == '2023':
        st.image("nube2023.png",caption="PyGWalker", use_column_width=True )
        ui.element("link_button", text=value + " Github", url="https://github.com/Kanaries/pygwalker", className="mt-2", key="btn2")

