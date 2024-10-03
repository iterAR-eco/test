import streamlit as st
import pandas as pd
import os
from git import Repo

# Archivo Excel donde se guardarán los datos
file_path = "datos_ingresados.xlsx"

# Clonar el repositorio en el que quieres guardar el archivo
repo_dir = "/ruta/local/repo"
if not os.path.exists(repo_dir):
    repo_url = "https://github.com/iterAR-eco/test"
    Repo.clone_from(repo_url, repo_dir)

repo = Repo(repo_dir)
file_path = os.path.join(repo_dir, "datos_ingresados.xlsx")

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

    # Crear un DataFrame con la nueva fila de datos ingresados
    nueva_fila = pd.DataFrame({"DNI": [dni], "Nombre": [nombre], "Apellido": [apellido]})

    # Concatenar el nuevo DataFrame con el existente
    df = pd.concat([df, nueva_fila], ignore_index=True)

    # Guardar el DataFrame actualizado en el archivo Excel
    df.to_excel(file_path, index=False)

    # Agregar y hacer commit al repositorio
    repo.git.add(file_path)
    repo.git.commit('-m', 'Datos actualizados')
    repo.git.push()

    # Mostrar mensaje de agradecimiento
    st.success("Gracias por ingresar sus datos")
