from FoxDot import Clock
from pythonosc import udp_client
import random

client = udp_client.SimpleUDPClient('127.0.0.1', 24000)

Clock.bpm = 60
Clock.clear()

def run_message():
    client.send_message('/draw', [])
    Clock.future(1, run_message)

run_message()

