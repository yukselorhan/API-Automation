import falcon
import uuid

def validate_uuid(req, resp, resource, params):
    try:
        uuid.UUID(params['book_id'], version=4)
    except ValueError:
        raise falcon.HTTPBadRequest(description="Not a valid uuid.")
