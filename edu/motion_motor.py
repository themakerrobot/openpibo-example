import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo


def motor_test():
    pibo = Edu_Pibo()
    while True:
        pibo.motor(2, 50, 20, 10)
        pibo.motor(8, -50, accel=40)
        time.sleep(1)

        pibo.motor(2, -50, speed=200)
        pibo.motor(8, 50)
        time.sleep(1)

if __name__ == "__main__":
    motor_test()