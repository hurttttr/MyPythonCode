import time
import threading

ticket = 5

class MyThread(threading.Thread):
    def __init__(self,name = None):
        super().__init__(name =name )
    
    def run(self):
        global ticket,lock
        while ticket>0:
            lock.acquire()
            if ticket>0:
                t = threading.current_thread()
                print('{}:卖出{}号票'.format(t.name,ticket))
            ticket-=1
            lock.release()
            time.sleep(1)
    
if __name__ == "__main__":
    lock = threading.Lock()
    t1 = MyThread('窗口1')
    t1.start()
    t2= MyThread("窗口2")
    t2.start()