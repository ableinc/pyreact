from sanic.response import HTTPResponse
from pyreact.response import html

class State:
    def __init__(self):
        self.state = {}
    
    def _app_lifecycle(self, cls):
        try:
            cls.pyWillUpdate()
            cls.pyDidUpdate()
        except AttributeError as ae:
            print(ae)
        
        try:
            html(cls.render(HTTPResponse))
            cls.pyDidMount()
            cls.pyWillMount()
        except AttributeError:
            print(f'{cls.__name__} does not have a render function.')
        
    @staticmethod
    def init():
        return HTTPResponse
    
    def setState(self, state, cls):
        if isinstance(state, list):
            for arg in state:
                for key, value in arg.items():
                    self.state[key] = value
        else:
            for key, value in state.items():
                self.state[key] = value
        print('setState()')
        self._app_lifecycle(cls)
  