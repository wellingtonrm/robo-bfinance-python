from src.processos.logs.log import Debug

class PeriodoCandles():
    periodoUM = [] # mais recente candles preco atual
    periodoDOIS = []
    periodoTRES = []
    
    minimoPeridoUM = []
    
    def __init__(self, symbol, candles) -> None:
        self.candles = candles
        self.symbol = symbol
        pass
    
    def exec(self):
        self.foreach()
        self.valorMinimoPeriodoUM()
    
    def foreach(self):
        for candles in range(0, 48):# 24 horas * 2 dias total de 48 candles  no total de 144 candles
            self.periodoUM.append(self.candles[candles])
            
        for candles in range(49, 97):
            self.periodoDOIS.append(self.candles[candles])
        
        for candles in range(98, 144):
            self.periodoTRES.append(self.candles[candles])
       
    
    def valorMinimoPeriodoUM(self):
        
        for candles in self.periodoUM:
            periodo = {}
            valorMinimoStr = ''
            valorMaximoStr = ''
            valorMinimo =0
            valorMaximo = 0
            
            if valorMinimo < float(candles["low"]):
               valorMinimo = float(candles["low"])
               valorMinimoStr = candles["low"]
               
            
            if float(candles["high"]) > valorMaximo:
               valorMaximo = float(candles["high"])
               valorMaximoStr= candles["high"]
              
               
        periodo["periodoUM"] = {
            "low": valorMinimoStr, 
            "high":valorMaximoStr, 
            "symbol":self.symbol
            }
         
        Debug.log("periodo 1", "NEAR", "12,00")
        return valorMinimo
        
    
    def valorMinimoPeriodoDOIS(self):
        pass
    
    def valorMinimoPeriodoTRES(self):
        pass
    
    def valorMaximoPeriodoUM(self):
        pass
    
    def valorMaximoPeriodoDOIS(self):
        pass
    
    def valorMaximoPeriodoTRES(self):
        pass
    
    