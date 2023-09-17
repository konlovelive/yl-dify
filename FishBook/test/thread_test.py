
import threading


def worker():
    print('i am thread')
    t=threading.current_thread()
    print(t.getName())

t=threading.current_thread()
print(t.getName())# 主线程名会显示：MainThread

# 定义一个新的线程，线程名默认为Thread-1
new_t=threading.Thread(target=worker,name='lin-Thread')# 指定线程的目标函数和线程名
# 线程启动
new_t.start()