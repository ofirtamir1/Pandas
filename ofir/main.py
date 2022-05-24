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
df7 = df.loc[(df['age'] > 35) | (df['age'] < 17)][['age']]

# ex8
df8 = df.loc[(df['age'] == 9) | (df['age'] == 25) | (df['age'] == 16) |
(df['age'] == 36) | (df['age'] == 36) | (df['age'] == 49)]
#ex 8
df8 = df
df8 =df.loc[(df['gender'] == 'F') | (df['name'] == 'Tal')]['name'].count()
#ex 9
df9 = df
df9 =df.loc[(df['gender'] == 'F')]
mean = df9['age'].mean()
#ex10
df10 = df
df9 =df.loc[(df['gender'] == 'M') & (df['name'] != 'Tal')] ['age'].sum()
#ex12
df12 =df
(df['name'].unique())
#ex13
df13 = df
(df['name'].value_counts())
#ex14
df14 =df.loc[(df['gender'] == 'M')]
(df['name'].value_counts())
#df15
df15 =df.loc[(df['gender'] == 'M')]
x = df15.groupby('gender')
#print (x.mean())
#ex16
df16= df
(df['name'] != 'Tal').value_counts()
def16groupby = df15.groupby('gender')
#ex17
df17=df
df17 =df.loc[(df['name'] == 'Ido') | (df['name'] == 'Shani')]
def17groupby = df17.groupby('name')
