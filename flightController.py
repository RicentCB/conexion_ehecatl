from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException

import time
import socket
import exceptions
import math
import argparse
# Clase que se encarga de la comunicacion con el controlador de vuelo
# a traves de comandos

class FlightController:
    __battery = 0        # Float: 0 - 1
    __currentLat = 0    # Float: Coorenda de latitud obtenida con el GPS Rango -100.0 - 100.0 
    __currentLon = 0    # Float: Coorenda de longitud obtenida con el GPS Rango -100.0 - 100.0
    __vehicle = object()    # Vehicle: Guarda el objeto vehículo donde se conecta
    __targetHeight = 4
    

    def __init__(self):
        # Realizar conexion con controlador
        #parser = argparse.ArgumentParser(description="commands")
        #parser.add_argument("--connect")
        #args = parser.parse_args()

        connection_string = "/dev/ttyAMA0" 
        baud_rate = 921600

        self.__vehicle = connect(connection_string, baud = baud_rate, wait_ready = True)

    # Getter: Bateria acutal del drone
    def __getBattery(self):
        volts = self.__vehicle.battery.voltage
        self.__battery = (2/3)(volts) - (7.4)
        return self.__battery

    # Getter posicion GPS actual
    def __getPosition(self):
        #Conexion GPS para obtener ubicacion
        global_pos = self.__vehicle.location.global_relative_frame
        self.__currentLat = global_pos.lat
        self.__currentLon = global_pos.lon

        currentPosition = (self.__currentLat, self.__currentLon)
        return currentPosition

    # Método que cambia el modo de vuelo del Pixhawk

    def changeMode(self, mode):
        self.__vehicle.mode = VehicleMode(mode)
        while self.__vehicle.mode != mode:
            print("Esperando a que se cambie a modo: "+mode)
            time.sleep(1)
        print("¡¡ Se cambio a modo: "+mode+" !!")

    # Método para hacer que el drone despegue
    def takeoff(self):
        
        self.changeMode()

        while not self.__vehicle.is_armable:
            print("Esperando a que el vehiculo sea armable...")
            time.sleep(1)
        print("Drone listo para armar!")

        self.__vehicle.armed = True

        #cmds = self.__vehicle.commands
        #cmds.download()
        #cmds.wait_ready()
        #self.__homeLocation = self.__vehicle.home_location

        while not self.__vehicle.armed:
            print("Esperando a que el vehiculo se arme...")
            time.sleep(1)

        print("Vehiculo armado")
        print("Despegando a : "+str(self.__targetHeight))

        self.__vehicle.simple_takeoff(self.__targetHeight)

        while self.__vehicle.location.global_relative_frame.alt < .95 * self.__targetHeight:
            print("ALTITUD ACTUAL: %d" %self.__vehicle.location.global_relative_frame.alt)
            time.sleep(1)

        print("Altitud alcanzada!")
    


    # Metodo prinicipal
    # Moviliza al drone dado un grupo de coordendas geograficas
    def moveTo(self, Lat, Lon):

        
        targetLocation = LocationGlobalRelative(float(Lat), float(Lon), self.__targetHeight)
        currentLoc = self.__vehicle.location.global_relative_frame

        distanceToTargetLocation = self.__get_distance_meters(targetLocation, currentLoc)

        self.__vehicle.simple_goto(targetLocation)

        print("Iniciando recorrido hacia: ("+str(targetLocation.lat)+", "+str(targetLocation.lon)+")")

        while self.__vehicle.mode.name == "GUIDED":
            currentDistance = self.__get_distance_meters(targetLocation, self.__vehicle.location.global_relative_frame)
            if currentDistance < distanceToTargetLocation * .01 :
                print("Punto alcanzado!")
                time.sleep(1)
                break
            time.sleep(1)
        
        


    def __get_distance_meters(self, targetLocation, currentLocation):
        dLat = targetLocation.lat - currentLocation.lat
        dLon = targetLocation.lon - currentLocation.lon

        return math.sqrt((dLon*dLon)+(dLat*dLat)) * 1.113195e5











    # Metodo para obtener datos del controlador
    @property
    def information(self):
        self.__getBattery()
        self.__getPosition()
        return {
            'battery': self.__battery,
            'currentLat': self.__currentLat,
            'currentLon': self.__currentLon,
        }