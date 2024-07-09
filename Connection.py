from pymongo import MongoClient, errors

class Connection:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://bolillo:bolillo23@cluster0.sruil0z.mongodb.net/?retryWrites=true&w=majority')
        self.database = self.client['Uber']
        self.collection = self.database['Viajes']

    def check_connection(self):
        try:
            self.client.server_info()
            print("Conexión establecida con MongoDB.")
            return True
        except Exception as e:
            print(f"No se pudo conectar a MongoDB: {e}")
            return False
    
conexion = Connection()

if not conexion.check_connection():
    print("no hay conexion")
else:
    print("sin hay conexion")

   