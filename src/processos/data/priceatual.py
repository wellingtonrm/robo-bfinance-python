from src.processos.data.services.api import Api
from  src.processos.logs.log import Console

class PriceAtual():

    def __init__(self) -> None:
        pass

    def getData(self, symbol=None, token=None):
        if symbol  == None:
         Console().log('Error: Modulo PriceAtua getData param vazio')
        else:
         payload = {"symbol":symbol}
         data = Api().post('/bn/prices', payload, token)
         dataJson = data.json()
         return dataJson["response"]
        
        