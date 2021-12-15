from fastapi import FastAPI
from habi import *
from typing import Optional


app = FastAPI()

@app.get("/property/")
def read_properties(city: Optional[str] = None, year: Optional[int] = None, status: Optional[str] = None):
    connection = connect_database()
    status = read_status(connection, status)
    results = []

    if city and year and status:
        results = filter_by_city_and_year(city, year, connection)
        results = filter_by_status(results, status, connection)
    elif city and year == None and status == None:
        results = filter_by_city(city, connection)
    elif year and city == None and status == None:
        results = filter_by_year(year, connection)
    elif year and city and status == None:
        results = filter_by_city_and_year(city, year, connection)
    elif year and status and city == None:
        results = filter_by_year(year, connection)
        results = filter_by_status(results, status, connection)
    elif city and status and year == None:
        results = filter_by_city(city, connection)
        results = filter_by_status(results, status, connection)
    elif year == None and city == None and status:
        query = f'SELECT * FROM property'
        results = read_query(connection, query)
        results = filter_by_status(results, status, connection)
    elif year == None and status == None and city == None:
        results = get_all_properties(connection)
    return {"results": results}

