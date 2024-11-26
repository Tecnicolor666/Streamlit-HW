# Ejemplo con StreamLit

Este repositorio contiene un ejemplo de aplicación web utilizando [Streamlit](https://streamlit.io/), una librería en Python para desarrollar aplicaciones web dinámicas de manera sencilla.

## Pasos para ejecutar la aplicación web

1. Crear el entorno virtual

Ejecuta el siguiente comando para crear un entorno virtual en el directorio actual:

```console
python -m venv venv
```

2. Activar el entorno virtual

```console
venv\Scripts\activate
```

NOTA: En `PowerShell` activa la politica de ejección de scripts con el siguiente comando

```console
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypas
```

3. Instalar las dependencias

Instala las dependencias de Python con:

```console
pip install -r requirements.txt
```

4. Ejecutar la aplicación de Streamlit

Para iniciar la aplicación, usa:

```console
streamlit run Stream.py
```

5. Abre un navegador y abre la dirección: http://localhost:8080
