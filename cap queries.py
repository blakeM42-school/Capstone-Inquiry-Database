import pandas as pd

file_path = r"C:\Users\hdmia\Desktop\capstone\SUU-Students-2024-01-25-T-06-30-15.csv"
students = pd.read_csv(file_path, encoding='latin1')
result = students.loc[students['DEPARTMENT'] == "Computer Science/Cybersecurity"]
result1 = students.loc[students['DEPARTMENT'] == "Aviation Sciences"]
result2 = students.loc[students['DEPARTMENT'] == "Engineering and Technology"]

result.to_csv(r"C:\Users\hdmia\Desktop\capstone\computerscienceandcybersecurity.csv")
result1.to_csv(r"C:\Users\hdmia\Desktop\capstone\aviationsciences.csv")
result2.to_csv(r"C:\Users\hdmia\Desktop\capstone\engineeringandtechnology.csv")

row_count = result.shape[0]
row_count1 = result1.shape[0]
row_count2 = result2.shape[0]
print(row_count)
print(row_count1)
print(row_count2)
#print(students.head(10))
#x = students.head(10)

#print(students.columns)

#print(x[['LAST_NAME', 'USERNAME']])

#print(students.iloc[1:4])

#print(students.iloc[2,1])

#for index, row in students.iterrows():
    #print(index, row['LAST_NAME'])



#print(students.describe())

#print(students.sort_values(['USERNAME', 'AGE'], ascending=[1,0]))

#print(students.loc[students['AGE'] >= 30.0])
