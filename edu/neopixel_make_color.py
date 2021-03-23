import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo


def make_color():
    pibo = Edu_Pibo()

    print("Start colorDB: ", pibo.get_colordb())

    # Make_color
    ret = pibo.make_color("black", (1, 1, 1))   # 기본으로 제공하는 목록에 있는 컬러
    print(ret)
    pibo.make_color("brown", (150,75,0)) 

    # Save DB
    pibo.save_colordb('./new_colordb')
    pibo.load_colordb('new_colordb')
    print("Add lime: ", list(pibo.get_colordb()[1].keys()))

    # Make_color2
    pibo.make_color("lime", (191,255,0))
    pibo.save_colordb('./new_colordb')
    pibo.load_colordb('new_colordb')
    print("Add brown: ", list(pibo.get_colordb()[1].keys()))
    
    # Delete color
    pibo.delete_color("brown")
    pibo.save_colordb('./new_colordb')
    pibo.load_colordb('new_colordb')
    print("Delete lime: ", list(pibo.get_colordb()[1].keys()))

    pibo.eye_on('lime')
    time.sleep(2)
    pibo.eye_off()
   
   
if __name__ == "__main__":
    make_color()