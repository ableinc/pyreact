from pyreact import React, Stylesheet
from pyreact.responses import html

class App(React):
    def __init__(self):
        super(App, self).__init__()
        self.state = {}
        self.stylesheet = Stylesheet('App.css')
        
    def render(self, request):
        self.root(self)  # REQUIRED
        content = f"""
        <div class="example">
            <h1>Welcome to PyReact</h1>
        </div>
        """
        return html(content, self.stylesheet)

