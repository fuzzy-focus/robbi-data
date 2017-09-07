import fnmatch
import os
import pandas as pd

matches = []
for root, dirnames, filenames in os.walk('.'):
    for filename in fnmatch.filter(filenames, '*.txt'):
        matches.append(os.path.join(root, filename))

df = pd.DataFrame()
for f in matches:
    data = pd.read_csv(f, sep='\t')
    data['file'] = f
    df = df.append(data, ignore_index=True)
group = df[['Area of Interest', 'Average fixation [ms]', 'Fixation count']].groupby(['Area of Interest']).sum()
print(group)
