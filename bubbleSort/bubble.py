"""By John Boner 01/28/2020 for CSCT 212 S01"""

def bubbleSort(x):
    n = len(x)
    for i in range(n):
      for j in range(0, n-i-1):
        if x[j] > x[j+1] :
          x[j], x[j+1] = x[j+1], x[j]
 


if __name__ == "__main__":
  x = [64, 34, 25, 12, 22, 11, 90]
  
  bubbleSort(x)
  
  print ("Sorted xay is:")
  for i in range(len(x)):
      print (x[i])