from src.processos.data.services.api import Api
from  src.processos.logs.log import Console

class ControleBot():
    
    def __init__(self) -> None:
        pass
    
    def exec(self, token):
     data = Api().get('/bot/vereficstart',  {}, token)
     dataJson = data.json()
     return dataJson["response"]