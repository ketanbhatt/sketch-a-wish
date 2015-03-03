import mimetypes
import os
import magic


def get_mimetype(fobject):
    '''
    Guess mimetype of a file using python-magic
    '''
    mime = magic.Magic(mime=True)
    mimetype = mime.from_buffer(fobject.read(1024))
    fobject.seek(0)
    return mimetype


def valid_image_mimetype(fobject):
    '''
    Look inside the file using python-magic to make sure the mimetype is an image
    '''
    mimetype = get_mimetype(fobject)
    if mimetype:
        return mimetype.startswith('image')
    else:
        return False
