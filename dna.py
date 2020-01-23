class DNA():
    def __init__(self, dna):
        self.dna = dna
        self.rna = ""

    def GetRNA(self):
        tScribe ={"A":"U","T":"A","G":"C","C":"G"}
        for i in self.dna:
            self.rna += tScribe[i]
        return self.rna
    
    def GetAmino(self):
        tSlate = {"Phe": ["UUU","UUC"],
                  "Leu": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
                  "Ile": ["AUU","AUC","AUA"],
                  "Met": ["AUG"],
                  "Val": ["GUU","GUC","GUA","GUG"],
                  "Ser": ["UCU","UCC","UCA","UCG","AGU","AGC"],
                  "Pro": ["CCU","CCC","CCA","CCG"],
                  "Thr": ["ACU","ACC","ACA","ACG"],
                  "Ala": ["GCU","GCA","GCC","GCG7"],
                  "Tyr": ["UUAU","UAC"],
                  "STOP": ["UAA", "UAG","UGA"],
                  "His": ["CAU","CAC"],
                  "Gln": ["CAA","CAG"],
                  "Asn": ["AAU","AAC"],
                  "Lys": ["AAA","AAG"],
                  "Asp": ["GAU","GAC"],
                  "Glu": ["GAA","GAG"],
                  "Cys": ["UGU","UGC"],
                  "Trp": ["UGG"],
                  "Arg": ["CGU","CGC","CGA","CGG","AGA","AGG"],
                  "Gly": ["GGU","GGC","GGA","GGG"]}
        
        amino = [self.rna[i:i+3] for i in range(0, len(self.rna),3)]
        print(amino)

        for j in amino:
            print(j)
            for key, value in tSlate.items():
                if j == value:
                    return key
                  




dna = "TACGTACCAGTATAGACCATAGATAGATAGGGATAGTAAATTTACATGCGAGCTAGATATATAGGTAGTGATAGATTAGGGCTAATCTACATATGCGCCGAGCGCTAGCGATAGAGAGTAGTAGCGATGTAGATTTACATAGCGGGCCGTCTCACATACGCATATTACGACGATTGGATTTACCGCGATACGGTCAGAGTAGGCGCAGGAATCTACTTATATTTATAGCGCCACGGATGTGGTAGACAGATAACT"

test = DNA(dna)
print(test.GetRNA())
print(" ")
print(test.GetAmino())