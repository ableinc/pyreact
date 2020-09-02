import sys, os
from sanic import Sanic
from pydotenvs import load_env
try:
    from pyreact.htmlparser import Parser
    from pyreact.response import html
except ImportError:
    from .htmlparser import Parser
    from .response import html


load_env()
app = Sanic(__name__)


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
    
    @staticmethod
    def _get_environment_variables_():
        host = os.environ.get('PYREACT_HOST', None)
        port = os.environ.get('PYREACT_PORT', None)
        env = os.environ.get('PYREACT_ENV', 'True')
        return host, port, env
    
    def _start_server_(self):
        host, port, env = self._get_environment_variables_()
        app.run(host=f'{host}' if host != None else '127.0.0.1', port=f'{port}' if port != None else '8000', auto_reload=bool(str(env)))
    
    def render(self, index_file_path):
        errors = []
        try:
            # self.htmlParser.feed(self.html)  # not required
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
    

