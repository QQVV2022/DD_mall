# qmall
e-commerce site (Vue + Django)
Frontend: vue.js
Backend: django, mysql, redis; celery

----------- dev process --------
1. Set up virtual env:
$pip install virtualenv

#python<version> -m venv <virtual-environment-name>
$mkdir projectA
$cd projectA
$python3.9 -m venv env

$source env/bin/activate
$deactivate


2. Get all related packages
$pip list
$pip freeze > requirements.txt
$pip install -r requirements.txt
