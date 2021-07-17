# tested with oscP5 0.9.9 and 2.0.4
add_library('oscP5') 
 
# Circle 클래스 정의
class Circle:
    def __init__(self):
        self.x = random(0, width)
        self.y = random(0, height*0.5)
        self.color = color(random(255), random(255), random(255))
        self.alpha = 255
    def display(self):
        fill(self.color, self.alpha)
        ellipse(self.x, self.y, 40, 40)
        self.alpha -= 4
        self.y += 1
    def isDead(self):
        return self.alpha < 0
                            
circles = []
 
# OSC dispatcher  
class Listen(OscEventListener): 
    def oscEvent(self,m):
        # OSC 메시지가 날라오면 Circle 객체 생성 후 circles 리스트에 삽입
        global circles
        data = m.arguments()
        if data[0] > 400:
            circles.append(Circle())
 
def setup():
    global osc
    size(600, 600)
    osc = OscP5(this, 24000)  # 24000포트 오픈
    osc.addListener(Listen()) # assigning a listener to class Listen

def draw():
    background(0)
    for c in circles[:]: #circles 리스트에 저장된 Circle 객체를 하나씩 꺼내서
        c.display()  # display 메서드 전달
        if c.isDead(): # Circle 객체가 dead(self.alpha 가 0보다 작다면) 했다면
            circles.remove(c) # circles 리스트에서 제거 

def stop():
    global osc
    osc.dispose()
