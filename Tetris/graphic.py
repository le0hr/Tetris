from pynput.keyboard import Key,  Events, Listener
import time

v = 0

while True:
    def on_press():
        print('Нажато')
    listener = Listener(on_press=on_press)
    listener.start()
    print('не нажато')