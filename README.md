
To run:

create env

clone the project

cd project folder

pip install -r requirements.txt

uvicorn main:app --port 8089 --reload

Then go to http://127.0.0.1:8089/docs

Execute GET http://127.0.0.1:8089/property/ without parameters return all the properties

GET  receive     year - city  - status   All are optional parameters. U can filter by zero or more parameters togueters.

Example:
http://127.0.0.1:8089/property/?city=bogota&year=2000&status=pre_venta

Response:
{"results":[[1,"calle 23 #45-67","bogota",120000000,"Hermoso apartamento en el centro de la ciudad",2000]]}




Dudas al inicio:

Nombre de las tablas 

Respuesta:

status_history

property

status






