import  csv

def sort(x):
  
  for i in range(x):
    min_idx = i
    for j in range(i+1, len(x)):
      if x[min_idx][0] > x[j][0]:
        min_idx = j
    x[i], x[min_idx] = x[min_idx], x[i]
    print(i)



with open("employeelist.csv", "a") as file:
  for row in file:
    print(row)