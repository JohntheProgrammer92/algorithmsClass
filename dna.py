class Data():
    def __init__(self, dna):
        self.dna = dna
        self.rna = ""
        self.amino = []
        self.chunks = ""

    def GetRNA(self):
        tScribe ={"A":"U","T":"A","G":"C","C":"G"}
        for i in self.dna:
            self.rna += tScribe[i]
        return self.rna
    
    def GetNTides(self):
        translate = {"UUU":"Phe" , "UUC":"Phe",
          "UUA":"Leu" , "UUG":"Leu" , "CUU":"Leu" , "CUC":"Leu" , "CUA":"Leu" , "CUG":"Leu",
          "AUU":"Ile" , "AUC":"Ile" , "AUA":"Ile" ,
          "AUG":"Met",
          "GUU":"Val" , "GUC":"Val" , "GUA":"Val" , "GUG":"Val" ,
          "UCU":"Ser" , "UCC":"Ser" , "UCA":"Ser" , "UCG":"Ser" , "AGU":"Ser" , "AGC":"Ser" ,
          "CCU":"Pro" , "CCC":"Pro" , "CCA":"Pro" , "CCG":"Pro" , 
          "ACU":"Thr" , "ACC":"Thr" , "ACA":"Thr" , "ACG":"Thr" ,
          "GCU":"Ala" , "GCA":"Ala" , "GCC":"Ala" , "GCG" : "Ala",
          "UAU":"Tyr" , "UAC":"Tyr" ,
          "UAA":"STOP" , "UAG":"STOP" , "UGA":"STOP",
          "CAU":"His" , "CAC":"His" ,
          "CAA":"Gln" , "CAG":"Gln" ,
          "AAU":"Asn" , "AAC":"Asn" ,
          "AAA":"Lys" , "AAG":"Lys" ,
          "GAU":"Asp" , "GAC":"Asp" ,
          "GAA":"Glu" , "GAG":"Glu" ,
          "UGU":"Cys" , "UGC":"Cys" ,
          "UGG":"Trp" ,
          "CGU":"Arg" , "CGC":"Arg" , "CGA":"Arg" , "CGG":"Arg" , "AGA":"Arg" , "AGG":"Arg" , 
          "GGU":"Gly" , "GGC":"Gly" , "GGA":"Gly" , "GGG":"Gly"}

        countDict = {}
        protein = ""
        total = 0
        self.amino = [self.rna[i:i+3] for i in range(0, len(self.rna),3)]
        
        with open("results.txt", 'a') as f:
            total = 0
            for j in self.amino:
               
                if translate[j] != "STOP":
                    for k in j:
                        if k in countDict:
                            countDict[k] += 1
                            total += 1
                        else:
                            countDict[k] = 1
                            total += 1

                    protein += translate[j]
                    protein +="-"
                else:
                    for k in j:
                        if k in countDict:
                            countDict[k] += 1
                            total += 1
                        else:
                            countDict[k] = 1
                            total += 1
                    protein += translate[j]
                    f.write(protein +"\n")
                    
                    perA = 100/total*countDict["A"]
                    perC = 100/total*countDict["C"]
                    perG = 100/total*countDict["G"]
                    perU = 100/total*countDict["U"]
                    f.write(str("%.2f" % perA) +"%\n")
                    f.write(str("%.2f" % perC) +"%\n")
                    f.write(str("%.2f" % perG) +"%\n")
                    f.write(str("%.2f" % perU) +"%\n\n")
                    countDict = {}
                    protein = ""
                    total = 0
                    f.write("---Protein Frequencies---\n")







                





dna = "TACGTACCAGTATAGACCATAGATAGATAGGGATAGTAAATTTACATGCGAGCTAGATATATAGGTAGTGATAGATTAGGGCTAATCTACATATGCGCCGAGCGCTAGCGATAGAGAGTAGTAGCGATGTAGATTTACATAGCGGGCCGTCTCACATACGCATATTACGACGATTGGATTTACCGCGATACGGTCAGAGTAGGCGCAGGAATCTACTTATATTTATAGCGCCACGGATGTGGTAGACAGATAACT"

test = Data(dna)
test.GetRNA()
test.GetNTides()
test.GetFreq()
