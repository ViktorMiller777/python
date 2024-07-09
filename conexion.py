from pymongo import MongoClient
import json


try:
    client = MongoClient('mongodb+srv://bolillo:bolillo123@cluster0.sruil0z.mongodb.net/?retryWrites=true&w=majority')

    database = client['Uber']

    collection = database['Viajes']

    documentos = collection.find()

    #intefaz de viaje que se mande a llamar los 2 otros intefaces de chofer y taxis 
    #comprobar que en conexion si alla conexion y que el archivo este vacio
    #converti el archivo de conexion en clase



    #INSERTAR DATOS A BASE DE DATOS DE MONGO  

    archivo = 'datos_viaje.json' #MODIFICO EL ARCHIVO ENTRE TAXIS, CHOFERES Y VIAJES PARA PODER INSERTARLOS 

    with open(archivo, 'r') as file:
        datos = json.load(file)

    insert = collection.insert_many(datos)
    with open(archivo, 'w') as file:
        json.dump([], file)
        print("Contenido del JSON insertado en la colección y archivo JSON vaciado.")

    documentos = collection.find()
    for documento in documentos:
        print(documento)
        
except:
    print("no hay conexion con la base de datos en mongo")



    




#YA NOMAS ME FALTA HACER QUE CUANDO EXISTA CONECCION AL CLUSTER IMAGINO QUE TUILIZANDO INTENET, SE MANDARAN LOS DATOS AL SERVIDOR PERO SI NO HAY CONECCION A INTENRET LOS DATOS SE ESTARAN MANDANDO AL ARCHIVO JSON PARA QUE CUANDO SE RECUPERE LA CONECCION MANDAR LOS DATOS DEL ARCHIVO AL SERVIDOR Y VACIAL EL ARCHIVO JSON
