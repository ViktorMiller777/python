from Viaje import Viaje
from Chofer import Chofer
from Taxi import Taxi
import json
from Connection import Connection

class Interfaz_viaje:
    def __init__(self):
        self.viaje = Viaje()
        self.conexion = Connection()
        self.choferes = Chofer()
        archivo = 'datos_viaje.json'
        self.viaje.convertir_obj(archivo)


    def menu(self):
        print("1. Crear un viaje")
        print("2. Mostrar un viaje")
        print("3. Actualizar un viaje")
        print("4. Eliminar un viaje")
        print("5. Salir")

    def create(self):
        distancia = input("Ingresa la distancia: ")
        destino = input("Ingresa el destino: ")
        precio = input("Ingresa el precio: ")
        
        print("Crear chofer")
        nombre = input("Ingresa tu nombre: ")
        paterno = input("Ingresa tu apellido paterno: ")
        materno = input("Ingresa tu apellido materno: ")
        rfc = input("Ingresa tu RFC: ")

        print("Crear taxi")
        matricula = input("Ingresa tu matricula: ")
        color = input("Ingresa un color: ")
        marca = input("Ingresa la marca: ")
        modelo = input("Ingresa el modelo: ")
        submarca = input("Ingresa la submarca: ")

        taxi = Taxi(matricula, color, marca, modelo, submarca)
        chofer = Chofer(nombre, paterno, materno, rfc, [taxi])
        viaje = Viaje(distancia, destino, precio, [chofer])

        #aqui sucede la magia :D

        if self.conexion.check_connection():
            self.viaje.crear(viaje)
            archivo = 'datos_viaje.json'
            self.viaje.convertir_json(archivo)
            with open(archivo, 'r') as file:
                datos = json.load(file) 

            self.conexion.collection.insert_many(datos)
            with open(archivo, 'w') as file:
                json.dump([], file)

            documentos = self.conexion.collection.find()
            for documento in documentos:
                print(documento)
        else:
            self.viaje.crear(viaje)
            archivo = 'datos_viaje.json'
            self.viaje.convertir_json(archivo)


    def read(self):
        index = int(input("Ingresa el índice del viaje: "))
        viaje = self.viaje.obtener(index)
        if viaje:
            print(f"Información del viaje: {viaje}\n")
        else:
            print("Índice fuera de rango")

    def update(self):
        index = int(input("Ingresa el índice del viaje: "))
        if 0 <= index < len(self.viaje.data):
            distancia = input("Ingresa la nueva distancia: ")
            destino = input("Ingresa el nuevo destino: ")
            precio = input("Ingresa el nuevo precio: ")

            print("Crear chofer")
            nombre = input("nuevo nombre: ")
            paterno = input("nuevo apellido paterno: ")
            materno = input("nuevo apellido materno: ")
            rfc = input("nuevo RFC: ")

            print("Crear taxi")
            matricula = input("nuevo matricula: ")
            color = input("Ingresa un color: ")
            marca = input("Ingresa la marca: ")
            modelo = input("Ingresa el modelo: ")
            submarca = input("Ingresa la submarca: ")

            taxi = Taxi(matricula, color, marca, modelo, submarca)
            chofer = Chofer(nombre, paterno, materno, rfc, [taxi])
            viaje = Viaje(distancia, destino, precio, [chofer])

            self.viaje.actualizar(index, viaje)
            archivo = 'datos_viaje.json'
            self.viaje.convertir_json(archivo)

    def delete(self):
        index = int(input("Ingresa el índice del viaje: "))
        self.viaje.eliminar(index)
        archivo = 'datos_viaje.json'
        self.viaje.convertir_json(archivo)

    def mostrar_menu(self):
        while True:
            self.menu()
            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                self.create()
            elif opcion == '2':
                self.read()
            elif opcion == '3':
                self.update()
            elif opcion == '4':
                self.delete()
            elif opcion == '5':
                print("Saliendo de la interfaz...")
                break
            else:
                print("Opción no válida")

if __name__ == '__main__':
    interfaz_viaje = Interfaz_viaje()
    interfaz_viaje.mostrar_menu()
