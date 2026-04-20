import multiprocessing 
import threading

def job(a,b):
    print('和ejja')


if __name__=='__main__':   #processing's must
    t1=threading.Thread(target=job,args=(4,9))
    p1=multiprocessing.Process(target=job,args=(1,2))

    t1.start()
    p1.start()

    t1.join()
    p1.join()