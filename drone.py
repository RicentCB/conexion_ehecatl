import time
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
    __state = ''

    def __init__(self):
        # Conexion con el controlador
        self.__controller = flightController.FlightController()
        try: 
            # Incializar instancia de firebase
            cred = credentials.Certificate("private_key.json")
            firebase_admin.initialize_app(cred, {'databaseURL': self.__serverDb})
            self.__db = db.reference("/%s%d"%(self.__nameCollection, self.__idDrone))
            # Enviar comando "Listo" al canal
            self.setReady()
            # Escuchar cambios en el canal
            self.__db.listen(self.onInstruction)
        except:
            print("Error al comunicarse con canal")
        # Mensaje de bienvenida
        print("Script Iniciado")

    # Metodo para calcular el rango maximo que puede volar el drone
    # @param battery (double): bateria actual
    # return (double)
    def __maxRange(self, battery):
        # TODO: Calculo de rango con bateria
        return battery * 100;

    # Metodo para limpiar interfaz de conexion
    def __cleanChannel(self):
        try:
            self.__db.parent.delete();
        except:
            print("Error al limpiar el canal de comunicacion")

    # Metodo para enviar informacion general actual del drone
    # Recopila la informacion del controlador, 
    # y la envia al canal de comunincacion.
    # @param instruction (String): instruccion a enviar
    def __sendInformation(self, instruction, extraInfo = {}):
        # Solicitar informacion al controlador de vuelo
        info = self.__controller.information
        # Limpiar informacion para ser enviada
        data = {
            'ins': instruction, 
            'state': self.__state,
            'battery': info['battery'],
            'lat': info['currentLat'],
            'lon': info['currentLon'],
            'maxRange': self.__maxRange(info['battery'])
        }
        data.update(extraInfo)
        self.__cleanChannel()
        try:
            self.__db.push(data)
        except:
            print("No se ha podido conectar al canal")

    # Metodo para preparar al drone para empezar a volar
    def setReady(self):
        # Limpiar canal de comunicacion
        self.__cleanChannel()
        # Cambiar estado del drone
        self.__state = 'waiting'
        # Enivar instruccion por el canal
        self.__sendInformation('dro_ready')

    # Metodo para iniciar un viaje
    def setStartTrip(self, coords):
        
        self.__controller.takeoff()
        # Cambiar estado del drone
        self.__state = 'inProgress'

        # Enivar instruccion de vuelo
        self.__sendInformation('dro_initTrip')
        # Obtener inicio y final de viaje
        finalDestination = coords[-1]
        indexCoords = 0
        numberOfCords = len(coords)
        # Programa prinicipal para control de vuelo
        while(coords[indexCoords] != finalDestination):
                self.__controller.moveTo(coords[indexCoords+1][0], coords[indexCoords+1][1])
                # Se ha alcanazdo el punto geografico destino
                self.__sendInformation('dro_position', {"progressTrip": indexCoords/numberOfCords});
                indexCoords += 1
            # Terminar verificar altura
        #Inicia secuencia de aterrizaje
        print("Iniciando secuencia de ATERRIZAJE...")
        self.__controller.changeMode("LAND")
        # Se ha alcanzado el destino final
        self.__sendInformation('dro_position', {"progressTrip": 1.0});
        # ----------------------------------------
        # Cambiar estado del drone
        self.__state = 'waiting'
        self.__sendInformation('dro_reachDest')
    
    

    # -------------------------------------------------------------
    # Metodo donde se "escuchan" todos los items
    # agregados en el canal por la app y por el drone
    # aqui se recibe y se procesa cada instruccion
    def onInstruction(self, dataRecived):
        dataRec = dataRecived.data
        if(dataRec != None and 'ins' in dataRec):
            instruction = dataRec['ins']
            print(instruction)
            # Instruccion para inicializar drone
            if(instruction == 'app_prepared'):
                self.setReady()
            # Instruccion para solicitar posicion actual
            elif(instruction == 'app_position'):
                self.__sendInformation('dro_position')
            # Instruccion para inciar viaje
            elif(instruction == 'app_startTrip'):
                coords = dataRec['coordsForTrip']
                self.setStartTrip(coords)
