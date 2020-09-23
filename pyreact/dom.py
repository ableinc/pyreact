import sys, os
from sanic import Sanic
from pydotenvs import load_env
from pathlib import Path
from .htmlparser import Parser
from .emitter import EventEmitter, EventListener
from .responses import html
from .javascript.browser.index import WebBrowswer

load_env()
app = Sanic(__name__)
app.static('/static', os.path.abspath(os.curdir + '/public'))

webbrowser = WebBrowswer()
emitter = EventEmitter()
listener = EventListener()
emitter.subscribe(listener.func, 'func')


def _get_environment_variables_():
    host = os.environ.get('PYREACT_HOST', '127.0.0.1')
    port = os.environ.get('PYREACT_PORT', 8000)
    env = os.environ.get('PYREACT_ENV', 'dev')
    return host, port, env


@app.listener('after_server_start')
async def _open_in_browser_(app, loop):
    host, port, _ = _get_environment_variables_()
    print('[PLACEHOLDER FOR AFTER_SERVER_START LISTENER]')
    # webbrowser.open(f'http://{host}:{port}')
    # emitter.send('func', data=_write_to_checkpoints_, args=('SERVER_STARTED', '1'))
    # webbrowser.open(f'http://{host}:{port}')


def _write_to_checkpoints_(key, value):
    os.environ[key] = value

# emitter.send('func', data=_write_to_checkpoints_, args=('SERVER_STARTED', '0'))


class ReactDOM:
    def __init__(self, router):
        self.router  = router
        self.html = None
        self.htmlParser = Parser()
    
    def _assign_handlers_(self):
        try:
            # app.add_route(root, '/')
            for handler in self.router:
                app.add_route(handler['handler'].render, handler['url'])
        except Exception as e:
            print(e)
        except AttributeError as ae:
            print(ae)

    def _start_server_(self):
        host, port, env = _get_environment_variables_()
        app.run(host=host, port=port, auto_reload=True if 'dev' in env else False)

    def render(self, index_file_path: str = ''):
        errors = []
        try:
            # self.htmlParser.feed(self.html)  # not required
            if index_file_path == '':
                index_file_path = os.path.abspath(os.curdir + '/public/index.html')
            with open(f'{index_file_path}') as html:
                self.html = html.read()
        except Exception as ex:
            print('A valid html file must be provided.')
            errors.append(ex)
        finally:
            if len(errors) > 0:
                sys.exit()
            else:
                os.environ['indexFile'] = index_file_path
                self._assign_handlers_()
                self._start_server_()
    

