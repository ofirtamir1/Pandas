import pandas as pd

df3 = pd.read_excel("people.xlsx")
df2 =df3.loc[(df3['gender'] == 'M')]
df4 =df2.groupby('gender')
print(df4['gender'])

print('WHASAPPPPPPPPPP')

print('facebook')