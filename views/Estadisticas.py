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

# Renderizar la tabla
#st.write(ui.table)


