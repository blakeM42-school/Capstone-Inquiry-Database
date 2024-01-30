import pandas as pd

file_path = r"C:\Users\blakemangola\Downloads\SUU-Students-2024-01-25-T-06-30-15.csv"
students = pd.read_csv(file_path, encoding='latin1')


#print(students.head(10))
#x = students.head(10)

#print(students.columns)

#print(x[['LAST_NAME', 'USERNAME']])

#print(students.iloc[1:4])

#print(students.iloc[2,1])

#for index, row in students.iterrows():
    #print(index, row['LAST_NAME'])

print(students.loc[students['USERNAME'] == "chamberscameron"])

#print(students.describe())

#print(students.sort_values(['USERNAME', 'AGE'], ascending=[1,0]))

#print(students.loc[students['AGE'] >= 30.0])