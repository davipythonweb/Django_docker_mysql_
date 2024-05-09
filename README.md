# Django_docker_mysql_

* Banco MySQL em nuvem com container Docker.(configuração simples.) 
* video 1 com tutorial deste projeto==>
'https://www.youtube.com/watch?v=WtdefC1WJgE' 
* video 2 =>
'https://www.youtube.com/watch?v=bldOLqAAqos'

#### criar environment => python -m venv venv
#### ativar venv => source venv/bin/activate
#### instalar => pip install django
#### instalar => pip install mysqlclient

#### criar arquivos 
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
