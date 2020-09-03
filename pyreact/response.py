from sanic import response
from pyreact.helper import append_to_root_index

def text(content):
    return response.text(content)


def html(content, stylesheet: str = ''):
    return response.html(append_to_root_index(content, stylesheet))


def json(content):
    return response.json(content)


def sendFile(content):
    return response.file(content)


def stream(content):
    return response.stream(content)


def file_stream(content):
    return response.file_stream(content)


def redirect(content):
    return response.redirect(content)


def raw(content: bytes):
    if not isinstance(content, bytes):
        return response.raw(b'{0}'.format(content))
    return response.raw(content)


def empty():
    return response.empty()