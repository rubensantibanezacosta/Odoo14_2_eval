


# Ocio Open Odoo Crud 2º evaluación  *(Proyecto formativo)*

Repositorio del modulo personalizado en Odoo 14.

El proyecto consta de los Crud para gestionar eventos, carga de imagenes mediante "Url", y añade campos y funcionalidades propias de Odoo 14. Se trata de una simulación de un posible Crud que gestione la base de datos del proyecto [Ocio Open](https://github.com/rubensantibanezacosta/Ocio_Open)



## Documentación del Proyecto

- [Informe de requisitos de la aplicación](https://github.com/rubensantibanezacosta/Odoo14_2_eval/blob/main/ocio__open/docs/Requisitos.md)

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
Deberá extraer las carpetas que contiene el repositorio directamente en su carpeta extra-addons.

Abra su nagegador el la dirección http://localhost:8069/


En el buscador de Aplicaciones busque la aplicación ocio_open, incidencias, digital sign, web responsive, y reports whith trademark, qr generator, e instálelas en el mismo orden.

![Captura de pantalla de 2021-12-05 18-38-52](https://user-images.githubusercontent.com/44450566/144759333-3de71503-c178-4413-94a1-a3b2db833b70.png)



## Probando el módulo

Para poder visualizar y utilizar en nuevo módulo, deberá proporcionar permisos al usuario.

![Captura de pantalla de 2021-12-05 18-47-10](https://user-images.githubusercontent.com/44450566/144759448-9b8ec65f-894c-404d-9bb0-87425af88b47.png)


Marque la casilla de Ocio Open Gestor, u Ocio Open operario, segun sus necesidades.

Es posible que deba acceder al modulo desde el modo desarrolador, para añadir el grupo de administracion/técnico a los modulos de ocio__open.

Pulse la tecla *f5* para actualizar la caché, y ya dispondra de las funcionalidades del módulo.

Tendrá nuevos campos en el formulario de usuarios:

![Captura de pantalla de 2021-12-05 18-48-51](https://user-images.githubusercontent.com/44450566/144759557-0301b2aa-7ecb-452d-afe0-d28468cfd13e.png)

Si marca su casilla Modo oscuro, su tema varíará, aunque debido a las limitaciones de Odoo el modo oscuro no funcionará como se espera.

![Captura de pantalla de 2022-02-27 19-27-31](https://user-images.githubusercontent.com/44450566/155896999-7e0e05f2-08e5-45a4-bc6d-b4b750b371e4.png)


Tendrá disponible en el menú la aplicación Ocio Open.

![Captura de pantalla de 2021-12-05 18-51-26](https://user-images.githubusercontent.com/44450566/144759606-11d09f07-b1d1-4f49-80db-77828b1df1a8.png)

Para crear nuevos eventos, debera primero cargar imágenes simplemente registrando la url en el campo correspondiente, y Odoo descargará y le mostrará la imagen.

![Captura de pantalla de 2021-12-05 18-53-48](https://user-images.githubusercontent.com/44450566/144759658-f29ac470-d557-4293-93a1-62e4b793c973.png)

Ahora podra crear un evento, y una vez creado, tendra una sección de comentarios en cada evento.

![Captura de pantalla de 2021-12-05 18-55-05](https://user-images.githubusercontent.com/44450566/144759700-cc1c6761-8d5a-4543-acad-b8d89a350769.png)

Podra imprimir informes de sus eventos:

![Captura de pantalla de 2022-02-27 19-37-25](https://user-images.githubusercontent.com/44450566/155897068-0140788e-8820-41b5-9162-9d337b6f09fb.png)

Podra generar códigos QR a traves de una mini aplicación situada junto a las notificaciones:

![Captura de pantalla de 2022-03-01 15-05-34](https://user-images.githubusercontent.com/44450566/156194195-a6a41fd1-55c0-41fd-ad1f-89756aea2f80.png)


Debido a las aplicaciones de terceros que se han instalado, su aplicación sera adaptable a resoluciones móviles, dispondra de un campo para registrar la firma de sus usuarios, y se añadira una marca de agua a sus informes.

![Captura de pantalla de 2022-02-27 19-36-28](https://user-images.githubusercontent.com/44450566/155897039-c9a890ce-499a-49a5-8f61-171d300e289b.png)

![Captura de pantalla de 2022-02-27 19-38-51](https://user-images.githubusercontent.com/44450566/155897128-284bac3c-94ef-477f-9332-676f6fe3830d.png)



Disfrute!!
