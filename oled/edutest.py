import os, sys, time

# 상위 디렉토리 추가 (for utils.config)
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

# openpibo 라이브러리 경로 추가
sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo

def audio_test():
    pibo.play(filename=cfg.TESTDATA_PATH+"/test.mp3", out='local', volume=-2000)
    time.sleep(3)
    pibo.stop()

def neopixel_test():
    pibo.eye_on(0,255,0)
    time.sleep(2)
    
    pibo.eye_on(0,0,255,255,0,0)
    time.sleep(2)

    pibo.eye_on('aqua')
    time.sleep(2)

    pibo.eye_off()

def device_test():
    pibo.check_device('battery')

def motion_test():
    # 모터 1개 제어
    pibo.motor(2, 50, 20, 10)
    time.sleep(2)

    # 모터 여러개 제어
    pibo.motors(positions=[-10,-20,40,0,-10,50,20,20,40,70], speed=[0,0,7,0,80,50, 10,10,20,70], accel=[0,0,30,20,30,0,0,0,30,20])
    time.sleep(2)

    # 모터 여러개 제어(movetime)
    pibo.motors_movetime(positions=[0,0,30,20, 30,0, 0,0,30,20], movetime=1000)
    time.sleep(2)

    # 모션 종류 및 상세 정보 확인
    pibo.get_motion()
    print()
    pibo.get_motion('cheer3')
    time.sleep(2)

    # 모션 동작 수행
    pibo.set_motion('dance1', 1)

def oled_test():
    # 문자
    pibo.draw_text((10, 10), '안녕하세요. Hello', 15)
    pibo.show_display()
    time.sleep(2)
    pibo.clear_display()

    # 이미지 
    pibo.draw_image(cfg.TESTDATA_PATH +"/clear.png")
    pibo.show_display()
    time.sleep(2)
    pibo.clear_display()

    # 도형
    pibo.draw_figure((10,10,30,30), "rectangle", True)
    pibo.draw_figure((70,40,90,60), "동그라미", False)
    pibo.draw_figure((15,15,80,50), "line")
    pibo.show_display()
    time.sleep(2)
    pibo.invert()
    time.sleep(2)
    pibo.clear_display()

def speech_test():
    # 번역
    ret = pibo.translate('즐거운 금요일', 'en')
    print('translate output: ', ret)
    time.sleep(3)

    # TTS
    pibo.tts("<speak><voice name='MAN_READ_CALM'>안녕하세요.<break time='500ms'/></voice></speak>", "tts.mp3", "ko")
    time.sleep(5)

    # STT
    pibo.stt()
    time.sleep(5)

    # 대화
    ans = pibo.conversation('저녁 뭐먹지')
    print('pibo: ', ans)

def camera_test():
    # 스트리밍
    pibo.start_camera()
    time.sleep(3)
    pibo.stop_camera()

    time.sleep(3)

    # 캡처
    pibo.start_camera()
    time.sleep(3)
    pibo.capture()

    time.sleep(3)

    # 객체/qr/text 인식
    pibo.start_camera()
    time.sleep(3)
    obj = pibo.search_object()
    qr = pibo.search_qr()
    text = pibo.search_text()
    print("Search Object: ", obj)
    print("Search QR: ", qr)
    print("Search Text: ", text)

    time.sleep(3)

    # 얼굴 인식
    pibo.start_camera()
    time.sleep(3)
    face = pibo.search_face()
    print('face: ', face)

    time.sleep(3)

    # 얼굴 학습
    pibo.start_camera()
    time.sleep(3)
    pibo.train_face()
    


if __name__ == "__main__":
    pibo = Edu_Pibo()
    audio_test()
    # neopixel_test()
    # device_test()
    # motion_tset()
    # oled_test()
    # speech_test()
    # camera_test()






    