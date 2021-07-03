import random
import time
from pythonosc import udp_client

# 127.0.0.1(IP) - 8080(port) 로 데이터를 send 하겠다.
client = udp_client.SimpleUDPClient('127.0.0.1', 57110)

# client = udp_client.SimpleUDPClient('192.168.1.34', 24000)
# client.send_message('/park', [100, 200, 300, 400])
# client.send_message('/byun', [100, 200, 300, 400])

id = 1000
while True:
    # 127.0.0.1 의 8080포트로 메시지 ('/filter', 100 ) 를 send
    # OSC 데이터는 '/tag', data1,data2,data3,data4.....
    client.send_message('/s_new', [ "sine", id, 0, 1, "freq", random.choice( [440,880,1320,220] ) ])
    id+=1
    time.sleep( random.choice( [0.5, 0.25, 0.125]  ))

