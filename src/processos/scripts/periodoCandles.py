
datass= {
    'openTime': 1655269200000, 
    'open': '3.41470000', 
    'high': '3.43940000', 
    'low': '3.28170000', 
    'close': '3.37010000', 
    'volume': '1226023.72000000', 
    'closeTime': 1655272799999, 
    'quoteVolume': '4112767.56106800', 
    'trades': 14020, 
    'baseAssetVolume': '623806.29000000', 
    'quoteAssetVolume': '2094632.67475500'
    }



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
        self.minimoPeridoUM.append(periodo)    
        print(self.minimoPeridoUM)
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
    
    