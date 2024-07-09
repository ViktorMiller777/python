import json
from Crud import Crud
class Taxi(Crud):
    def __init__(self, matricula=None, color=None, marca=None, modelo=None, submarca=None):
        super().__init__()
        self.isList=matricula is None and color is None and marca is None and modelo is None and submarca is None
        if self.isList:
            self.tipo = "Lista"
            print("Es una lista")
        else:
            self.tipo = "Objeto"
            self.matricula = int(matricula)
            self.color = color
            self.marca = marca
            self.modelo = modelo
            self.submarca = submarca

    def __str__(self): #este te muestra el objeto en string y no en memoria como el print
        if self.isList:
            return "Esta instancia es una lista de taxis."
        else:
            return f"{self.tipo} Taxi:{int(self.matricula)}, {self.color}, {self.marca}, {self.modelo}, {self.submarca}"

    def mostrar_lista(self):
        if self.isList:
            print("Lista de Taxis:")
            for taxi in self.data:
                print(taxi)
        else:
            print("Esta no es una lista de taxis")

    def mostrar_objeto(self):
        if not self.isList:
            print(f"Taxi ({self.tipo}):{self.matricula}, {self.color}, {self.marca}, {self.modelo}, {self.submarca}")
        else:
            print("Esta instancia no es un objeto individual de taxi.")

    def dict(self):
        if not self.isList:
            return {
                "matricula: ": self.matricula,
                "color: ": self.color,
                "marca: ": self.marca,
                "modelo: ": self.modelo,
                "submarca: ": self.submarca
            }
        
    def diccionario(self):
        if self.isList:
            return [taxi.dict() for taxi in self.data]
        else:
            return self.dict()

    def convertir_json(self,filename="datos_taxi.json"):
        json_data = self.diccionario()
        with open(filename, 'w') as file:
            json.dump(json_data, file, indent=4)
        
#CONVERTIR A OBJETO
    def verificar(self,data):
        taxi=None
        if isinstance(data, dict):
            print("data:",data)
            taxi = Taxi(
                matricula=data.get('matricula: '),
                color=data.get('color: '),
                marca=data.get('marca: '),
                modelo=data.get('modelo: '),
                submarca=data.get('submarca: ')
            )
        else:
            self.data = []
            for item in data:
                print("item",item)
                self.crear(self.verificar(item))
        return taxi

        
    def convertir_obj(self,archivo):
        with open(archivo, 'r') as file:
            data = json.load(file)
        taxis = self.verificar(data)
        return taxis 
                
if __name__ == '__main__':

    lista_taxi = Taxi()

    nombre_archivo = "datos_taxi.json"

    # print(f"Los datos del taxi se han guardado en el archivo '{nombre_archivo}'.")

    print("------------------------------------------------")
    archivo = 'datos_taxi.json'
    # lista_taxi.convertir_obj(archivo)

    #aqui solo estoy creando instancias de taxis para guardarlos en la lista
    taxi1 = Taxi(10,"rojo","lamborghini","2020","deportivo")
    taxi2 = Taxi(20,"negro","volkswagen","2010","pointer")
    taxi3 = Taxi(30,"azul","ford","2020","pickup")
    #ahora toca agregar los autos a la lista
    lista_taxi.crear(taxi1)
    lista_taxi.crear(taxi2)
    lista_taxi.crear(taxi3)

    #con este codigo se guarda o actualiza en el archivo de los autos
    lista_taxi.convertir_json(archivo)




    for obj in lista_taxi.data:
        if(obj is not None):
            print(f"Objeto: {obj}")

  
