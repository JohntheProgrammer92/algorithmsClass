def sort(csv):
    if csv.split('.')[-1] == "csv":
        data = open(csv)
        # sorts data at init using a selection sort
        data.read()
        for line in data:
            array = line
            for i in range(len(array)):
                min_idx = i
                for j in range(i+1, len(array)):
                    if array[min_idx] > array[j]:
                        min_idx = j
                array[i], array[min_idx] = array[min_idx], array[i]
        newCSV = open("Sort.csv", "a")
    

        
        for i in newCSV:
            for j in i[6]:
                print(j)

    else:
        print("Invalid file type")


x = "employeelist.csv"
sort(x)
