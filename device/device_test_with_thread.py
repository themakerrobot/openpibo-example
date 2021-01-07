'''
+ 메시지 구조
 - VERSION(10) ->  ex) #10:!
 - HALT(11) -> ex) #11:!
 - DC_CONN(14) -> ex) #14:!
 - BATTERY(15) -> ex) #15:!
 - PIR(30) -> ex) #30:!
 - TOUCH(31) -> ex) #31:!
'''
import os
import sys

# 상위 디렉토리 추가 (for utils.config)
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

# openpibo 라이브러리 경로 추가
sys.path.append(cfg.OPENPIBO_PATH + '/lib')
from device.devicelib import cDevice

import time
from threading import Thread, Lock

obj = cDevice()
next_cmd = [False, ""]

def decode_pkt(pkt):
  print("Recv:", pkt)

def update():
  system_check_time = time.time()
  battery_check_time = time.time()

  while True:
    if next_cmd[0] == True:
      data = obj.send_raw(next_cmd[1])
      decode_pkt(data)

    if time.time() - system_check_time > 1:  # 시스템 메시지 1초 간격 전송
      data = obj.send_cmd(obj.code['SYSTEM'])
      decode_pkt(data)
      system_check_time = time.time()

    if time.time() - battery_check_time > 10: # 배터리 메시지 10초 간격 전송
      data = obj.send_cmd(obj.code['BATTERY'])
      decode_pkt(data)
      battery_check_time = time.time()

    time.sleep(0.1)

if __name__ == "__main__":
  obj.send_cmd(obj.code['PIR'], "on")

  t = Thread(target=update, args=())
  t.daemon = True
  t.start()

  while True:
    pkt = input("")
    if pkt == 'q':
      break

    # 메시지를 처리하고 있다면, 다음 메시지 목록에 등록
    if obj.locked() == True:
      next_cmd = [True, pkt]
      continue

    next_cmd = [False, ""]
    data = obj.send_raw(pkt)

    print(data)

