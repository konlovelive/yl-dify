import threading
import time

from werkzeug.local import Local

stack = Local()  # 线程隔离
stack.b = 1


def woker():
    stack.b = 2
    print('in new thread,value is:' + str(stack.b))  # 这种写法有误，函数woker里无法识别stack


new_thread = threading.Thread(target=woker, name='lin_thread')
new_thread.start()
time.sleep(1)

# 主线程
print('in main thread, value is ' + str(stack.b))

