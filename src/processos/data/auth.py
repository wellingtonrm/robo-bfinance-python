from src.processos.data.services.api import Api

class Authenticacao():
    def __init__(self) -> None:
        pass
    
    def token(self):
         payload = {"email":"wrm@gmail.com", "password":"sd121212"}
         data = Api().post('/auth', payload, '')
         dataJson = data.json()
         return dataJson["response"]["access_token"]
