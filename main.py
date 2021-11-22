from drone import Drone
from distanceSensor import Sensor

def main():
    # Drone1 = Drone()
    Sensor1 = Sensor(20, 21)
    Sensor2 = Sensor(19, 26)
    Sensor1.start()
    Sensor2.start()


if __name__ == '__main__':
    main()