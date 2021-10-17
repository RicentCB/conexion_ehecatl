# Librerias
import flightController
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Drone:
    __serverDb = 'https://conexionehecatl2021-default-rtdb.firebaseio.com/'
    __nameCollection = 'instructionsid'
    __idDrone = 1
    __db = None
    __battery = 0

    def __init__(self):
        # Inciializar instancia de firebase
        cred = credentials.Certificate("private_key.json")
        firebase_admin.initialize_app(cred, {'databaseURL': self.__serverDb})
        self.__controller = flightController.FlightController()
        self.__db = db.reference("/%s%d"%(self.__nameCollection, self.__idDrone))
        self.setReady()
        self.__db.listen(self.onInstruction)
        print("Script Iniciado")
        print("Esperando instruccion")

    def __maxRange(self, battery):
        return battery * 100;

    # Metodo para enviar informacion a la interfaz de conexion
    # @param data: Mapa con los datos a enviar
    def __sendInformation(self, data):
        self.__db.push(data)

    # Metodo para limpiar interfaz de conexion
    def __cleanChannel(self):
        self.__db.parent.delete();

    # Metodo para preparar al drone
    def setReady(self):
        self.__cleanChannel()
        # Solicitar informacion al controlador de vuelo
        info = self.__controller.information
        # Limpiar informacion para ser enviada
        data = {
            'ins': 'dro_ready', 
            'battery': info['battery'],
            'currentLat': info['currentLat'],
            'currentLon': info['currentLon'],
            'maxRange': self.__maxRange(info['battery'])
        }
        self.__sendInformation(data)
    
    # Metodo para obtener posicion actual
    def setPosition(self):
        # Solicitar informacion al controlador de vuelo
        info = self.__controller.information
        # Limpiar informacion para ser enviada
        stateOfDrone = 'waiting'
        data = {
            'ins': 'dro_position', 
            'state': stateOfDrone,
            'battery': info['battery'],
            'currentLat': info['currentLat'],
            'currentLon': info['currentLon'],
            'maxRange': self.__maxRange(info['battery'])
        }
        self.__sendInformation(data)

    def onInstruction(self, dataRecived):
        dataRec = dataRecived.data
        if(dataRec != None and 'ins' in dataRec):
            instruction = dataRec['ins']
            print(instruction)
            if(instruction == 'app_prepared'):
                self.setReady()
            elif(instruction == 'app_position'):
                self.setPosition()
