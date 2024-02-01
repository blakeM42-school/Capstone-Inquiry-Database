import pandas as pd

file_path = r"C:\Users\blakemangola\OneDrive - Southern Utah University\Desktop\capstone\SUU-Students-2024-01-25-T-06-30-15 (1).csv"
students = pd.read_csv(file_path, encoding='latin1')
result = students.loc[students['DEPARTMENT'] == "Computer Science/Cybersecurity"]
result1 = students.loc[students['DEPARTMENT'] == "Aviation Sciences"]
result2 = students.loc[students['DEPARTMENT'] == "Engineering and Technology"]
result3 = students.loc[students['DEPARTMENT'] == "Mathematics"]
result1a = students.loc[students['COLLEGE'] == "Engineering/Computational Sci"]

result.to_csv(r"C:\Users\blakemangola\OneDrive - Southern Utah University\Desktop\capstone\computerscienceandcybersecurity_depart.csv")
result1.to_csv(r"C:\Users\blakemangola\OneDrive - Southern Utah University\Desktop\capstone\aviationsciences_depart.csv")
result2.to_csv(r"C:\Users\blakemangola\OneDrive - Southern Utah University\Desktop\capstone\engineeringandtechnology_depart.csv")
result3.to_csv(r"C:\Users\blakemangola\OneDrive - Southern Utah University\Desktop\capstone\mathematics_depart.csv")
result1a.to_csv(r"C:\Users\blakemangola\OneDrive - Southern Utah University\Desktop\capstone\EngineeringandComputationalSci_college.csv")

row_count = result.shape[0]
row_count1 = result1.shape[0]
row_count2 = result2.shape[0]
row_count3 = result3.shape[0]
row_count4 = result1a.shape[0]
print(row_count)
print(row_count1)
print(row_count2)
print(row_count3)
print(row_count4)
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
