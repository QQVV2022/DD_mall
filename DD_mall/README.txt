e-commerce site (Vue + Django) Frontend: vue.js Backend: django, mysql, redis; celery

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
$doker rmi dd_mall-backend