
def bubbleSort(x):
    n = len(x)
    for i in range(n):
      for j in range(0, n-i-1):
        if x[j] > x[j+1] :
          x[j], x[j+1] = x[j+1], x[j]
 

x = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(x)
 
print ("Sorted xay is:")
for i in range(len(x)):
    print ("%d" %x[i]),