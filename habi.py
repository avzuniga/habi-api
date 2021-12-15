from sql_connect import create_server_connection, create_database, execute_query, read_query
import json


"Creamos la conexion con la Base de datos"


def connect_database():
    connection = create_server_connection(
        "3.130.126.210", "pruebas", "VGbt3Day5R", 3309)
    query = "USE habi_db"
    execute_query(connection, query)
    return connection


def read_status(connection, status):
    "Obtengo los tipos de estados de las propiedades"
    query = 'SELECT * FROM status'
    results = read_query(connection, query)
    for r in results:
        if r[1] == status:
            status = r[0]
    return status


def filter_by_city(city, connection):
    query = f'SELECT * FROM property WHERE city LIKE "{city}"'

    "Tengo todas las propiedades filtradas por ciudad"
    results = read_query(connection, query)
    return results


def filter_by_year(year, connection):
    query = f'SELECT * FROM property WHERE year LIKE {year}'

    "Tengo todas las propiedades filtradas por año"
    results = read_query(connection, query)
    return results


def filter_by_city_and_year(city, year, connection):
    query = f'SELECT * FROM property WHERE city LIKE "{city}" AND year LIKE {year}'

    "Tengo todas las propiedades filtradas por ciudad y año"
    results = read_query(connection, query)
    return results


def filter_by_status(results, status, connection):
    "Tengo todas las propiedades filtradas por status"
    response = []
    for r in results:
        id = r[0]
        print(id)
        query = f'SELECT * FROM status_history WHERE property_id = {id}'
        results_ = read_query(connection, query)
        if len(results_) > 0:
            print(results_[-1])
            if results_[-1][2] == status:
                response.append(r)
    return response


def get_all_properties(connection):
    "Tengo todas las propiedades"
    query = f'SELECT * FROM property'
    results = read_query(connection, query)
    return results
