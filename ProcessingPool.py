import multiprocessing

def job(x):
    return x*x

def multicore():
    pool=multiprocessing.Pool()
    res=pool.map(job,range(10))
    res=pool.apply_async(job,(2,))
    print(res.get())
    multi_res=[pool.apply_async(job,(i,)) for i in range(10)]
    print([res.get() for res in multi_res])

if __name__=='__main__':
    multicore()