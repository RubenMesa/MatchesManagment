import requests

class PythonRequest():

    def __init__(self, url):
        self.url=url

    def agregar(self, data):
        response = requests.post(self.url, data)
        respuesta_json = response.json()
        print(respuesta_json)
    
agrega= PythonRequest('http://127.0.0.1:8000/api/posiciones/')
data = {
    "nombre":"mediapunta",
    "descripcion":"Dar el último pase a los delanteros para el gol"
}

agrega.agregar(data)
