import requests


class Api():

    url = "https://investoficial.herokuapp.com/v1"

    def __init__(self) -> None:
        pass
    
    def post(self, path, params):
        data= requests.post(self.url+path, data=params)
        return data

    def get(self,path, parms):
        pass

    def put(self, path, parms):
        pass

    def delete(self, path, parms):
        pass