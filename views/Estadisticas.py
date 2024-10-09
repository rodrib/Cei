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