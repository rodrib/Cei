import streamlit as st

from forms.contact import contact_form


@st.experimental_dialog("Contact Me")
def show_contact_form():
     contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/comite-etica-logo.png", width=230)

with col2:
    st.title("Comite de Etica en Investigacion Provincial", anchor=False)
    st.write(
        "Promover, jerarquizar y regular la investigación para la salud como herramienta que aporte criterios de efectividad para la toma de decisiones en las políticas sanitarias de la Provincia."
    )
    if st.button("✉️ Contact Me"):
        pass#show_contact_form()


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("FUNCIONES", anchor=False)
st.write(
    """
    - Fijar prioridades para la investigación en salud en la provincia de Misiones.
    - Implementar un Registro de Investigadores e Investigaciones en la Provincia de Misiones de acuerdo al Registro Nacional de Investigaciones en Salud (RENIS).
    - Fortalecer las capacidades de investigación para la consolidación de los Sistemas Provinciales de Investigación en salud y del Sistema Nacional de Investigación para la Salud (SNIS).
    - Determinar las políticas rectoras de las actividades de investigación en la Provincia de Misiones.
    - Fortalecer la rectoría y gobernanza del Ministerio de Salud de la Provincia de Misiones en la investigación para la salud.
    - Promover la investigación en el ámbito de la provincia en las condiciones establecidas por las normativas vigentes.
    - Promover la formación de recursos humanos en el campo de la investigación en las ciencias de la salud.
    - Articular con organismos gubernamentales y no gubernamentales para la promoción y desarrollo de investigaciones en ciencias de la salud.
    """
)


# --- SKILLS ---
st.write("\n")
st.subheader("MIEMBROS", anchor=False)
st.write(
    """
    - Rodrigo Bogado (Rfeb)
    - Marcelo Gamarra (Chelo)
    - Cristina Martin 
    - Gaston Sioli 
    - Donovan Rivero 
    """
)