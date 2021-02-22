import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo


def motors_test():
    pibo = Edu_Pibo()
    while True:
        pibo.motors(
            positions=[-10,-20,40,0,-10,50,20,20,40,70], 
            speed=[0,0,7,0,80,50, 10,10,20,70], 
            accel=[0,0,30,20,30,0,0,0,30,20]
        )
        time.sleep(1)

        pibo.motors(
            positions=[10,20,-40,0,10,-50,-20,-20,-40,-70], 
            speed=[10,30,5,15,20,80, 20,10,20,50], 
        )
        time.sleep(1)

if __name__ == "__main__":
    motors_test()