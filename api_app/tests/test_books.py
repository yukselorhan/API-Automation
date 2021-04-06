import falcon
from falcon import testing
import pytest

import uuid

import sys
sys.path.append('*/api_app/')

import api_app.src.app as app
from api_app.src.data import BOOKS

@pytest.fixture
def client():
    return testing.TestClient(app.api) #test clientı oluşturuyoruz api calları simule etmek için 

def test_get_books(client):
    expected = list(BOOKS)

    response = client.simulate_get('/books') #books uzantısında get requesti simule ediyor

    assert response.status == falcon.HTTP_OK  
    assert response.json == expected  #dönen sonuç ile beklediğimi sonuçu kontrol ediyor, beklediğim sonuç dataki books
    assert len(response.json) == 0 #hiç kitap olmadıgını kontrol ediyor varsa testi patlatıyor


def test_put_book_invalid_request(client):
    new_book = {
        
    }

    response = client.simulate_put('/book', json=new_book)
    assert response.status == falcon.HTTP_BAD_REQUEST #author ile title parametrelerini göndermediğim için bad request dönmesi lazım, dönmezse patlat
    assert response.json['error'] == "Fields 'author' and 'title' are required" #dönen jsondaki error fieldı buna eşit değilse testi patlatır


def test_put_book_empty_field(client): 
    new_book = {
        "author": "Jack Nicholson",
        "title": ""
    }

    response = client.simulate_put('/book', json=new_book)
    assert response.status == falcon.HTTP_BAD_REQUEST 
    assert response.json['error'] == "Field 'title' cannot be empty"


def test_put_id_field(client): 
    new_book = {
        "author": "John Smith",
        "title": "Reliability of late night deployments",
        "id": "139"
    }

    response = client.simulate_put('/book', json=new_book)
    assert response.status == falcon.HTTP_404 
   

def test_put_book(client):
    new_book = {
        "author": "John Smith",
        "title": "SRE 101"
    }

    response = client.simulate_put('/book', json=new_book)
    assert response.status == falcon.HTTP_CREATED
    new_book["id"] = response.json['id']
    assert response.json == new_book

    response = client.simulate_get(f'/book/{new_book["id"]}')
    assert response.status == falcon.HTTP_OK
    assert response.json == new_book


def test_put_existing_book(client):
    new_book = {
        "author": "John Smith",
        "title": "SRE 101"
    }

    response = client.simulate_put('/book', json=new_book)
    assert response.status == falcon.HTTP_OK
    assert response.json['error'] == "Another book with similar title and author already exists."
