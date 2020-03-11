#defining module
def fasta():
#defining variable filename
    filename = 'short.fasta'
    filename_split = filename.split('.')
#checking filename to ensure it is the correct type
    assert(len(filename_split) == 2)
    assert(filename_split[1] == 'fasta')
#defining counters
    counter_A = 0
    counter_C = 0
    counter_G = 0
    counter_T = 0

#openning file and then counting letters and printing the results
    with open('/Users/cameronkilduff/Desktop/03_Assignment/short.fasta', 'r') as input_file:
        input_file.readline()
        for line in input_file:
            my_list = line.strip()
            for i in my_list:
                if i == 'A':
                    counter_A += 1
                elif i == 'C':
                    counter_C += 1
                elif i == 'G':
                    counter_G += 1
                elif i == 'T':
                    counter_T += 1
                else:
                    print('Character |',Character,'|')
                    raise NameError()
print('As:', counter_A)
print('Cs:', counter_C)
print('Gs:', counter_G)
print('Ts:', counter_T)
