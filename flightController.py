# Clase que se encarga de la comunicacion con el controlador de vuelo
# a traves de comandos

class FlightController:
    __battery = 0        # Float: 0 - 1
    __currentLat = 0    # Float: Coorenda de latitud obtenida con el GPS Rango -100.0 - 100.0 
    __currentLon = 0    # Float: Coorenda de longitud obtenida con el GPS Rango -100.0 - 100.0

    def __init__(self):
        # TODO: Realizar conexion con controlador
        self.__battery = 0.95
        self.__currentLat = 19.5040103
        self.__currentLon = -99.1470982

    # Getter: Bateria acutal del drone
    @property
    def getBattery(self):
        #TODO: OBtener bateria
        return self.__battery

    # Mok setear gps
    def setPosition(self, lat, lon):
        self.__currentLat = lat;
        self.__currentLon = lon;

    # Getter posicion GPS actual
    @property
    def getPosition(self):
        #TODO:
        lat = 19.5040103
        lon =  -99.1470982
        currentPosition = (lat, lon)
        return currentPosition

    # Metodo para obtener datos del controlador
    @property
    def information(self):
        return {
            'battery': self.__battery,
            'currentLat': self.__currentLat,
            'currentLon': self.__currentLon,
        }