from drone import Drone
from distanceSensor import DistanceSensor

def main():
    # Drone1 = Drone()
    Sensor1 = DistanceSensor(20, 21)
    Sensor1.start()


if __name__ == '__main__':
    main()