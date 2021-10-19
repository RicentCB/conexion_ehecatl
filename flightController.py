# Clase que se encarga de la comunicacion con el controlador de vuelo
# a traves de comandos

class FlightController:
    __batery = 0        # Float: 0 - 1
    __currentLat = 0    # Float: Coorenda de latitud obtenida con el GPS Rango -100.0 - 100.0 
    __currentLon = 0    # Float: Coorenda de longitud obtenida con el GPS Rango -100.0 - 100.0

    def __init__(self):
        # TODO: Realizar conexion con controlador
        self.__batery = 0.95
        self.__currentLat = 19.5040103
        self.__currentLon = -99.1470982

    # Metodo para obtener datos del controlador
    @property
    def information(self):
        return {
            'battery': self.__batery,
            'currentLat': self.__currentLat,
            'currentLon': self.__currentLon,
        }