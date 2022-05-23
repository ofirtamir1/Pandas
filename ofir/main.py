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
df4 =df2.groupby('gender')
#df6
df1 =df.loc[(df['age'] >20)]



