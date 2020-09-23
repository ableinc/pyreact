from sanic.response import HTTPResponse
from .responses import html
import inspect


class Recursion:
    def __init__(self):
        self.count = 0
    
    def get_count(self):
        return self.count
    
    def set_count(self, value):
        self.count += value


class State:
    def __init__(self):
        super(State, self).__init__()
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
        print('PARENT: ', inspect.stack()[2][3])
        if isinstance(state, list):
            for arg in state:
                for key, value in arg.items():
                    self.state[key] = value
        else:
            for key, value in state.items():
                self.state[key] = value
        self._app_lifecycle(cls)
  