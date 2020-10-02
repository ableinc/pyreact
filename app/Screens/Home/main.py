from pyreact import React, Stylesheet
from pyreact.responses import html

class HomePage(React):
    def __init__(self):
        super(HomePage, self).__init__()
        self.state = {
            'items': [
                {
                'name': 'Apples',
                'cost': '1.25'
                },
                {
                'name': 'Oranges',
                'cost': '2.25'
                }
            ],
            'shop_name': "Greg's Fruit Stand"
            }
        self.stylesheet = Stylesheet('style.css')

    def pyDidMount(self):
        print('pyDidMount()')

    def pyWillMount(self):
        print('pyWillMount()')
    
    def pyWillUpdate(self):
        print('pyWillUpdate: ', self.state)
  
    def pyDidUpdate(self):
        print('pyDidUpdate: ', self.state)
  
    def push(self):
        self.setState({'foo': 'bar'}, self)
    
    def pop(self):
        self.setState({'foo': ''}, self)
        
    def render(self, request):
        self.root(self)  # REQUIRED
        container = []
        self.push()  # Not recommended, setState outside of render().
        for item in self.state['items']:
            container.append(f"<p>{item['name']}: {item['cost']}</p>")
        content = f"""
        <div class="example">
            <div class="nav">
                <ul>
                    <a href="/about">About Page</a>
                </ul>
            </div>
            <h1>Home Page</h1>
            <p>Store Name: {self.state['shop_name']}</p>
            <p>Inventory:</p>
            {container}
        </div>
        """
        return html(content, self.stylesheet)

