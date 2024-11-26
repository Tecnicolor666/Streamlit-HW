1. Pasos para ejecutar la aplicación de Streamlit en un entorno virtual (venv)
Crear el entorno virtual
Ejecuta el siguiente comando para crear un entorno virtual en el directorio actual:
python -m venv venv

2. Activar el entorno virtual
venv\Scripts\activate

3. Instalar las dependencias
Asegúrate de que tienes el archivo requirements.txt. Luego, instala las dependencias con:
pip install -r requirements.txt

La libreria que debe instalarse y estar en el txt es:
streamlit==1.26.0

4.Ejecutar la aplicación de Streamlit
Para iniciar la aplicación, usa:
streamlit run Stream.py

5. En caso de error al crear el ambiente virtual, tienes que activar la politica en PowerShell con el siguiente comando
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
