from src.processos.data.auth import Authenticacao
from src.processos.data.controleBot import ControleBot
from src.processos.color import bcolors
from src.processos.abstract.estrategia import Estrategia
from src.processos.data.priceatual import PriceAtual
from src.processos.logs.log import Console
from src.processos.data.services.checkInternet import  check
from src.processos.data.candles import Candles
import time

class MediaMovelAritimetica(Estrategia):

    def __init__(self):
        self.token = Authenticacao().token()

    def foreachSymbolControle(self):
        data = ControleBot().exec(self.token)
        for symbol in data:
          if symbol["status"] == True:
             self.montarestrategia(symbol["symbol"])
        
        
        

    def montarestrategia(self, symbol):
        pass


    def executarEstrategia(self):
        pass

    def executarRobo(self):
         while True:
            #data =  self.getpreco()
            #Console().log(data, bcolors.WARNING)
            time.sleep(10)


