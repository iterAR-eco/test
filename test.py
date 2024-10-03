import streamlit as st
import pandas as pd
import os

# Archivo Excel donde se guardarán los datos
file_path = "datos_ingresados.xlsx"

# Crear archivo Excel si no existe
if not os.path.exists(file_path):
    df = pd.DataFrame(columns=["DNI", "Nombre", "Apellido"])
    df.to_excel(file_path, index=False)

# Título de la app
st.title("Registro de datos")

# Formulario para ingresar los datos
with st.form(key="formulario_registro"):
    dni = st.text_input("Ingrese su DNI")
    nombre = st.text_input("Ingrese su Nombre")
    apellido = st.text_input("Ingrese su Apellido")
    submit_button = st.form_submit_button("Guardar")

# Si se presiona el botón de guardar
if submit_button:
    # Leer el archivo Excel existente
    df = pd.read_excel(file_path)

    # Crear una nueva fila con los datos ingresados
    nueva_fila = {"DNI": dni, "Nombre": nombre, "Apellido": apellido}

    # Agregar la nueva fila al DataFrame
    df = df.append(nueva_fila, ignore_index=True)

    # Guardar el DataFrame actualizado en el archivo Excel
    df.to_excel(file_path, index=False)

    # Mostrar mensaje de agradecimiento
    st.success("Gracias por ingresar sus datos")

    # Mostrar los datos guardados
    st.write("Datos actuales en el archivo Excel:")
    st.dataframe(df)
