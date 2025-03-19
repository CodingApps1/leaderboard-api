import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_add_user(client):
    response = client.post('/api/users', json={
        'name': 'Alice', 
        'age': 25, 
        'address': '456 Park Ave'
    })
    assert response.status_code == 201
    assert response.json['name'] == 'Alice'
