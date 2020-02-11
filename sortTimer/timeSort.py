from time import *
from random import *
from copy import *

def mkList(x,y):
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
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose 

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, *args):
        self.end = time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print ('elapsed time: %f ms' % self.msecs)
    

if __name__ == "__main__":
    while True:            
        numLists = input("Enter the number of arrays you would like to sort: ")
        if numLists.isdigit():
            numNumbers = input("Enter the number of random numbers per array to sort: ")
            if numNumbers.isdigit():
                print("\n\nBegin sorting...")
                arr = mkList(int(numLists),int(numNumbers))
                bubArr = deepcopy(arr)
                with Timer(True):
                    for i in (bubArr := deepcopy(arr)):
                        bubbleSort(i)
                print("Bubble sort complete!\n")
                with Timer(True):
                    for j in (selectArr := deepcopy(arr)):
                        bubbleSort(selectArr)
                print("Selection sort complete!\n")
                with Timer(True):
                    for k in (insertArr := deepcopy(arr)):
                        bubbleSort(insertArr)
                print("insertion sort complete!\n")
                sentinel = input("Enter 'Q' to quit or any other key to continue: ").upper()
                if sentinel =="Q":
                    break
                print("")
            else:
                print("Incorrect data type please start over.")
        else:
            print("Please input an interger.")
