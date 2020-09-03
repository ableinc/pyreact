try:
    from pyreact.tools import PyNodeDict  # implement later
    from pyreact.main import React
    from pyreact.dom import ReactDOM
    from pyreact.response import html
except ImportError:
    from .tools import PyNodeDict
    from .main import React
    from .dom import ReactDOM
    from .response import html
        

class App(React):
    def __init__(self):
        super(App, self).__init__()
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
        self.stylesheet = 'style.css'

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
        container = []
        for item in self.state['items']:
            container.append(f"<p>{item['name']}: {item['cost']}</p>")
        content = f"""
        <div class="example">
            <h1>App Page</h1>
            <p>Store Name: {self.state['shop_name']}</p>
            <p>Inventory:</p>
            {container}
        </div>
        """
        return html(content, self.stylesheet)


if __name__ == '__main__':
    router = [
        { 'url': '/', 'handler': App()}
    ]
    ReactDOM(router=router).render()
