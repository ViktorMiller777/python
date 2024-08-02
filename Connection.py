from pymongo import MongoClient, errors

class Connection:
    def __init__(self):
        try:
            self.client = MongoClient('mongodb+srv://bolillo:bolillo123@cluster0.sruil0z.mongodb.net/?retryWrites=true&w=majority')
            self.database = self.client['TestMongo']
            self.collection = self.database['Viajes']
        except errors.ConfigurationError as e:
            print(f"Error de conexión a MongoDB: {e}")
        except errors.ConfigurationError as e:
            print(f"Error de configuración en la conexión a MongoDB: {e}")

    def check_connection(self):
        try:
            self.client.server_info()
            print("Conexión establecida con MongoDB.")
            return True
        except errors.OperationFailure as e:
            print(f"Error de autenticación: {e}")
            return False
        except Exception as e:
            print(f"No se pudo conectar a MongoDB: {e}")
            return False
    
conexion = Connection()

if not conexion.check_connection():
    print("no hay conexion")
else:
    print("sí hay conexion")

   