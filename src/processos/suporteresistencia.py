from src.processos.scripts.periodoCandles import PeriodoCandles
from src.processos.data.controleBot import ControleBot
from src.processos.data.services.checkInternet import check
from src.processos.data.auth import Authenticacao
from src.processos.data.candles import Candles
from src.processos.color import bcolors
from src.processos.abstract.estrategia import Estrategia
from src.processos.data.priceatual import PriceAtual
from src.processos.logs.log import Console
import time

# Estrategia baseada em 6 dias no Timeframe 1 hora


class SuporteResistencia(Estrategia):
    preco = 0

    def __init__(self):
        self.token = Authenticacao().token()

    def foreachSymbolControle(self):
        data = ControleBot().exec(self.token)
        for symbol in data:
          if symbol["status"] == True:
             self.montarestrategia(symbol["symbol"]) 

    def montarestrategia(self, symbol):
        initPreco      = PriceAtual().getData(symbol, self.token)
        initCandles    = Candles().getData(symbol, self.token)
        candles        = list(reversed(initCandles))
        periodoCandles = PeriodoCandles(symbol, candles).exec()

    def executarRobo(self):

        while True:
            self.foreachSymbolControle()
        # data =  self.getcandles()
           #Console().log(self.symbol, bcolors.OK)
            #Console().log(self.preco, bcolors.OK)
            time.sleep(3)
