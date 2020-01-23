class DNA():
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
    
    def GetAmino(self):
        tSlate = {"UUU":"Phe" , "UUC":"Phe",
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
        
        self.amino = [self.rna[i:i+3] for i in range(0, len(self.rna),3)]

        for i in self.amino:
            self.chunks += tSlate[i]
        





dna = "TACGTACCAGTATAGACCATAGATAGATAGGGATAGTAAATTTACATGCGAGCTAGATATATAGGTAGTGATAGATTAGGGCTAATCTACATATGCGCCGAGCGCTAGCGATAGAGAGTAGTAGCGATGTAGATTTACATAGCGGGCCGTCTCACATACGCATATTACGACGATTGGATTTACCGCGATACGGTCAGAGTAGGCGCAGGAATCTACTTATATTTATAGCGCCACGGATGTGGTAGACAGATAACT"

test = DNA(dna)
test.GetRNA()
test.GetAmino()
print(test.amino)
print(" ")
print(test.chunks)