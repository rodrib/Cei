

import streamlit as st

# original_title = '<h1 style="font-family: serif; color:white; font-size: 20px;">Comite de Etica Provincial✨ </h1>'
# st.markdown(original_title, unsafe_allow_html=True)


# # Set the background image
# background_image = """
# <style>
# [data-testid="stAppViewContainer"] > .main {
#     background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
#     background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
#     background-position: center;  
#     background-repeat: no-repeat;
# }
# </style>
# """

# st.markdown(background_image, unsafe_allow_html=True)

# st.text_input("", placeholder="Streamlit CSS ")

# input_style = """
# <style>
# input[type="text"] {
#     background-color: transparent;
#     color: #a19eae;  // This changes the text color inside the input box
# }
# div[data-baseweb="base-input"] {
#     background-color: transparent !important;
# }
# [data-testid="stAppViewContainer"] {
#     background-color: transparent !important;
# }
# </style>
# """
# st.markdown(input_style, unsafe_allow_html=True)


# Page title
st.set_page_config(page_title='CEI', page_icon='📊',
                   layout="wide", # Forma de layout ancho o compacto
                    initial_sidebar_state="expanded" # Definimos si el sidebar aparece expandido o colapsado
                   )
st.title('📊 Comite de Etica Provincial: Documentos')



st.header("Directores e Investigadores")

mensaje = """
El Circuito de presentación de Planes de Trabajos de Investigación en los que participan personas humanas se ha modificado debido a la incorporación al sistema de una Herramienta online para la presentación, seguimiento y evaluación de los mismos denominada AiSalud_PLatform.

En el siguiente link encontrarán la información correspondiente así como direcciones para plantear dudas en relación al uso de la mencionada Plataforma o a otras en relación a las investigaciones.

Por otra parte, debido a la versatilidad de la misma, recomendamos que soliciten la carga de Planes de Proyectos ya iniciados o finalizados ya que esto permitirá ver en todo momento la producción en investigaciones en salud humana de su equipo de trabajo y, asimismo, nos permitirá ampliar la base de datos en relación a las líneas que se investigan en nuestra provincia y, al finalizar cada año, premiar a los mejores trabajos seleccionados desde el Formulario de presentación de Informes anuales que figura en la mencionada Plataforma.
"""

st.markdown(mensaje)


st.header("Normativa y Documentacion")

with st.expander("1- Resolución 1480/11"):
    st.write("[Enlace a la resolución](https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-1480-2011-187206)")
    st.write("""
    APRUEBASE LA GUIA PARA INVESTIGACIONES CON SERES HUMANOS. OBJETIVOS. DEROGASE LA RESOLUCION DEL MINISTERIO DE SALUD N° 1490 DEL 14 DE NOVIEMBRE DE 2007 QUE APROBABA LA GUIA DE LAS BUENAS PRACTICAS DE INVESTIGACION CLINICA EN SERES HUMANOS, LA CUAL SE REEMPLAZA POR LA GUIA PARA INVESTIGACIONES CON SERES HUMANOS APROBADA POR EL ARTICULO 1° DE LA PRESENTE RESOLUCION. DEROGASE LA RESOLUCION DEL MINISTERIO DE SALUD N° 102 DEL 2 DE FEBRERO DE 2009 QUE CREABA EL REGISTRO DE ENSAYOS CLINICOS EN SERES HUMANOS, EL CUAL SE REEMPLAZA POR EL REGISTRO NACIONAL DE INVESTIGACIONES EN SALUD CREADO POR EL ARTICULO 2° DE LA PRESENTE RESOLUCION.
    """)


# Disposición 6677/10 de ANMAT
with st.expander("2- Disposición 6677/10 de ANMAT"):
    st.write("[Enlace a la disposición](https://www.argentina.gob.ar/normativa/nacional/disposici%C3%B3n-6677-2010-174557)")
    st.write("""
    APRUEBASE EL REGIMEN DE BUENA PRACTICA CLINICA PARA ESTUDIOS DE FARMACOLOGIA CLINICA. DEROGANSE LAS DISPOSICIONES A.N.M.A.T. NROS. 5330/97, 3436/98, 3112/00, 690/05, 1067/08 Y 6550/08.
    """)

