# Users & Skills

Appweb desarrolada en python con el framework DJANGO.

## Introduccion
	
La app esta orientada al area de Recursos Humanos de cualquier empresa de Software, tiene por objetivo facilitar la toma de decision
de los candidatos que se postularon a un puesto de trabajo ofrecido, llevar un historial del perfil y a futuro, medir el rendimiento y performance del empleado contratado. Consiste en evaluar las habilidades tecnicas y analiticas, mediante una serie de pruebas con respecto al lenguaje de programacion en la cual se especializa.

## Requisitos 

Ejecutar el siguiente comando en la terminal:

pip install -r requirements.txt

## Instalacion

1. Descargar repo mediante el comando "git clone https://github.com/df2017/userskills.git".

2. Luego ejecuta los "Requisitos".

3. Con respecto al archivo settings.py, deben crear en el mismo directorio del archivo mencionado, un archivo llamado ".env", en el mismo    deben configurar sus variables de entorno por seguridad al proyecto en produccion.

4. Luego deben crear la carpeta db para guardar el archivo de la base de datos.

5. Para finalizar ejecutar los siguientes comandos en la consola:
	"python manage.py makemigrations"
	"python manage.py migrate"
	"python manage.py createsuperuser"
	"python manage.py runserver"
