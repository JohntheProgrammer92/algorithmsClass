""" John Boner - sort II"""
from time import *
from random import *
from copy import *
import numpy as np
import  matplotlib.pyplot as plt

def mkList(x,y):
    """takes user input and creates a 2d array"""
    arrs = []
    for i in range(x):
        numbs = []
        for j in range(y):
            numbs.append(randint(1 ,1000))
        arrs.append(numbs)
    return arrs

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selectionSort(arr):
    for i in range(len(arr)): 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]: 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key

def nativeSort(arr):
    return arr.sort()


def plotDictionary(times, title):
    plotTimes = []
    plotNames = []
    for key in times:
        plotTimes.append(times[key])
        plotNames.append(key)
    N = len(plotNames)
    ind = np.arange(N)
    width = .25
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, plotTimes, width, color='r')
    ax.set_ylabel('Time')
    ax.set_title(title)
    ax.set_xticks(ind + width)
    ax.set_xticklabels(plotNames)
    plt.show()

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose 

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, *args):
        self.end = time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000 
        if self.verbose:
            print ('elapsed time: %f ms' % self.msecs)

    def GetTime(self):
        return self.msecs

if __name__ == "__main__":
    while True:
        timeDict = {}
        t = Timer(True)         
        numLists = input("Enter the number of arrays you would like to sort: ")
        if numLists.isdigit():
            numNumbers = input("Enter the number of random numbers per array to sort: ")
            if numNumbers.isdigit():
                print("\n\nBegin sorting...")
                arr = mkList(int(numLists),int(numNumbers))
                with t:
                    for i in (deepcopy(arr)):
                        bubbleSort(i)
                print("Bubble sort complete!\n")
                timeDict['bubble'] = t.GetTime()
                with t:
                    for j in (deepcopy(arr)):
                        selectionSort(j)
                print("Selection sort complete!\n")
                timeDict['selection'] = t.GetTime()
                with t:
                    for k in (deepcopy(arr)):
                        insertionSort(k)
                print("Insertion sort complete!\n")
                timeDict['insertion'] = t.GetTime()
                with t:
                    for l in (deepcopy(arr)):
                        nativeSort(l)
                print("Native sort complete!\n")
                timeDict['native'] = t.GetTime()
                sentinel = input("Enter 'Q' to quit or any other key to continue: ").upper()
                if sentinel =="Q":
                    break
                print("")
            else:
                print("Incorrect data type please start over.")
        else:
            print("Please input an interger.")

    plotDictionary(timeDict, 'Num List: '+str(numLists)+' Nums per list: '+str(numNumbers))
