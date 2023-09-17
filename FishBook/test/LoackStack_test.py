import threading
import time

from werkzeug.local import LocalStack

stack=LocalStack()# 线程隔离
stack.push(1)
print('in main thread after push,value is:'+str(stack.top))

def woker():
    print('in new thread before push,value is:' + str(stack.top))
    stack.push(2)
    print('in new thread after push,value is:' + str(stack.top))

new_thread=threading.Thread(target=woker,name='lin_thread')
new_thread.start()
time.sleep(1)

# 主线程
print('finally,in main thread value is '+ str(stack.top))

