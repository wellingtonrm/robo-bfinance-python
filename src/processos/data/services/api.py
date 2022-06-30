from asyncio import exceptions
import requests


class Api():

    url = "https://investoficial.herokuapp.com/v1"

    def __init__(self) -> None:
        pass
    
    def post(self, path, params={}, token=''):
        data= requests.post(self.url+path, data=params, headers={'Authorization': 'bearer '+token})
        return data
        
    def get(self,path, params={}, token=''):
        data= requests.get(self.url+path,  params, headers={'Authorization': 'bearer '+token})
        return data
        

    def put(self, path, parms):
        pass

    def delete(self, path, parms):
        pass
    