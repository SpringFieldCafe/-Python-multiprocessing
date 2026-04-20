import threading
import multiprocessing
import time

def job(q):
    res=0
    for i in range(10000000):
        res+=i+i**2+i**3
    q.put(res)


def mulcore():
    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=job,args=(q,))
    p2=multiprocessing.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1=q.get()
    res2=q.get()
    print('multicore:',res1+res2)

def normal():
    res=0
    for j in range(2):
        for i in range(10000000):
            res+=i+i**2+i**3
    print('normal:',res)

def multithread():
    q=multiprocessing.Queue()
    t1=threading.Thread(target=job,args=(q,))
    t2=threading.Thread(target=job,args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1=q.get()
    res2=q.get()
    print('multithread:',res1+res2)

if __name__=='__main__':
    st=time.time()
    normal()
    s1=time.time()
    print('normal:',s1-st)
    st=time.time()
    mulcore()
    s2=time.time()
    print('mulcore:',s2-st)
    st=time.time()
    multithread()
    s3=time.time()
    print('multithread',s3-st)
    