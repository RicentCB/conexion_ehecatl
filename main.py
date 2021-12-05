from drone import Drone
import sys

def main():
    kMaxHeightDrone = 4
    if len(sys.argv) > 1:
        kMaxHeightDrone = int(sys.argv[1])
    
    Drone1 = Drone(kMaxHeightDrone)

if __name__ == '__main__':
    main()