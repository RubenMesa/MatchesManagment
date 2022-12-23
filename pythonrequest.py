import requests

class PythonRequest():

    def __init__(self, url):
        self.url=url
        
        
    def get_posiciones():
        url_posiciones = f'http://127.0.0.1:8000/api/posiciones/'
        response = requests.get(url_posiciones)
        json = response.json()
        print ("{:<20} {:<15}".format("Nombre", "Descripción"))
        print ("{:<20} {:<15}".format("--------", "-------------"))
        for element in json['verposicion']:
            print("{:<20} {:<15}".format(element['nombre'],element['descripcion']))
        print("")
    
    def post_posiciones(data):
        url = "http://127.0.0.1:8000/api/posiciones/"
        response = requests.post(url, data=data)
        json = response.json()
        print(json['message'])

    def put_posiciones(id,data):
        url = ("http://127.0.0.1:8000/api/posiciones/"+id)
        response = requests.put(url, data=data)
        json = response.json()
        print(json['message'])

    def delete_posiciones(id):
        url = ("http://127.0.0.1:8000/api/posiciones/"+id)
        response = requests.delete(url)
        json = response.json()
        print(json['message'])

