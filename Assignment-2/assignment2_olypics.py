# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
# df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

# question-0
# df.index[0]

# question-1
# df[Gold].argmax();

#question-2
#df['diff'] = df['Gold'] - df['Gold.1'];
#df['diff'].argmax() 

# qustion-3
# df_nonZero = df[(df['Gold'] > 0) & (df['Gold.1'] > 0)]
# df_diff = df_nonZero['Gold'] - df_nonZero['Gold.1'];
# df_relative = df_diff / df_nonZero['Gold.2']
# print(df_relative.argmax())

#question-4
# Points_of_length_146 = pd.Series(3*df['Gold.2']+2*df['Silver.2']+1*df['Bronze.2'])
# print(len(Points_of_length_146))

