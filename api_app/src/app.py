import falcon

from api_app.src import  books

api = application = falcon.API()

api.add_route('/books', books.Books())
api.add_route('/book/{book_id}', books.Book())
api.add_route('/book', books.Book())


