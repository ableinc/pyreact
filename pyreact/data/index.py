from pyreact import ReactDOM

# import Screens
from .App import App

if __name__ == '__main__':
    router = [
        { 'url': '/', 'handler': App() }
    ]
    ReactDOM(router=router).render()