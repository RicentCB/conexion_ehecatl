from gpiozero import DistanceSensor 
from signal import signal, SIGTERM, SIGHUP, pause
from threading import Thread
from time import sleep

class Sensor(Thread):
    # Atributos estaticos
    __MAX_DISTANCE = 3.0
    __id = ''

    # Definicion de constructor
    def __init__(self, echo, trigger, id):
        # Guardar id
        self.__id = id
        # Incializar pines
        # self.__sensor = DistanceSensor(echo=echo, 
        #     trigger=trigger, 
        #     max_distance=self.__MAX_DISTANCE)
        # Incializar Hilo
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        while True:
            print(self.__id)
            sleep(0.25)
            # distance = self.getDistance
            # print(self.__id+'{:1.2f}'.format(distance) + " cm")
            
    
    # def start(self):
    #     try:
    #         signal(SIGTERM, self.__safe_exit)
    #         signal(SIGHUP, self.__safe_exit)

    #         self.__isReading = True
    #         reader = Thread(target=self.__readDistance, daemon=True)
    #         reader.start()

    #         pause() 
    #     except KeyboardInterrupt:
    #         pass
    #     finally:
    #         self.__sensor.close()

    # Metodo para obtener la distancia sensada
    # @property
    # def getDistance(self):
    #     return self.__sensor.distance * 100
    
    # def __safe_exit(self, signum, frame):
    #     exit(1)