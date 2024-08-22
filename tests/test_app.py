import pytest
from app import create_app, db
from models.produtor_models import Produtor

@pytest.fixture
def client():

    test_config = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }

    app = create_app(test_config=test_config)
    app.config['TESTING'] = True
  
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"message": "Hello word!"}

def test_add_produtor(client):
    response = client.post('/produtores', json={
        'cpf_cnpj': '12345678909',
        'nome_produtor': 'João da Silva',
        'nome_fazenda': 'Fazenda Boa Vista',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'area_total': 100.0,
        'area_agricultavel': 50.0,
        'area_vegetacao': 20.0,
        'culturas': 'Soja'
    })
    assert response.status_code == 201
    data = response.json
    assert data['nome_produtor'] == 'João da Silva'

def test_update_produtor(client):
    # Primeiro, adicione um produtor para atualizar
    client.post('/produtores', json={
        'cpf_cnpj': '12345678909',
        'nome_produtor': 'João da Silva',
        'nome_fazenda': 'Fazenda Boa Vista',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'area_total': 100.0,
        'area_agricultavel': 50.0,
        'area_vegetacao': 20.0,
        'culturas': 'Soja'
    })

    # Atualizar o produtor existente
    response = client.put('/produtores/1', json={
        'nome_produtor': 'João da Silva Atualizado'
    })
    assert response.status_code == 200
    data = response.json
    assert data['nome_produtor'] == 'João da Silva Atualizado'

def test_delete_produtor(client):
    # Primeiro, adicione um produtor para deletar
    client.post('/produtores', json={
        'cpf_cnpj': '12345678909',
        'nome_produtor': 'João da Silva',
        'nome_fazenda': 'Fazenda Boa Vista',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'area_total': 100.0,
        'area_agricultavel': 50.0,
        'area_vegetacao': 20.0,
        'culturas': 'Soja'
    })

    # Deletar o produtor existente
    response = client.delete('/produtores/1')
    assert response.status_code == 204

    # Verificar se o produtor foi realmente deletado
    response = client.get('/produtor/1')
    assert response.status_code == 404
