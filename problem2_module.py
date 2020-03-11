from typing import Dict 

def printDigrams(pairsCount: Dict[str, int]):
    "Print the digrams"
    
    bases = ['A', 'G', 'C', 'T']
    
counter_AA = 0
counter_AG = 0
counter_AC = 0
counter_AT = 0
counter_GA = 0
counter_GG = 0
counter_GC = 0
counter_GT = 0
counter_CA = 0
counter_CG = 0
counter_CC = 0
counter_CT = 0
counter_TA = 0
counter_TG = 0
counter_TC = 0
counter_TT = 0
    
    
    with open('Users\xbbnx39\Desktop\Pythonclass\short.fasta.txt', 'r') as input_file:
        input_file.readline()
        for line in input_file:
            my_list = line.strip()
            for i in my_list:
                if i == 'AA':
                     counter_AA += 1
                elif i == 'C':
                    counter_C += 1
                elif i == 'G':
                    counter_G += 1
                elif i == 'T':
                    counter_T += 1
                else:
                    print('Character |',Character,'|')
                    raise NameError()   

    print(' ', end=' ')
    for ch in bases:
        print(ch.rjust(7), end=' ')
    print()
    
    for ch1 in bases:
        print(ch1, end=' ')
        
        for ch2 in bases:
            digram = ch1 + ch2
            if (digram in pairsCount):
                count = pairsCount[digram]
            else:
                    count=0
                
            print(repr(count).rjust(7), end=' ')
        print()


        

