import os
from rich.panel import Panel
from rich.console import Console
from rich.padding import Padding
from rich.table import Table




class Debug():


    def log(param, symbol, price):
        
       
        console = Console()
        match param:
         case 'periodo 1':
          limpar = 'cls' if os.name == 'nt' else 'clear'
          os.system(limpar)        
          console.print(Panel.fit(f"[bold yellow] Robo Bfinance conectado ao Binance", border_style="green"))
          
        
          tableEstrategiaSuporteResistencia  = Table()
          tableEstrategiaSuporteResistencia.add_column("Suporte e Rsistencia", justify="center")
          tableEstrategiaSuporteResistencia.columns[0].header_style = "bold"
        
          
        
        
          table1 = Table()
          table1.add_column(f"Symbol {symbol}", justify="left")
          
          table1.add_row(f"Preço atual - {price}")
          table1.add_row(f"Preço objetivo de compra - {price}")
          tableEstrategiaSuporteResistencia.add_row(table1)
      
          console.print(tableEstrategiaSuporteResistencia)
          
          
          
         case 'periodo 2':
          limpar = 'cls' if os.name == 'nt' else 'clear'
          os.system(limpar)
          console.print(Panel.fit(f"[bold yellow] Robo Bfinance conectado ao Binance", border_style="green"))
          
        
          tableEstrategiaSuporteResistencia  = Table()
          tableEstrategiaSuporteResistencia.add_column("Media Movel Aritimetica", justify="center")
          tableEstrategiaSuporteResistencia.columns[0].header_style = "bold"
        
        
          table1 = Table()
          table1.add_column(f"Symbol {symbol}", justify="left")
          
          table1.add_row(f"Preço atual - {price}")
          table1.add_row(f"Preço objetivo de compra - {price}")

          tableEstrategiaSuporteResistencia.add_row(table1)
      
          console.print(tableEstrategiaSuporteResistencia)