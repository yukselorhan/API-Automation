import uuid
import falcon
from falcon.media.validators import jsonschema
from .schemas import book

from .data import BOOKS
from .hooks import  validate_uuid


class Books(object):
    def __init__(self):
        self.books = BOOKS  #Datadaki booksu alıp buraya koyuyor

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  #hiçbir sorun yoksa 200 dönmesini tanımlıyoruz
        resp.media = self.books
       
class Book(object):
    def __init__(self):
        self.books = BOOKS

    def on_get(self, req, resp, book_id):
        try:
            requested_book = [book for book in self.books if book['id'] == book_id][0]
        except IndexError:
            resp.status = falcon.HTTP_NOT_FOUND  #gönderilen id ile bookstaki kitaplar arasında match yoksa hata alcak burada o hatayı handle ediyoruz
        else:
            resp.status = falcon.HTTP_200
            resp.media = requested_book  

    def on_put(self, req, resp):
        new_book = req.media

        if  "id" in new_book:  #gönderilen kitapların için id fieldı varsa 404 dön
            resp.status = falcon.HTTP_404
        elif "author" not in new_book and "title" not in new_book:
            resp.media = {"error": "Fields 'author' and 'title' are required"}
            resp.status = falcon.HTTP_BAD_REQUEST
        elif "author" not in new_book :
            resp.media = {"error": "Field 'author' is a required"}
            resp.status = falcon.HTTP_BAD_REQUEST
        elif "title" not in new_book:
            resp.media = {"error": "Field 'title' is a required"}
            resp.status = falcon.HTTP_BAD_REQUEST
        elif len(new_book["author"]) == 0 and len(new_book["title"])== 0:    
            resp.media = {"error": "Fields 'author' and 'title' cannot be empty"}
            resp.status = falcon.HTTP_BAD_REQUEST
        elif len(new_book["author"]) == 0:
            resp.media = {"error": "Field 'author' cannot be empty"}
            resp.status = falcon.HTTP_BAD_REQUEST
        elif len(new_book["title"]) == 0:
            resp.media = {"error": "Field 'title' cannot be empty"}
            resp.status = falcon.HTTP_BAD_REQUEST
        else:
            for book in self.books:
                if new_book["author"] == book["author"] and new_book["title"] == book["title"]:
                    resp.media = {"error": "Another book with similar title and author already exists."}
                    resp.status = falcon.HTTP_BAD_REQUEST
                    return 
            
            new_book["id"] = str(uuid.uuid4())
            self.books.append(new_book) 
            resp.media = new_book
            resp.status = falcon.HTTP_201




#http request olarak atılan isteklerin çalıştıracağı kodlar tanımlanıyor