from src.threadEstrategiaMediaMovelAritimetica import ExecThreadsMediaMovelAritimetica
from src.threadEstrategiaSuporteResistencia import ExecThreadSuporteResistencia
from src.processos.data.services.checkInternet import check
from  src.processos.logs.log import Debug

import time

while True:
    if not check():
        Debug.log("Network Error!")
        time.sleep(3)
    else:
    
     suporteesistenciahread = ExecThreadsMediaMovelAritimetica(1, 'Media Movel Aritimetica')
     mediaMovelAritimetica  = ExecThreadSuporteResistencia( 1, 'suporte e Resistencia')

     arrThread = []
     arrThread.append(suporteesistenciahread)
     arrThread.append(mediaMovelAritimetica)

     mediaMovelAritimetica.start()
     suporteesistenciahread.start()

     for thred in arrThread:
         thred.join()
    
    