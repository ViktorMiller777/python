class Crud:
    def __init__(self):
        self.data = []
        
    def crear(self, item):
        self.data.append(item)
        print(f"Item {item} agregado a la lista.\n")

    def actualizar(self, index, item):
        if 0 <= index < len(self.data):
            self.data[index] = item
            print(f"Item en índice {index} actualizado a: {item}.\n")
        else:
            print("Índice fuera de rango.")

    def eliminar(self, index):
        if 0 <= index < len(self.data):
            print(f"Item {self.data[index]} eliminado de la lista.\n")
            del self.data[index]
        else:
            print("Índice fuera de rango.")

    def obtener(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            print("Índice fuera de rango.")
            return None
    