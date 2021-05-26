import threading
import time

class MyThread(threading.Thread):
    def __init__(self):
        super().__init__(name=None)

    def run(self):
        t = threading.current_thread()
        print('线程{}开始'.format(t.name))
        for i in range(10):
            print('Hello, World')
            time.sleep(1)
        print('线程{}结束'.format(t.name))

t = MyThread()
t.start()