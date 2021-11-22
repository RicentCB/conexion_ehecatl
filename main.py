from drone import Drone
from distanceSensor import Sensor

from threading import Thread

class myClassA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            print("A")

class myClassB(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            print("B")

def main():
    # Drone1 = Drone()
    # Sensor1 = Sensor(20, 21, 'S1')
    # Sensor2 = Sensor(19, 26, 'S2')
    # Sensor1.start()
    # Sensor2.start()
    myClassA()
    myClassB()
    while True:
        pass


if __name__ == '__main__':
    main()