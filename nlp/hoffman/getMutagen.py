import csv
#import sys
#fileName = str(sys.argv[0])
def getPositions(s):
    li = s.split()
    res = ';'.join([li[i+1] for i, x in enumerate(li) if x == "MUTAGEN"])
    return res
    
    
with open('uniprot-filtered-reviewed.tab', newline='') as data:
    data_reader = csv.reader(data, delimiter='\t')
    f = open("positions.txt", "a+")
    for data in data_reader:
        line = data[0] + "\t" + getPositions(data[-1]) + "\n"
        f.write(line )
        
