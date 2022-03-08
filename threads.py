import threading
from time import sleep

""" print(threading.active_count())
print(threading.enumerate())
print(threading.enumerate()[0].name)
print(threading.enumerate()[0].is_alive()) """

def wait():
    sleep(2)
    while True:
        print('Talismar')

t = threading.Thread(target=wait, name="Wait")
t.start()