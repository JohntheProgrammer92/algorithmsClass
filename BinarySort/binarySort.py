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
			with open(csv) as data:#sorts data at init using a selection sort
				if self.testData(data):
					array = [num for num in data]
					for i in range(len(array)):
						min_idx = i 
						for j in range(i+1, len(array)):
							if array[min_idx] > array[j]: 
								min_idx = j 
						array[i], array[min_idx] = array[min_idx], array[i]
				
					with open("sorted.csv","w")as sorted:
						numRanks = {}
						totalRankPay = {}
						for i in array:
							i=i.split(',')
							if i[6] in numRanks:
								numRanks[i[6]] += 1
							else: 
								numRanks[i[6]] = 1
							if i[6] in totalRankPay:
								totalRankPay[i[6]] += int(i[7])
							else:
								totalRankPay[i[6]] = int(i[7])
						for j in array:
							j =j.split(',')
							print(j)	
						for i in array:
							i + (str(totalRankPay[j[6]] / numRanks[j[6]]))
							sorted.write(str(i))
				else:
					self.errs.append("Invalid data set")
		else:
			self.errs.append("Not a CSV file.")

	def testData(self,data):
		for i in data:
			arr = i.split(",")
			if len(arr) == 8:
				return True
			else:
				return False
		

	def averageSalaryPerRank(self, array):
		#finds the average salary per rank
		numRanks = {}
		totalRankPay = {}
		for i in array:
			i=i.split(',')
			if i[6] in numRanks:
				numRanks[i[6]] += 1
			else: 
				numRanks[i[6]] = 1
			if i[6] in totalRankPay:
				totalRankPay[i[6]] += int(i[7])
			else:
				totalRankPay[i[6]] = int(i[7])
		for j in array:
			j =j.split(',')
			j.append(str(totalRankPay[j[6]] / numRanks[j[6]]))
			print(j)	

		return array
		


			
		

	
	def phoneSSNFix(self, f):
		#takes the phone numbers after the file is sorted and fixes them.
		file = [record for record in f]
		number = ""
		social = ""
		
		for digit in file[3]:
			if digit.isdigit():
				number += str(digit)
		file[3] = number
		for j in file[4]:
			if j.isdigit():
				social += str(j)
		file[4] = social
		return f

	#def select(self,id):
		#search using binarysearch.



if __name__=='__main__':
	csv = input("Type the name of the file to search: ")
	table = DataSet(csv)
	if len(table.errs) > 0:
		print(table.errs) 
	#Test error handling 
	#print(*[i for i in table.errs] if len(table.errs) > 0 else "success")