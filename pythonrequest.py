import requests

class PythonRequest():

    def __init__(self, url):
        self.url=url
        
        
    def get_posiciones():
        url_posiciones = f'http://127.0.0.1:8000/api/posiciones/'
        response = requests.get(url_posiciones)
        # response.text
        json = response.json()
        print ("{:<20} {:<15}".format("Nombre", "Descripción"))
        print ("{:<20} {:<15}".format("--------", "-------------"))
        for element in json['verposicion']:
            print("{:<20} {:<15}".format(element['nombre'],element['descripcion']))
        print("")
    
    def post_posiciones():
        url = "http://127.0.0.1:8000/api/posiciones/"
        data = '{"nombre": "Juanito", "descripcion": "descripcion de prueba" }'
        response = requests.post(url, data=data)
        json = response.json()
        print(json['message'])

    def put_posiciones():
        id= "11"
        url = ("http://127.0.0.1:8000/api/posiciones/"+id)
        data = '{"nombre": "Juanitoo", "descripcion": "descripcion de prueba" }'
        response = requests.put(url, data=data)
        json = response.json()
        print(json['message'])

    def delete_posiciones():
        id= "11"
        url = ("http://127.0.0.1:8000/api/posiciones/"+id)
        #data = '{"nombre": "Juanitoo", "descripcion": "descripcion de prueba" }'
        response = requests.delete(url)
        json = response.json()
        print(json['message'])




a=PythonRequest.delete_posiciones()