
[View in English](https://github.com/rubensantibanezacosta/Odoo-Ocio-Open-Crud/blob/main/docs/EnglishReadme.md)

# Ocio Open Odoo Crud  *(Proyecto formativo)*

Repositorio del modulo personalizado en Odoo 14.

El proyecto consta de los Crud para gestionar eventos, carga de imagenes mediante "Url", y añade campos y funcionalidades propias de Odoo 14. Se trata de una simulación de un posible Crud que gestione la base de datos del proyecto [Ocio Open](https://github.com/rubensantibanezacosta/Ocio_Open)



## Documentación del Proyecto

- [Informe de requisitos de la aplicación](https://github.com/rubensantibanezacosta/Odoo-Ocio-Open-Crud/blob/main/docs/Requisitos.md)

## Comenzando

Link de descarga:

Desde Github: https://github.com/rubensantibanezacosta/Odoo-Ocio-Open-Crud


## Prerequisitos

Necesitas un entorno de desarrollo con:
* [Sistema operativo linux](https://www.linux.org/).
* [Git](https://git-scm.com) -  https://git-scm.com/downloads.
* [Docker](https://www.docker.com/) - https://www.docker.com/products/docker-desktop.
* [Python](https://www.python.org/downloads/) -  https://www.python.org/downloads/.

## Instrucciones de instalación

Descargue el contenedor oficial de Odoo 14 y el contenedor oficial de PostgreSQL
[Guía oficial](https://hub.docker.com/_/odoo)

```
docker pull odoo
docker pull postgres
```

Cree el archivo ```docker-compose.yml```

```
version: '3.1'
services:
  web:
    image: odoo:14.0
    depends_on:
      - db
    ports:
      - "8069:8069"
    volumes:
      - odoo-web-data-copy:/var/lib/odoo
      - odoo-web-config:/etc/odoo
      - ./extra-addons:/mnt/extra-addons
  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_PASSWORD=odoo
      - POSTGRES_USER=odoo
      - PGDATA=/var/lib/postgresql/data/pgdata
    ports:
      - "5432:5432"
    volumes:
     - odoo-db-data-copy:/var/lib/postgresql/data/pgdata
volumes:
  odoo-web-data-copy:
  odoo-db-data-copy:
  odoo-web-config:
```


Arranque su docker-compose:

```
docker-compose up
```

Clone el repositorio en su carpeta Extra-addons:

```
git clone https://github.com/rubensantibanezacosta/Odoo-Ocio-Open-Crud
```
Deberá renombrar la carpeta que contiene la aplicación con el nombre "ocio__open"

Abra su nagegador el la dirección http://localhost:8069/


En el buscador de Aplicaciones busque la aplicación, e instálela.

![Captura de pantalla de 2021-12-05 18-38-52](https://user-images.githubusercontent.com/44450566/144759333-3de71503-c178-4413-94a1-a3b2db833b70.png)



## Probando el módulo

Para poder visualizar y utilizar en nuevo módulo, deberá proporcionar permisos al usuario.

![Captura de pantalla de 2021-12-05 18-47-10](https://user-images.githubusercontent.com/44450566/144759448-9b8ec65f-894c-404d-9bb0-87425af88b47.png)


Marque la casilla de Ocio Open Gestor, u Ocio Open operario, segun sus necesidades.

Pulse la tecla *f5* para actualizar la caché, y ya dispondra de las funcionalidades del módulo.

Tendrá nuevos campos en el formulario de usuarios:

![Captura de pantalla de 2021-12-05 18-48-51](https://user-images.githubusercontent.com/44450566/144759557-0301b2aa-7ecb-452d-afe0-d28468cfd13e.png)

Tendrá disponible en el menú la aplicación Ocio Open.

![Captura de pantalla de 2021-12-05 18-51-26](https://user-images.githubusercontent.com/44450566/144759606-11d09f07-b1d1-4f49-80db-77828b1df1a8.png)

Para crear nuevos eventos, debera primero cargar imágenes simplemente registrando la url en el campo correspondiente, y Odoo descargará y le mostrará la imagen.

![Captura de pantalla de 2021-12-05 18-53-48](https://user-images.githubusercontent.com/44450566/144759658-f29ac470-d557-4293-93a1-62e4b793c973.png)

Ahora podra crear un evento, y una vez creado, tendra una sección de comentarios en cada evento.

![Captura de pantalla de 2021-12-05 18-55-05](https://user-images.githubusercontent.com/44450566/144759700-cc1c6761-8d5a-4543-acad-b8d89a350769.png)


Disfrute!!


