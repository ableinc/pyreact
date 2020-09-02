import sys
try:
    from pyreact.tools import PyNodeDict
    from pyreact.state import State
except ImportError:
    from .tools import PyNodeDict
    from .state import State


class React(State):
    def __init__(self):
        pass
    
    def root(self, cls):
        self._app_lifecycle(cls)
