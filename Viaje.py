import json
from Crud import Crud
from Chofer import Chofer
from Taxi import Taxi

class Viaje(Crud):
    def __init__(self, distancia=None, destino=None, precio=None, choferes=None):
        super().__init__()
        self.isList = distancia is None and destino is None and precio is None and choferes is None
        if self.isList:
            self.tipo = 'Lista'
            print("Es una lista")
        else:
            self.tipo = "Objeto"
            self.distancia = distancia
            self.destino = destino
            self.precio = int(precio)
            self.choferes = choferes if choferes is not None else []

    def __str__(self):
        chofer_str = ', '.join(str(chofer) for chofer in self.choferes)
        return f"Distancia: {self.distancia}, Destino: {self.destino}, Precio: {self.precio}, choferes:[{chofer_str}]"
    
    def dict(self):
        if not self.isList:
            return {
                "distancia": self.distancia,
                "destino": self.destino,
                "precio": self.precio,
                "choferes": [chofer.dict() for chofer in self.choferes]
            }
        
    def diccionario(self):
        if self.isList:
            return [viaje.dict() for viaje in self.data]
        else:
            return self.dict()
        
    def convertir_json(self, archivo="datos_viaje.json"):
        json_data = self.diccionario()
        with open(archivo, 'w') as file:
            json.dump(json_data, file, indent=4)

    def verificar(self, data):
        viaje = None
        if isinstance(data, dict):
            print("data:", data)
            viaje = Viaje(
                distancia=data.get('distancia'),
                destino=data.get('destino'),
                precio=data.get('precio'),
                choferes=[Chofer(
                    nombre=chofer.get('nombre'),
                    paterno=chofer.get('paterno'),
                    materno=chofer.get('materno'),
                    rfc=chofer.get('rfc'),
                    taxis=[Taxi(
                        matricula=taxi.get('matricula'),
                        color=taxi.get('color'),
                        marca=taxi.get('marca'),
                        modelo=taxi.get('modelo'),
                        submarca=taxi.get('submarca')
                    ) for taxi in chofer.get('taxis', [])]
                ) for chofer in data.get('choferes', [])]
            )
        else:
            self.data = []
            for item in data:
                print("item", item)
                self.crear(self.verificar(item))
        return viaje

    def convertir_obj(self, archivo):
        with open(archivo, 'r') as file:
            data = json.load(file)
        viajes = self.verificar(data)
        return viajes

if __name__ == '__main__':
    lista_viaje = Viaje()

    taxi1 = Taxi(1010, "naranja", "konoha", "viento", "hokage")
    chofer1 = Chofer("Miller", "Morgan", "Rodriguez", "123", [taxi1])

    viaje1 = Viaje("10 mts", "Mi casa", 100, [chofer1])
    lista_viaje.crear(viaje1)

    archivo = 'datos_viaje.json'
    lista_viaje.convertir_json(archivo)
    lista_viaje.convertir_obj(archivo)
