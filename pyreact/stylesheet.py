import os.path as path
import inspect

class Stylesheet:
    def __init__(self, stylesheet):
        self.stylesheet = stylesheet
    
    def init(self):
        # print('PARENT: ', inspect.stack()[2][3])
        # print('FRAMEINFO: ', inspect.stack()[3])
        stylesheet_directory = inspect.stack()[3][1]
        return path.join(path.dirname(stylesheet_directory), self.stylesheet)
