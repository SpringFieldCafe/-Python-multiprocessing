import multiprocessing
import time

def job(v,num,l):
    l.acquire()
    for i in range(10):
        time.sleep(0.3)
        v.value+=num
        print(v.value)
    l.release()

def multicore():
    l=multiprocessing.Lock()
    v=multiprocessing.Value('i',0)
    p1=multiprocessing.Process(target=job,args=(v,1,l))
    p2=multiprocessing.Process(target=job,args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__=='__main__':
    multicore()