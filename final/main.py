from bs4 import BeautifulSoup as bs
import requests
import os, sys, time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

sys.path.append(cfg.OPENPIBO_PATH + '/edu')
from pibo import Edu_Pibo

weather_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"

def play_tts(play_words):
    print('play_tts')
    filename = cfg.TESTDATA_PATH+"/tts.mp3"
    return_text = "<speak><voice name='WOMAN_READ_CALM'> {} <break time='500ms'/></voice></speak>".format(play_words)
    pibo.tts(return_text, filename, "ko")
    pibo.play_audio(filename, out='local', volume=-1500, background=False)

def bot_weather():
    print('bot_weather')
    pibo.draw_image(cfg.TESTDATA_PATH + "/icon/weather_bot.png")
    pibo.show_display()
    
    html = requests.get(weather_url)

    soup = bs(html.text, 'html.parser')
    main_data = soup.find('div', {'class': 'main_info'})

    today_temp = main_data.find('span', {'class': 'todaytemp'}).text
    today_feel_temp = main_data.find('p', {'class':'cast_txt'}).text
    today_weather = "오늘 기온은 {}°, {}.".format(today_temp, today_feel_temp)
    play_tts(today_weather)

def bot_picture():
    print('bot_picture')
    pibo.draw_image(cfg.TESTDATA_PATH + "/icon/camera.png")
    pibo.show_display()

    face = pibo.detect_face()
    print(face[1])

    if face[0]:
        print('have face')
    else:
        pibo.capture()
        time.sleep(3)
        pibo.draw_image("/home/pi/openpibo-example/final/capture.png")
        pibo.show_display()

def bot_walk(bot_keywords):
    print('bot_walk')
    pibo.draw_image(cfg.TESTDATA_PATH + "/icon/walk.png")
    pibo.show_display()
    
    motions_db = {
        "앞" : "forward1",
        "뒤" : "backward1",
        "왼쪽" : "left",
        "오른쪽" : "right"
    }

    go_motion = "stop"
    for motion in motions_db:
        if motion in bot_keywords:
            go_motion = motions_db[motion]

    pibo.set_motion(go_motion, 4)
    pibo.set_motion("stop", 1)

bot_db ={
    '날씨' : bot_weather,
    '사진' : bot_picture,
    '걸어' : bot_walk,
}

def check_words(bot_keywords):
    print('check_words')
    matched = False

    for item in bot_db:
        if item in bot_keywords:
            matched = True
            
            if item == '걸어':
                bot_db[item](bot_keywords)
            else:
                bot_db[item]()

    if matched ==False:
        ans = pibo.conversation(bot_keywords)
        play_tts(ans[1])

def start_listen():
    print('start_listen')
    pibo.set_motion("lookup", 1)

    pibo.stop_camera()

    pibo.draw_image(cfg.TESTDATA_PATH + "/icon/mic.png")
    pibo.show_display()

    ret = pibo.stt()

    print('pibo stt : {}'.format(ret[1]))

    if "no result" not in ret[1] :
        pibo.draw_image(cfg.TESTDATA_PATH + "/icon/check.png")
        pibo.show_display()

        check_words(ret[1])
    else:
        check_person()
        

def check_person():
    print('check_person')
    pibo.start_camera()
    time.sleep(1)
    face = pibo.search_face()

    if face[0] : 
        print('have face')
        return 1
    else:
        return 0

def msg_device(msg):
    print('msg_device')
    print(msg)
    #check_dev = msg.split(": ")[1]

    if "person" in msg["PIR"]:
        get_face = check_person()
        if get_face:
            start_listen()

def device_thread_test():
    print('device_thread_test')
    # pibo.start_devices(msg_device)

    while True:
        _,ret = pibo.check_device("system")
        msg_device(ret)
        time.sleep(1)

if __name__ == "__main__":
    pibo = Edu_Pibo()
    greeting = "안녕! 난 파이보야."

    pibo.draw_image(cfg.TESTDATA_PATH + "/icon/pibo_logo.png")
    pibo.show_display()

    play_tts(greeting)
    pibo.set_motion("welcome", 1)
    pibo.set_motion("stop", 1)

    device_thread_test()
