from pyreact import React, Stylesheet
from pyreact.responses import html


class AboutPage(React):
    def __init__(self):
        super(AboutPage, self).__init__()
        self.state = {}
        self.stylesheet = Stylesheet('style.css')
    
    def pyDidMount(self):
        print('About page loaded.')

    def render(self, request):
        content = """
        <div class="aboutPage">
            <div class="nav">
                <ul>
                    <a href="/">Main Page</a>
                </ul>
            </div>
            <h1>About Page</h1>
        </div>
        """
        return html(content, self.stylesheet)
