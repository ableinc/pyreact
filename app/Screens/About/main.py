from pyreact import React, Stylesheet
from pyreact.responses import html
from datetime import datetime


class AboutPage(React):
    def __init__(self):
        super(AboutPage, self).__init__()
        self.state = {}
        self.stylesheet = Stylesheet('style.css')
    
    def pyDidMount(self):
        print('About page loaded.')
    
    def get_date_string(self):
        today = f"Today's date is {datetime.now()}"
        return today

    def add_date_to_state(self):
        today = self.get_date_string()
        self.setState({ "date": today }, self)
    
    def display_date(self):
        date_string = self.get_date_string()
        view = f"""
        <p>{date_string}</p>
        """
        return view

    def render(self, request):
        self.root(self)  # REQUIRED
        self.add_date_to_state()
        content = f"""
        <div class="aboutPage">
            <div class="nav">
                <ul>
                    <a href="/">Main Page</a>
                </ul>
            </div>
            <h1>About Page</h1>
            <p>{self.state['date']}</p>
            <p>{self.display_date()}</p>
        </div>
        """
        return html(content, self.stylesheet)
