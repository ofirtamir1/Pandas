import pandas as pd

#ex1
df = pd.read_excel("people.xlsx")
#ex2
df2=['age'].mean())
#ex3
(df3['name'].count())
#ex4
(df4['age'].sum())
#ex5
df2 =df3.loc[(df3['gender'] == 'M')]
df5 =df2.groupby('gender')
#df6
df6 =df.loc[(df['age'] >20)]
#df7
df7 =df.loc[(df['age'] > 35) | (df['age'] <17)]
print(df7[['age']])


