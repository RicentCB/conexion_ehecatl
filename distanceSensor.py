from gpiozero import DistanceSensor 
from signal import signal, SIGTERM, SIGHUP, pause
from threading import Thread
from time import sleep

class Sensor:
    # Atributos estaticos
    __MAX_DISTANCE = 3.0
    __isReading = False

    # Definicion de constructor
    def __init__(self, echo, trigger):
        # Incializar pines
        self.__sensor = DistanceSensor(echo=echo, 
            trigger=trigger, 
            max_distance=self.__MAX_DISTANCE)

    def __readDistance(self):
        while self.__isReading:
            distance = self.getDistance
            print('{:1.2f}'.format(distance) + " cm")
            sleep(0.5)
    
    def start(self):
        try:
            signal(SIGTERM, self.__safe_exit)
            signal(SIGHUP, self.__safe_exit)

            self.__isReading = True
            reader = Thread(target=self.__readDistance, daemon=True)
            reader.start()

            pause() 
        except KeyboardInterrupt:
            pass
        finally:
            self.__sensor.close()

    # Metodo para obtener la distancia sensada
    @property
    def getDistance(self):
        return self.__sensor.distance * 100
    
    def __safe_exit(self, signum, frame):
        exit(1)