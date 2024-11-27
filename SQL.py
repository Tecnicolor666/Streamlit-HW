import sqlite3
import streamlit as st

# Configuración de la base de datos
def init_db():
    conn = sqlite3.connect("usuarios.db")  # Nombre del archivo de base de datos
    cursor = conn.cursor()
    # Crear tabla si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insertar_usuario(nombre, edad):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conn.commit()
    conn.close()

def obtener_usuarios():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

# Inicializar la base de datos
init_db()

# Interfaz de la aplicación
st.title("Mi primera app con Streamlit y base de datos")

# Formulario simple
st.header("Formulario")
nombre = st.text_input("¿Cuál es tu nombre?")
edad = st.number_input("¿Cuántos años tienes?", min_value=0, step=1)

if st.button("Enviar"):
    if nombre:
        insertar_usuario(nombre, edad)
        st.success(f"Hola, {nombre}. Tienes {edad} años. Tu información ha sido guardada.")
    else:
        st.error("Por favor ingresa tu nombre.")

# Mostrar usuarios registrados
st.header("Usuarios registrados")
usuarios = obtener_usuarios()
if usuarios:
    for usuario in usuarios:
        st.write(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Edad: {usuario[2]}")
else:
    st.info("No hay usuarios registrados.")
