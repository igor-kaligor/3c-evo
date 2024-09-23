import pytest
from app import app, db


data_test = {
        "value": "+55 84 91234-4321",
        "monthyPrice": 0.03,
        "setupPrice": 3.40,
        "currency": "U$"
    }

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()


def test_create_object(client):
    response = client.post('/api/numbers', json=data_test)
    assert response.status_code == 201
    assert response.json['message'] == "Number created"

def test_get_objects(client):

    [client.post('/api/numbers', json=data_test) for _ in range(15)]
    response = client.get('/api/numbers')
    assert response.status_code == 200
    print(response.json)
    # assert len(response.json) == 1

def test_get_object(client):
    client.post('/api/numbers', json=data_test)
    response = client.get('/api/numbers/1')
    assert response.status_code == 200
    assert response.json['value'] == "+55 84 91234-4321"

def test_update_object(client):
    client.post('/api/numbers', json=data_test)
    response = client.put('/api/numbers/1', json={
        "value": "+55 84 91234-4322",
        "monthyPrice": 0.04, #New value
        "setupPrice": 3.50, #New value
        "currency": "U$"
    })
    assert response.status_code == 200
    assert response.json['message'] == "Number updated"

def test_delete_object(client):
    client.post('/api/numbers', json=data_test)
    response = client.delete('/api/numbers/1')
    assert response.status_code == 200
    assert response.json['message'] == "Number deleted"