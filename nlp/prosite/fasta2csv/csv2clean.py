#Read CSV
import csv
import re

def parseProtein(data):
    i = [pos for pos, char in enumerate(data) if char == '/']
    j = data.find("|")
    end = len(data) if len(i) <= 2 else i[2]
    score = "(0)" if len(i) <=2 else data[i[2]+1:]

    return {
        "location":data[i[0] + 1:i[1]],
        "name": data[0:i[0]],
        "motif":data[j+1:end],
        "score":score
    }
paths = ['./test-cc', './test-mf']
for path in paths:
    out_lines = []
    text = ""
    with open(f'{path}_input.csv') as f:
        reader = csv.reader(f, delimiter='\t')
        curMotifs = ""
        curName = ""
        for row in reader:
            parsed = parseProtein(row[0])
            if parsed["name"] == curName:
                curMotifs += f"\t{parsed['motif']};{parsed['location']};{parsed['score']}"
            else: #Add last row. First row will be blank
                out_lines.append(f"{curName}{curMotifs}") 
                curMotifs =  f"\t{parsed['motif']};{parsed['location']};{parsed['score']}"
                curName = parsed["name"]
    out_lines.pop(0)
    with open(f'{path}_output.csv', 'w') as fout:
        fout.write('\n'.join(out_lines))
            
        

#Write to text file
#output_file = "data/animes_wstartend.txt"
#with open(output_file, "w") as f:
#    f.write(text)
