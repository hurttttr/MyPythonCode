import threading
import time

def thread_body():
    t = threading.current_thread()
    print('线程{}开始'.format(t.name))
    while True:
        print('Hello, World')
        time.sleep(1)

t1 = threading.Thread(target=thread_body)
t1.start()