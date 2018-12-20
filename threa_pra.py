#coding:utf-8
import threading
import time
import thread


lock=threading.Lock()
rlock=threading.RLock()
con=threading.Condition()
num=0

data=1


class Producer(threading.Thread):
    def __init__(self):
        #super(Producer,self).__init__(self)
        threading.Thread.__init__(self)

    def run(self):
        global num
        con.acquire()
        while True:
            print "开始生产："
            num+=1
            print "现有鱼丸个数：%s"%str(num)
            time.sleep(1)

            if num>5:
                print "鱼丸个数已超过5个，无需继续生产"

                con.notify()
                print "Producer Notifing。。"
                con.wait()
                print "Producer waiting finished"
                print "waiting continue"
#wait之后，当前线程将暂停，并保存当前环境，下一个notify执行时，会接着下面的部分执行
        print "produce release start\n"
        con.release()
        print "produce release end\n"

class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print "<<<<consumer acquire>>>>"
        con.acquire()
        print "<<consumer acquire   step in >> >"
        global num
        while True:
            print "开始消费："
            num-=1
            print "剩余鱼丸个数：%s"%str(num)
            time.sleep(2)
            if num<1:
                print "鱼丸么有啦，需要制作"

                con.notify()
                print "Consumer notifing"
                con.wait()
                print "consumer waiting"
        print "consumer release start "
        con.release()
        print "consumer release end"



semaphore=threading.Semaphore(2)
#bouded信号量有大小的限制，不能超过初始设置的值，release后可以+1，主线程如果release了，容易出现异常，因为主线程可以不获取的情况下，去release信号量,如果主线程acquire则不会出现
#semaphore=threading.BoundedSemaphore(2)
def func_sem():
    print "%s acquire semaphore"%threading.currentThread().getName()
    if semaphore.acquire():
        print "%s get the semaphore"%threading.currentThread().getName()
        time.sleep(4)

        print "%s release the semaphore"%threading.currentThread().getName()
        semaphore.release()







def p_time():
    print time.strftime('%Y-%m-%d %H:%M:%S')

def func1():
    print "func1 is runing!\n"


def func_join(t_input,testdata=[]):
    print "in func_join\n"
    p_time()
    t_input.start()

    t_input.join()

    print "out join"
    p_time()
    print testdata


def Inner_Join():
    print "Start Function Inner_join"
    time.sleep(10)
    print "Stop Function Inner_join"



class MyThred(threading.Thread):
    def run(self):
        print "MyThread is running!"




def Lock_Fun():
    global data
    #print "In lock function:"

    if lock.acquire():

        print "%s get the lock."%threading.currentThread().getName()
        data+=1
        time.sleep(1)
        print "%s release the lock."%threading.currentThread().getName()
        lock.release()


def Rlock_Fun():
    print "%s is acquiring rlock"%threading.currentThread().getName()
    if rlock.acquire():
        print "%s get the rlock"%threading.currentThread().getName()
        time.sleep(2)

        print "%s acquiring again"%threading.currentThread().getName()
        if rlock.acquire():
            print "%s get the rlock again"%threading.currentThread().getName()

            time.sleep(2)

        print "Release lock"
        rlock.release()
        time .sleep(2)
        print "Release lock again"
        rlock.release()
        time.sleep(2)

def func_time():
    p_time()
    print "hello timer"
event=threading.Event()

def func_Event():
    print "%s wait for event"%threading.currentThread().getName()
    event.wait()

    print "%s recv event"%threading.currentThread().getName()

local=threading.local()
local.tname='main'
def func_local():
    local.tname='not main'
    print local.tname



alist=None

condition=threading.Condition()


def doSet():
    if condition.acquire():
        while alist is None:
            condition.wait()
        for i in range(len(alist))[::-1]:
            alist[i]=1

        condition.release()


def doPrint():
    global alist
    if condition.acquire():
        while alist is None:
            condition.wait()
        for i in alist:
            print i,
        print
        condition.release()

def doCreate():
    global alist
    if condition.acquire():
        if alist is None:
            alist=[0 for i in range(10)]
            condition.notifyAll()

        condition.release()


if __name__=="__main__":
    '''
    t1 = threading.Thread(target=func1)
    t1.start()

    t2=MyThred()
    t2.start()

    print "t3"
    t3=thread.start_new(func1,())
    '''
    '''
#threading join 
    t1=threading.Thread(target=Inner_Join)
    t2=threading.Thread(target=func_join,args=(t1,),kwargs={'testdata':[1,2]})
    t2.start()
    '''
    '''
    #threading Rlock

    tm=threading.Thread(target=Rlock_Fun)
    tn=threading.Thread(target=Rlock_Fun)
    tq=threading.Thread(target=Rlock_Fun)
    tm.start()
    tn.start()
    tq.start()
    '''

    '''
    #threading_lock
    tm=threading.Thread(target=Lock_Fun)
    tn=threading.Thread(target=Lock_Fun)
    tq=threading.Thread(target=Lock_Fun)
    tp=threading.Thread(target=Lock_Fun)
    tm.start()
    tn.start()
    tq.start()

    tp.start()
    '''
    '''
    print Producer.mro()
    p=Producer()
    c=Consumer()
    p.start()
    c.start()
    '''

    '''
    t1=threading.Thread(target=func_sem)
    t2=threading.Thread(target=func_sem
                        )
    t3=threading.Thread(target=func_sem)
    t4=threading.Thread(target=func_sem)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    time.sleep(2)

    print "main thread release sempahore without acquire"
    #semaphore.acquire()#主线程可不acquire就去release信号量
    semaphore.release()
    '''
    '''
    p_time()
    t_timer=threading.Timer(5,func_time)
    t_timer.start()
    '''

    '''
    t1=threading.Thread(target=func_Event)
    t2=threading.Thread(target=func_Event)
    t1.start()
    t2.start()
    time.sleep(2)
    print "main thread set event"
    event.set()
    '''


    '''
    t=threading.Thread(target=func_local)
    t.start()
    t.join()
    print dir(local)
    print local.tname
    '''
    tset=threading.Thread(target=doSet,name='tset')
    tprint=threading.Thread(target=doPrint,name='tprint')
    tcreate=threading.Thread(target=doCreate,name='tcreate')
    tset.start()
    tprint.start()
    tcreate.start()
