import pandas as pd
#ex1
df=pd.read_excel('people.xlsx')
df_animals=pd.read_excel('animals.xlsx')
df1 = df.rename(columns={'name' : 'person_name' , 'age' :'person_age'})
#ex2
df2 = df_animals.rename(columns={'ID': 'animalID' , 'Name': 'Animals_name' , 'Age': 'Animalage'})
#ex3
df3 = df.merge (df2 , left_on= 'name' , right_on = 'Animals_name')
#print(df3)
#ex4
df4= df.merge (df_animals , left_on= 'name' , right_on = 'Name', how= 'left')
#print(df4)
#ex5
df5= df3['name'].unique()
#print(df5)
#ex6
df6= df3.loc[df3['name']=='Ido']
df6=df6['Owner_ID']
#print(df6)
#ex7
df7= df3.loc[df3['age']>20]
df7=df7['name']
#print(df7)
#ex8
df8=df3.loc[df['age']>=30]
df8=df8['Animalage']
#print (df8)
#ex9
df9= df3.loc[(df3['gender']== 'F')&((df3['Type']=='dog')|(df3['Type']=='cat'))]
#print(df9['name'])
#ex10
df10= df4.loc[(df4['gender']== 'M')&~(df4['Type'].notnull())]
#print(df10['name'])
#ex11
df11=df3.loc[(df3['gender']== 'F')&((df3['Color']=='white'))]
#print(df11['birth_date'])
#ex12
df12 = df3.loc[(df3['age']>20)&(df3['Type']=='dog')]
df12 = df12['Color'].unique()
#print(df12)
#ex13
df13=df4.loc[~(df4['Type'].notnull())]
df13=df13['name'].unique()
print(df13)
