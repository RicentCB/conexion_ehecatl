from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from gpiozero import DistanceSensor, Buzzer

class DistanceSensor:
    def __init__(self):
        try:
            signal(SIGTERM, safe_exit)
            signal(SIGHUP, safe_exit)

            sensor.when_in_range = buzzer.on
            sensor.when_out_of_range = buzzer.off

            pause()

        except KeyboardInterrupt:
            pass