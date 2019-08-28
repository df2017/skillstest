# Users & Skills
Introduccion

La app consiste en evaluar las habilidades tecnicas de un programador, mediante una serie de pruebas con respecto al lenguaje de programacion en la cual se especializa.

Tutorial puesta en marcha.

1 - Descargar repo mediante el comando "git clone https://github.com/df2017/skillstest.git".
2 - Con respecto al archivo settings.py, deben crear en el mismo directorio del archivo mencionado, un archivo llamado ".env", en el mismo deben configurar sus variables de entorno por seguridad al proyecto en produccion.
3 - Luego deben crear la carpeta db para guardar el archivo de la base de datos.
4 - Para finalizar ejecutar los siguientes comandos en la consola:
    "python manage.py makemigrations"
    "python manage.py migrate"
    "python manage.py createsuperuser"
    "python manage.py runserver"
