paths = ['./test-cc', './test-mf']
for path in paths:
    out_lines = []
    row =  ''
    with open(f'{path}.eml', 'r') as f:
        for line in f:
            if line.startswith('>'):
                out_lines.append(row)
                row = line[1:].strip() + '\t'
            else:
                row += line.strip()
        out_lines.pop(0)
    with open(f'{path}_input.csv', 'w') as fout:
        fout.write('\n'.join(out_lines))
