"""By John Boner 01/28/2020 for CSCT 212 S01"""
from random import *
def bubbleSort(x, y = "A"):
  c = 0
  s = 0
  n = len(x)
  for i in range(n):
    for j in range(0, n-i-1):
      c += 1
      if y == "A":
        if x[j] > x[j+1] :
          x[j], x[j+1] = x[j+1], x[j]
          s += 1
      elif y == "D":
        if x[j] < x[j+1] :
          x[j], x[j+1] = x[j+1], x[j]
          s += 1
  return (x, c, s)


if __name__ == "__main__":
  userInput = input("how many numbers to generate and sort?: ")
  sortStyle = input("(A)scending or (D)escending?: ").upper()
  arr = [randint(1,100) for i in range(int(userInput))]
  print(arr)
  bubble = bubbleSort(arr, sortStyle)
  print(bubble[0])
  print(bubble[1])
  print(bubble[2])
  print("\n")
  sentence = input("Enter a sentence: ")
  bubbleTwo = bubbleSort(list(sentence))
  string = ""
  for i in bubbleTwo[0]:
    string += i
  print(string)

