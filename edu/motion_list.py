import os, sys, time, pprint

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo

def audio_test():
    pibo = Edu_Pibo()
    motion_list = pibo.get_motion()
    print(motion_list[1])

    time.sleep(0.5)
    print('모션을 입력하면 해당 모션의 정보를 조회할 수 있습니다.(q: 나가기)')
    user_input = input('입력: ')
    
    if user_input == 'q':
        return
    info = pibo.get_motion(user_input)
    pprint.pprint(info[1])

if __name__ == "__main__":
    audio_test()