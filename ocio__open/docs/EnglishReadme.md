
[Ver en Castellano](https://github.com/rubensantibanezacosta/Odoo-Ocio-Open-Crud)

# Ocio Open Odoo Crud  *(Training project)*

Repository of the custom module in Odoo 14.


The project consists of the Crud to manage events, load images through "Url", and adds fields and functionalities of Odoo 14. It is a simulation of a possible Crud that manages the project [Ocio Open](https://github.com/rubensantibanezacosta/Ocio_Open) database.



## Project Documentation

- [Application requirements report](https://github.com/rubensantibanezacosta/Odoo-Ocio-Open-Crud/blob/main/docs/Requisites.md)

## Starting

Download Links:

From Github: https://github.com/rubensantibanezacosta/Odoo-Ocio-Open-Crud

## Prerequisites

Necesitas un entorno de desarrollo con:
* [Linux SO](https://www.linux.org/).
* [Git](https://git-scm.com) -  https://git-scm.com/downloads.
* [Docker](https://www.docker.com/) - https://www.docker.com/products/docker-desktop.
* [Python](https://www.python.org/downloads/) -  https://www.python.org/downloads/.

## Setup guide

Download the official Odoo 14 container and the official PostgreSQL container
[Official guide](https://hub.docker.com/_/odoo)

```
docker pull odoo
docker pull postgres
```

Create the file ```docker-compose.yml```

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


Boot your docker-compose:

```
docker-compose up
```

Clone the repository into your Extra-addons folder:

```
git clone https://github.com/rubensantibanezacosta/Odoo-Ocio-Open-Crud
```

Open your browser at the address http://localhost:8069/


In the Applications search engine find the application, and install it.

![Captura de pantalla de 2021-12-05 18-38-52](https://user-images.githubusercontent.com/44450566/144759333-3de71503-c178-4413-94a1-a3b2db833b70.png)



## Testing the module

In order to view and use the new module, you must provide permissions to the user.

![Captura de pantalla de 2021-12-05 18-47-10](https://user-images.githubusercontent.com/44450566/144759448-9b8ec65f-894c-404d-9bb0-87425af88b47.png)


Check the box for Ocio Open Manager, or Ocio Open Operator, according to your needs.

Press the * f5 * key to update the cache, and you will have the module's functionalities.

You will have new fields in the user form:

![Captura de pantalla de 2021-12-05 18-48-51](https://user-images.githubusercontent.com/44450566/144759557-0301b2aa-7ecb-452d-afe0-d28468cfd13e.png)

The Ocio Open application will be available in the menu.

![Captura de pantalla de 2021-12-05 18-51-26](https://user-images.githubusercontent.com/44450566/144759606-11d09f07-b1d1-4f49-80db-77828b1df1a8.png)

To create new events, you must first upload images by simply registering the url in the corresponding field, and Odoo will download and show you the image.

![Captura de pantalla de 2021-12-05 18-53-48](https://user-images.githubusercontent.com/44450566/144759658-f29ac470-d557-4293-93a1-62e4b793c973.png)

Now you can create an event, and once created, you will have a comment section on each event.

![Captura de pantalla de 2021-12-05 18-55-05](https://user-images.githubusercontent.com/44450566/144759700-cc1c6761-8d5a-4543-acad-b8d89a350769.png)


Enjoy!!
