from src.threadEstrategiaMediaMovelAritimetica import ExecThreadsMediaMovelAritimetica
from src.threadEstrategiaSuporteResistencia import ExecThreadSuporteResistencia

suporteesistenciahread = ExecThreadsMediaMovelAritimetica(1, 'Media Movel Aritimetica')
mediaMovelAritimetica = ExecThreadSuporteResistencia(1, 'suporte e Resistencia')

arrThread = []
arrThread.append(suporteesistenciahread)
arrThread.append(mediaMovelAritimetica)

mediaMovelAritimetica.start()
suporteesistenciahread.start()

for thred in arrThread:
    thred.join()

