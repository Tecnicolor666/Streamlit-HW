import streamlit as st

# Título de la aplicación
st.title("Mi primera app con Streamlit")

# Formulario simple
st.header("Formulario")
nombre = st.text_input("¿Cuál es tu nombre?")
edad = st.number_input("¿Cuántos años tienes?", min_value=0, step=1)

if st.button("Enviar"):
    if nombre:
        st.success(f"Hola, {nombre}. Tienes {edad} años.")
    else:
        st.error("Por favor ingresa tu nombre.")
