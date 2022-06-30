from src.processos.data.services.api import Api
from  src.processos.logs.log import Console


class Candles():

    def __init__(self) -> None:
        pass

    def getData(self, symbol=None, token=None):
        if symbol  == None:
         Console().log('Error: Modulo Candles getData symbol null')
        else:
         payload = {"symbol":symbol, "interval":"1h"}
         data = Api().post('/bn/candles', payload, token)
         dataJson = data.json()
         return dataJson["response"]
        
