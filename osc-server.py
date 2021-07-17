from pythonosc import osc_server
from pythonosc import dispatcher
from pythonosc import udp_client

# OSC 메시지 처리를 위한 Dispatcher 객체 생성
dispatcher = dispatcher.Dispatcher()

# SuperCollider 로 메시지를 보내기 위한 OSC 클라이언트
client = udp_client.SimpleUDPClient('127.0.0.1', 57110)

# processing 로 메시지는 보내기 위한 OSC 클라이언트
p5 = udp_client.SimpleUDPClient('127.0.0.1', 24000)

# maxmsp 로 메시지는 보내기 위한 OSC 클라이언트
maxmsp = udp_client.SimpleUDPClient('127.0.0.1', 2000) #2000이 아닐 수 있음. maxmsp에서 확인하기

# OSC 메시지 처리 함수들
def filter_handle(addr, filter1, filter2):
    print('receive filter message:', addr, filter1, filter2)

def amp_handle(addr, amp):
    print('receive amp message:', addr, amp)

id = 1000

def scsynth(addr, freq):
    global id, client
    # SuperCollider 로 메시지 보내기
    client.send_message('/s_new', [ "sine", id, 0, 1, "freq", freq ])
    p5.send_message("/message", [freq])
    id += 1


# OSC 메시지별 처리 함수 등록
dispatcher.map('/filter', filter_handle)
dispatcher.map('/amp', amp_handle)
dispatcher.map('/scsynth', scsynth)
dispatcher.map('/eye_left', filter_handle)

# 서버 세팅 ( 서버 주소 설정 및 서버로 메시지가 전달될때 처리할 Dispatcher 등록)
osc_server = osc_server.ThreadingOSCUDPServer(('127.0.0.1', 2000), dispatcher)

# 서버 런
osc_server.serve_forever()

