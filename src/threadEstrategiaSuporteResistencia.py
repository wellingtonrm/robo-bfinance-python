from src.processos.suporteresistencia import SuporteResistencia
import threading



class ExecThreadSuporteResistencia(threading.Thread):
    
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id =id
        self.name =name
        
    
    def run(self):
        SuporteResistencia().executarRobo()