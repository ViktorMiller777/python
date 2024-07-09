import json
from Crud import Crud
from Taxi import Taxi 

class Chofer(Crud):
    def __init__(self, nombre=None, paterno=None, materno=None, rfc=None, taxis=None):
        super().__init__()
        self.isList = nombre is None and paterno is None and materno is None and rfc is None and taxis is None
        if self.isList:
            self.tipo = "Lista"
            print("Es una lista")
        else:
            self.tipo = "Objeto"
            self.nombre = nombre
            self.paterno = paterno
            self.materno = materno
            self.rfc = rfc
            self.taxis = taxis if taxis is not None else []

    def __str__(self):
        taxi_str = ', '.join(str(taxi) for taxi in self.taxis)
        return f"Chofer: {self.nombre}, {self.paterno}, {self.materno}, {self.rfc}, Taxi:[{taxi_str}]"

    def dict(self):
        if not self.isList:
            return {
                "nombre": self.nombre,
                "paterno": self.paterno,
                "materno": self.materno,
                "rfc": self.rfc,
                "taxis": [taxi.dict() for taxi in self.taxis]
            }
        
    def diccionario(self):
        if self.isList:
            return [chofer.dict() for chofer in self.data]
        else:
            return self.dict()
    
    def convertir_json(self, archivo="datos_chofer.json"):
        json_data = self.diccionario()
        with open(archivo, 'w') as file:
            json.dump(json_data, file, indent=4)

    def verificar(self, data):
        chofer = None
        if isinstance(data, dict):
            print("data:", data)
            chofer = Chofer(
                nombre=data.get('nombre'),
                paterno=data.get('paterno'),
                materno=data.get('materno'),
                rfc=data.get('rfc'),
                taxis=[Taxi(
                    matricula=taxi.get('matricula: '),
                    color=taxi.get('color: '),
                    marca=taxi.get('marca: '),
                    modelo=taxi.get('modelo: '),
                    submarca=taxi.get('submarca: ')
                ) for taxi in data.get('taxis', [])]
            )
        else:
            self.data = []
            for item in data:
                print("item", item)
                self.crear(self.verificar(item))
        return chofer

    def convertir_obj(self, archivo):
        with open(archivo, 'r') as file:
            data = json.load(file)
        chofers = self.verificar(data)
        return chofers
     
if __name__ == '__main__':
    lista_chofer = Chofer()
    archivo = 'datos_chofer.json'
    taxi = Taxi(1010, "naranja", "konoha", "viento", "hokage")
    chofer1 = Chofer("Miller", "Morgan", "Rodriguez", "123", [taxi])
    taxi1 =Taxi(200,"negro","avento","1021","bigi")
    chofer2 = Chofer("yo","yo","yo","yo",[taxi1])
    lista_chofer.crear(chofer1)
    lista_chofer.crear(chofer2)
    lista_chofer.convertir_json(archivo)
    lista_chofer.convertir_obj(archivo)