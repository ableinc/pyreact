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
        except AttributeError:
            pass
        
        try:
            # html(cls.render(HTTPResponse))
            cls.pyWillMount()
            cls.pyDidMount()
        except AttributeError:
            pass
        
    @staticmethod
    def init():
        return HTTPResponse
    
    def setState(self, state, cls):
        if 'self.setState' in inspect.stack()[1][4][0]:
            print('Warning: setState() being invoked in render() is not recommended.')
        if isinstance(state, list):
            for arg in state:
                for key, value in arg.items():
                    self.state[key] = value
        else:
            for key, value in state.items():
                self.state[key] = value
        self._app_lifecycle(cls)
  