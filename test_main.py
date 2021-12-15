from fastapi.testclient import TestClient

from main import app
from habi import connect_database

client = TestClient(app)


def test_connect():
        try:
            connect_database()
        except Exception as e:
            print(e)

def test_get_property():
    response = client.get('http://127.0.0.1:8089/property/')
    assert  'results' in response.json()
    
    
    