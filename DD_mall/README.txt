e-commerce site (Vue + Django) Frontend: vue.js Backend: django, mysql, redis; celery
refer:
https://github.com/LondonAppDeveloper/deploy-django-with-docker-compose/tree/main
https://github.com/scalablescripts/python-microservices/tree/main

----------- dev process --------

Set up virtual env:
$pip install virtualenv #python -m venv
$mkdir projectA $cd projectA
$python3.9 -m venv env

$source env/bin/activate
$deactivate

Get all related packages
$pip list $pip freeze > requirements.txt
$pip install -r requirements.txt

Docker run:
$docker compose up
$docker stop dd_mall-db-1 dd_mall-backend-1
$docker rm dd_mall-db-1 dd_mall-backend-1
$docker rmi dd_mall-backend

$docker exec -it dd_mall-backend-1 sh
$docker exec -it dd_mall-db-1 /bin/bash

on mysql cotainer:
$mysql -u root -p qmall
on backend container:
$ mysql -P 3306 -h db --protocol=tcp -u root -p qmall
on mac:
$ mysql -P 33066 --protocol=tcp -u root -p qmall --ssl-mode=DISABLED

-------------init finish------------------------
