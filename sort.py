import sort_lib as sort_lib
import sort_intersection as si
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import time 
#import datetime

fig, axs = plt.subplots(2, 2)

def createReverseArray(len):

    #return np.random.randint(900000, size=(arrayLen))

    newArr = [0] * len
    i = 0
    val = len
    while i < len:
        newArr[i] = val
        val -= 1;
        i += 1
    return newArr

def customPlot(arraySizeIncrement, loopCount, plx, ply):
    i = 1
    
    xpointsForIS = [0]
    ypointsForIS = [0]

    xpointsForMS = [0]
    ypointsForMS = [0]

    while i < loopCount:

        arrayLen = arraySizeIncrement * i

        xpointsForIS.append(arrayLen)
        xpointsForMS.append(arrayLen)

        arr = createReverseArray(arrayLen) 
        
        #startTime = datetime.datetime.now()    
        startTime = time.perf_counter_ns()
        sort_lib.insertionSort(arr)
        #elapsedTime = (datetime.datetime.now() - startTime).microseconds
        elapsedTime = time.perf_counter_ns() - startTime
        
        ypointsForIS.append(elapsedTime)

        arr = createReverseArray(arrayLen) # np.random.randint(900000, size=(arrayLen))
        
        #startTime = datetime.datetime.now()
        startTime = time.perf_counter_ns()
        sort_lib.mergeSort(arr, 0, (arrayLen - 1))
        #elapsedTime = (datetime.datetime.now() - startTime).microseconds    
        elapsedTime = time.perf_counter_ns() - startTime
        
        ypointsForMS.append(elapsedTime)

        i += 1

    narr_xpointsForIS = np.array(xpointsForIS)
    narr_xpointsForMS = np.array(xpointsForMS)
    
    title = "arraySizeIncrement:{} loopCount:{}".format(arraySizeIncrement, loopCount)
    axs[plx, ply].set_title(title)

    axs[plx, ply].set_xlabel('array size')

    axs[plx, ply].set_ylabel('time in nanoseconds')
    axs[plx, ply].yaxis.set_major_formatter(lambda x, pos: f'{x / 1e6:.1f}')
    axs[plx, ply].plot(narr_xpointsForIS, np.array(ypointsForIS), color='red', linestyle = 'dotted', marker='', label="Insertion")
    axs[plx, ply].legend()
    axs[plx, ply].plot(narr_xpointsForMS, np.array(ypointsForMS), color='blue', linestyle = 'dotted', marker='', label="Merge")
    axs[plx, ply].legend()

    xi , yi = si.intersection(narr_xpointsForIS, np.array(ypointsForIS), narr_xpointsForMS, np.array(ypointsForMS))

    axs[plx, ply].scatter(xi, yi, color='black')

customPlot(20, 30, 0, 0)
customPlot(10, 30, 0, 1)
customPlot(30, 30, 1, 0)
customPlot(5, 30, 1, 1)

plt.show()
