import threading
from src.processos.mediamovelaritimetica import MediaMovelAritimetica


class ExecThreadsMediaMovelAritimetica(threading.Thread):
    
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id =id
        self.name =name
        
    
    def run(self):
        MediaMovelAritimetica().executarRobo() 