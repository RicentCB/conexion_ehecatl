from time import sleep
from gpiozero import DistanceSensor 

class Sensor:
    __MAX_DISTANCE = 3.0
    def __init__(self, echo, trigger):
        # Incializar pines
        self.__sensor = DistanceSensor(echo=echo, 
            trigger=trigger, 
            max_distance=self.__MAX_DISTANCE)
    
    def start(self):
        try:
            while True:
                distance = self.getDistance
                print("Distancia: ",'{:1.2f}'.format(distance) + " cm")
                sleep(0.5)
        except KeyboardInterrupt:
            pass
        finally:
            self.__sensor.close()

    # Metodo para obtener la distancia sensada
    @property
    def getDistance(self):
        return self.__sensor.distance * 100