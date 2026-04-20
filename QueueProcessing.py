import multiprocessing
import threading
import queue

def job1(q,a,d):
    res=0
    for i in range(1000):
        res+=i+i**2
    q.put(res)



def job2(q):
    w=0
    lock=threading.Lock()
    def subjob1(q):
        nonlocal w,lock
        lock.acquire()
        for i in range(1,10):
            w+=i
            print(w)
        q.put(w)
        lock.release()

    def subjob2(q):
        nonlocal w,lock
        lock.acquire()
        for j in range(10,101,10):
            w+=j
            print(w)
        q.put(w)
        lock.release()


    t1=threading.Thread(target=subjob1,args=(q,))
    t2=threading.Thread(target=subjob2,args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    q.put(w)


if __name__=='__main__':
    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=job1,args=(q,3,5))
    p2=multiprocessing.Process(target=job2,args=(q,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    res1=q.get()
    res2=q.get()
    print(res1,res2)