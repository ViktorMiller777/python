from Taxi import Taxi
class Interfaz:
    def __init__(self,taxis=None):
        self.isFile=taxis is None
        if self.isFile:
            self.taxi = Taxi()
            archivo = 'datos_taxi.json'
            self.taxi.convertir_obj(archivo)
        else:
            self.taxi = taxis

    def menu(self):
        print("1. Crear un taxi.")
        print("2. Informacion de un taxi.")
        print("3. Actualizar un taxi.")
        print("4. Eliminar un taxi.")
        print("5. Salir")

    def create(self):
        matricula = input("Ingresa tu matricula: ")
        color = input("Ingresa un color: ")
        marca = input("Ingresa la marca: ")
        modelo = input("Ingresa el modelo: ")
        submarca = input("Ingresa la submarca: ")
        taxi = Taxi(matricula, color, marca, modelo, submarca)
        self.taxi.crear(taxi) 
        archivo = 'datos_taxi.json'
        self.taxi.convertir_json(archivo)  

    def read(self):
        index = int(input("Ingresa el indice del taxi: "))
        taxi = self.taxi.obtener(index)
        if taxi:
            print(f"Informacion del Taxi: {taxi}\n")
        else:
            print("Taxi no encontrado.")

    def update(self):
        index = int(input("Ingresa el índice del taxi: "))
        if 0 <= index < len(self.taxi.data):
            matricula = int(input("Ingresa la nueva matricula: "))
            color = input("Ingresa el nuevo color: ")
            marca = input("Ingresa la nueva marca: ")
            modelo = input("Ingresa el nuevo modelo: ")
            submarca = input("Ingresa la nueva submarca: ")
            taxi = Taxi(int(matricula), color, marca, modelo, submarca)
            self.taxi.actualizar(index, taxi)
            archivo = 'datos_taxi.json'
            self.taxi.convertir_json(archivo)   
            
        else:
            print("Indice fuera de rango.")

    def delete(self):
        index = int(input("Selecciona el Indice del taxi: "))
        self.taxi.eliminar(index)
        archivo = 'datos_taxi.json'
        self.taxi.convertir_json(archivo)   

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
                print("Saliendo del sistema")
                break
            else:
                print("Opcion no valida \n")

if __name__ == '__main__':
    interfaz = Interfaz()
    interfaz.mostrar_menu()
