import sys
from .tools import PyNodeDict
from .state import State


class React(State):
    def __init__(self):
        super(React, self).__init__()
    
    def root(self, cls):
        self._app_lifecycle(cls)
