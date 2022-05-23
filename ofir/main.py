import pandas as pd

# ex1
df = pd.read_excel("people.xlsx")
# ex2
df2 = df
# ex3
df3 = df
(df3['name'].count())
# ex4
df4 = df
(df4['age'].sum())
# ex5
df5 = df
df5 = df3.loc[(df3['gender'] == 'M')]
df5 = df2.groupby('gender')
# ex6
df6 = df
df6 = df.loc[(df['age'] > 20)]
# ex7
df7 = df
df7 = df.loc[(df['age'] > 35) | (df['age'] < 17)]
(df7[['age']])
# ex8
df8 = df.loc[(df['age'] == 9) | (df['age'] == 25) | (df['age'] == 16) |
(df['age'] == 36) | (df['age'] == 36) | (df['age'] == 49)]
#ex 8
df8 = df
df8 =df.loc[(df['gender'] == 'F') | (df['name'] == 'Tal')]
print(df8['name'].count())