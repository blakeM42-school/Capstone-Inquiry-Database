import pandas as pd
import matplotlib.pyplot as plt

# Read data from a CSV file
csv_file_path = 'C:\\Users\\blakemangola\\Downloads\\SUU-Students-2024-01-25-T-06-30-15.csv'
df = pd.read_csv(csv_file_path)

# Assuming the CSV file has a column named 'CLASS_STANDING' and another named 'CURRENT_SEMESTER_CREDITS'
# Adjust these column names based on your actual CSV file structure
categories = df['CLASS_STANDING']
values = df['CURRENT_SEMESTER_CREDITS']

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='skyblue')
plt.xlabel('Class Standing')
plt.ylabel('Current Semester Credits')
plt.title('Bar Chart from CSV Data')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()


