import pandas as pd
data={
    'Name':['John','Emma','Sant','Lisa','Tom'],
    'Age':[25,30,28,32,27],
    'Country':['USA','Canada','India','UK','Australia'],
    'Salary':[50000,60000,70000,80000,65000]
}
df=pd.DataFrame(data)
print("Original Data Frame")
print(df)

name_age=df[['Name','Age']]
print("Original Data Frame")
print(df)

name_age=df[['Name','Age']]
print("Name and age Columns")
print(name_age)

filtered_df=df[df['Country']=='USA']
print("\nfiltered DAtaFrame(Country='USA')")
print(filtered_df)

sorted_df=df.sort_values('Salary',ascending=False)
print("\nSorted DataFrame(by salary in descending order)")
print(sorted_df)

average_salary=df['Salary'].mean()
print("\nAverage Sallary",average_salary)

df['Experience']=[3,6,4,8,5]
print("\nData farme with added experience")
print(df)

df.loc[df['Name']=='Emma','Salary']=65000
print("\nDataFrame with updating emmma's salary")
print(df)

df = df.drop('Experience', axis=1)
print("\nDataFrame after deleting the column")
print(df)
