import threading
import time

class Stack:
    def __init__(self):
        self.pointer = -1
        self.data=[-1,-1,-1,-1,-1]

    def push(self,x):
        global condition
        condition.acquire()
        while self.pointer==len(self.data)-1:
            condition.wait()
        
        self.pointer+=1
        self.data[self.pointer]=x
        condition.notify()
        condition.release()

    def pop(self):
        global condition
        condition.acquire()
        while self.pointer == -1:
            condition.wait()
        x = self.data[self.pointer]
        self.pointer-=1
        condition.notify()
        condition.release()
        return x

def thread_producer():
    global stack
    for i in range(5):
        print('生产：{}'.format(i))
        stack.push(i)
        time.sleep(1)

def thread_consumer():
    global stack
    for i in range(5):
        x = stack.pop()
        print('消费：{}'.format(x))
        time.sleep(1)

if __name__ == "__main__":
    stack = Stack()
    condition = threading.Condition()

    producer = threading.Thread(target=thread_producer)
    producer.start()
    consumer = threading.Thread(target=thread_consumer)
    consumer.start()
