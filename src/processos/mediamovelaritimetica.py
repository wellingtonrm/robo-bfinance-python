from src.processos.color import bcolors
from src.processos.abstract.estrategia import Estrategia
from src.processos.data.priceatual import PriceAtual
from  src.processos.logs.log import Console
import time

class MediaMovelAritimetica(Estrategia):

    def __init__(self):
        pass

    def getpreco(self):
        initPreco = PriceAtual().getData('icpusdt')
        return initPreco
        
        
        

    def montarestrategia(self):
        pass


    def executarEstrategia(self):
        pass

    def executarRobo(self):
         while True:
            data =  self.getpreco()
            Console().log(data, bcolors.WARNING)
            time.sleep(10)


