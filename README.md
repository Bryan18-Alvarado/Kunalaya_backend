<p align="center">
  <img src="logo.png" width="503" alt="kunalaya-logo" />
</p>

# Kunalaya
App para la preservacion de nuestras historias y tradiciones

Este repositorio funciona como su nombre lo indica como backend de kunalaya app

Se procedera con los requisitos para ponerlo en marcha y verificar sus funcionalidades

## Requerimientos:
- Lenguaje: Python 3.13.7
- Base de datos: Postgresql 17.5

Estas dos herramientas son las principales que dan forma a nuestro proyecto, si no se
poseen estas herramientas aqui se les facilita su descarga desde sus sitios oficiales

- [python](https://www.python.org/)
- [postgresql](https://www.postgresql.org/)

Ya teniendolos solo falta clonar el repositorio 

```bash
  git clone https://github.com/Bryan18-Alvarado/Kunalaya_backend
```

## Instalacion
Ya teniendo el repositorio se procede en la instalacion de todo sus componentes,

#### Creacion del entorno de desarrollo
Trabajando con python se debe de aislar el proyecto y todas sus dependencias de nuestras computadora, evitando asi que afecte otros proyectos en los que este trabajando, con los comandos de python debe de realizarlo de la siguiente manera:

``` bash
$ python -m venv "nombre-del-entorno"
```

Para activarlo varia segun el sistema operativo

#### Linux
``` bash
$ source "nombre-del-entorno"/bin/activate
```

#### Windows
``` powershell
"nombre-del-entorno"\Scripts\activate
```

## Dependencias
Se procede a la instalacion de las dependencias las cuales estan en el archivo "requirements.txt" el cual se debe de instalar con pip:

```bash
$ pip install -r requirements.txt
```

## Base de datos
El proyecto utiliza postgresql como base de datos, se ha dejado un template de como debe de ser el archivo "db_settings.py", debe de crear el archivo con la estructura mostrada

```bash
DB = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': '',
    'USER': '',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '5432'
  }
}
```

Ya configurado el db_settings se procede a hacer las migraciones de los modelos a postgres con los siguientes comandos:

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

Ya realizada las migraciones se esta listo para correr el servidor con el comando runserver

```bash
$ python manage.py runserver 0.0.0.0:8000
```

Habiendo hecho todo esto se esta listo el montaje del backend y pasar al [frontend](https://github.com/Bryan18-Alvarado/Kunalaya_frontend)