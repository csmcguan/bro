import os
import sys
import multiprocessing as mp
import numpy as np 

def load_trace(f):
    return np.loadtxt(f, delimiter="\t")

def simulate(f):
    trace = load_trace(f)
    outgoing = trace[np.where(trace[:,1] == 777)]
    incoming = trace[np.where(trace[:,1] == -777)]
    outgoing = outgoing[outgoing[:,0].argsort(kind="mergesort")]
    incoming = incoming[incoming[:,0].argsort(kind="mergesort")]
    if len(outgoing) == 0:
        out_rng = 0
    else:
        q75, q25 = np.percentile(outgoing[:,0], [75, 25])
        out_rng = q75 -q25
    if len(incoming) == 0:
        in_rng = 0
    else:
        q75, q25 = np.percentile(incoming[:,0], [75, 25])
        in_rng = q75 -q25
    return [out_rng, in_rng]

def parallel(flist, n_jobs=25):
    pool = mp.Pool(n_jobs)
    arr = pool.map(simulate, flist)
    return arr

if __name__ == '__main__':
    fdir = os.path.join("defended", sys.argv[1])
    flist  = []
    for f in os.listdir(fdir):
        flist.append(os.path.join(fdir, f))

    arr = parallel(flist)
    arr = list(zip(*arr))
    arr = list(arr[0]) + list(arr[1])
    arr = np.array(arr)
    print("{} clustering".format(sys.argv[1]))
    print("================================")
    print("mean iqr:\t{:.4f}".format(arr.mean()))
    print("median iqr:\t{:.4f}".format(np.median(arr)))
    print("max iqr:\t{:.4f}".format(arr.max()))
    print("std dev:\t{:.4f}".format(arr.std()))
    print()
