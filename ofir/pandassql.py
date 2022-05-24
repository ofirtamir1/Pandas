import pandas as pd
#ex1
df=pd.read_excel('people.xlsx')
df_animals=pd.read_excel('animals.xlsx')
df1 = df.rename(columns={'name' : 'person_name' , 'age' :'person_age'})
#ex2
df2 = df_animals.rename(columns={'ID': 'animalID' , 'Name': 'Animals_name' , 'Age': 'Animalage'})
#ex3
df3 = df.merge (df_animals , left_on= 'name' , right_on = 'Name')
#print(df3)
#ex4
df4= df.merge (df_animals , left_on= 'name' , right_on = 'Name', how= 'left')
#print(df4)
