import pandas as pd

df = pd.read_csv('positions.txt', sep='\t')
entryName = "P12530"
position = (df[df['Entry'].str.contains(entryName)]['Mutagenesis'])
#print(position)

df2 = pd.read_csv('input_files/test.txt', sep='\t')
df2['Mutagenesis']='abc'
for index, row in df2.iterrows():
    print(row['Mutagenesis'])
    df2.at[index, 'Mutagenesis']="changed"
    print(row['Mutagenesis'])



