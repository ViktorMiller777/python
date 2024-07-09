from Chofer import Chofer
from Interfaz import Interfaz
from Taxi import Taxi

class Interfaz_chofer(Chofer):
    def __init__(self, chofers = None):
        self.isFile = chofers is None
        if self.isFile:
            self.taxis = Interfaz()
            self.chofer = Chofer()
            archivo = 'datos_chofer.json'
            self.chofer.convertir_obj(archivo)

    def menu(self):
        print("1. Crear un chofer")
        print("2. Mostrar un chofer")
        print("3. Actualizar un chofer")
        print("4. Eliminar un chofer")
        print("5. Salir")

    def create(self):
        nombre = input("Ingresa tu nombre: ")
        paterno = input("Ingresa tu apellido paterno: ")
        materno = input("Ingresa tu apellido materno: ")
        rfc = input("Ingresa tu RFC: ")

        print("Crear taxi:")
        matricula = int(input ("ingresa la matricula: "))
        color = input("color: ")
        marca = input("marca: ")
        modelo = input("modelo: ")
        submarca = input("submarca: ")

        taxi = Taxi(matricula, color, marca, modelo, submarca)
        chofer = Chofer(nombre, paterno, materno, rfc, [taxi]) 
        
        self.chofer.crear(chofer)
        archivo = 'datos_chofer.json'
        self.chofer.convertir_json(archivo)
         
    def read(self):
        index = int(input("Ingresa el indice del chofer: "))
        chofer = self.chofer.obtener(index)
        if chofer:
            print(f"Informacion del chofer: {chofer}\n")
        else:
            print("Indice fuera de rango")

    def update(self):
        index = int(input("Ingresa el indice del chofer: "))
        if 0 <= index < len(self.chofer.data):
            nombre = input("Escribe el nuevo nombre: ")
            paterno = input("Escribe el nuevo apellido paterno: ")
            materno = input("Escribe el nuevo apellido materno: ")
            rfc = input("Escribe el nuevo RFC: ")

            print("Datos nuevos taxi:")
            matricula = input("matricula: ")
            color = input("color: ")
            marca = input("marca: ")
            modelo = input("modelo: ")
            submarca = input("submarca: ")

            taxi = Taxi(matricula, color, marca, modelo, submarca)
            chofer = Chofer(nombre, paterno, materno, rfc, [taxi])

            self.chofer.actualizar(index, chofer)
            archivo = 'datos_chofer.json'
            self.chofer.convertir_json(archivo)  


    def delete(self):
        index = int(input("Ingresa el indice del chofer: "))
        self.chofer.eliminar(index)
        archivo = 'datos_chofer.json'
        self.chofer.convertir_json(archivo)  

    def mostrar_menu(self):
        while True:
            self.menu()
            opcion = input("Selecciona una opcion: ")
            if opcion == '1':
                self.create()
            elif opcion == '2':
                self.read()
            elif opcion == '3':
                self.update()
            elif opcion == '4':
                self.delete()
            elif opcion == '5':
                print("Saliendo")
                break
            else:
                print("Opcion no valida")
                
if __name__ == '__main__':
    interfaz_chofer = Interfaz_chofer()
    interfaz_chofer.mostrar_menu()