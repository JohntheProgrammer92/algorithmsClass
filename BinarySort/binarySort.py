""" 
John Boner
Algorithms
02/26/2020
"""
#this class will take a data set (csv), and give it methods to use as tools
#Such as a select method, an average salary tool, and a number sanitizer.

class DataSet():
	def __init__(self, csv):
		self.errs = []
		if csv.split('.')[-1] == "csv":
			with open(csv) as self.data:#sorts data at init using a selection sort
				for i in range(len(self.data)): 
					min_idx = i 
					for j in range(i+1, len(self.data)): 
						if self.data[min_idx][0] > self.data[j][0]: 
							min_idx = j 
					self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
				with open("sorted"+csv,"a")as sorted:
					for i in self.data:
						sorted.write(i)
		else:
			self.errs.append("Not a CSV file.")

#testData(self.data):
	#test the content of the csv to determine if its correct.

#averageSalaryPerRank():
	#finds the average salary per rank

# def phoneSSNFix(self.data):
	#takes the phone numbers after the file is sorted and fixes them.

#def select(self,id):
	#search using binarysearch.

if __name__=='__main__':
	csv = input("Type the name of the file to search: ")
	table = DataSet(csv)
	#Test error handling 
	print(*[i for i in table.errs] if len(table.errs) > 0 else "success")