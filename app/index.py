import sys
sys.path.append('.')
from pyreact.dom import ReactDOM

# import Screens
from Screens.Home import HomePage
from Screens.About import AboutPage

if __name__ == '__main__':
    router = [
        { 'url': '/', 'handler': HomePage() },
        { 'url': '/about', 'handler': AboutPage() }
    ]
    ReactDOM(router=router).render()