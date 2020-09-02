from sanic import response
from bs4 import BeautifulSoup
import os, sys

def _append_to_root_index(html_content: str):
    index_file = os.environ.get('indexFile', None)
    if index_file == None:
        print('No index file found. Exiting.')
        sys.exit()
    with open(index_file) as fp:
        raw_html = fp.read()
    soup = BeautifulSoup(raw_html, 'html.parser')
    soup.div.append(BeautifulSoup(html_content, 'html.parser'))
    return soup.prettify(formatter='html')


def text(content):
    return response.text(content)


def html(content):
    return response.html(_append_to_root_index(content))


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