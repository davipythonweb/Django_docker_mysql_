# Django_docker_mysql_


#### instalar => pip install mysqlclient

<!-- criar arquivos -->
- data.sql
- docker-compose.yml
- Dockerfile

`docker-compose build`

`docker-compose up`

`docker-compose up -d`
- verificar containers
`docker compose ps -a`

- listar as informaçoes do container
`docker container ls`

- abrir um shell na maquina virtual do container docker
* docker exec -it (id do container) /bin/bash

- para acessar o terminal mysql
`mysql -ppass -uroot`

- comandos mysql
`show tables;`
`show databases;`
`use my_database;`


`django createsuperuser (name)`
`Admin$50001`
`admin`