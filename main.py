import tkinter as tk
from tkinter import filedialog
import pandas as pd
import ttkbootstrap as tb
from tkinter import filedialog, ttk

data1 = None  # Global variable to store loaded data for the first tab
data2 = None  # Global variable to store loaded data for the second tab
data3 = None  # Global variable to store loaded data for the third tab
data4 = None  # Global variable to store loaded data for the fourth tab
data5 = None  # Global variable to store loaded data for the fifth tab
data6 = None  # Global variable to store loaded data for the sixth tab
data7 = None  # Global variable to store loaded data for the seventh tab

# changes
def load_csv(tab_num):
    """Load a CSV file and display its contents."""
    global data1, data2, data3, data4, data5, data6, data7
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            if tab_num == 1:
                data1 = pd.read_csv(file_path, encoding='utf-8')
            elif tab_num == 2:
                data2 = pd.read_csv(file_path, encoding='utf-8')
            elif tab_num == 3:
                data3 = pd.read_csv(file_path, encoding='utf-8')
            elif tab_num == 4:
                data4 = pd.read_csv(file_path, encoding='utf-8')
            elif tab_num == 5:
                data5 = pd.read_csv(file_path, encoding='utf-8')
            elif tab_num == 6:
                data6 = pd.read_csv(file_path, encoding='utf-8')
            elif tab_num == 7:
                data7 = pd.read_csv(file_path, encoding='utf-8')
        except UnicodeDecodeError:
            # Try reading with a different encoding (e.g., 'latin-1')
            if tab_num == 1:
                data1 = pd.read_csv(file_path, encoding='latin-1')
            elif tab_num == 2:
                data2 = pd.read_csv(file_path, encoding='latin-1')
            elif tab_num == 3:
                data3 = pd.read_csv(file_path, encoding='latin-1')
            elif tab_num == 4:
                data4 = pd.read_csv(file_path, encoding='latin-1')
            elif tab_num == 5:
                data5 = pd.read_csv(file_path, encoding='latin-1')
            elif tab_num == 6:
                data6 = pd.read_csv(file_path, encoding='latin-1')
            elif tab_num == 7:
                data7 = pd.read_csv(file_path, encoding='latin-1')




def calculate_sum():
    """Calculate the sum of NUM_ENROLLED column for the filtered data."""
    global data1
    if data1 is not None:
        filter_condition1 = filter_entry1.get()
        filter_condition2 = filter_entry2.get()
        filtered_data = data1[(data1['TERM_DESC'].astype(str) == filter_condition1) & (data1['COLLEGE_NAME'].astype(str) == filter_condition2)]
        sum_column = filtered_data['NUM_ENROLLED'].sum()
        result_label1.config(text=f"Sum of 'NUM_ENROLLED' column for filtered data: {sum_column}")
    else:
        result_label1.config(text="Please load a CSV file first.")


def calculate_length():
    """Calculate the length of specified columns for the filtered data."""
    global data2
    if data2 is not None:
        term_desc = "TERM_DESC"
        college = "COLLEGE"
        major1 = "MAJOR1"
        filter_condition1 = filter_entry3.get()
        filter_condition2 = filter_entry4.get()

        filtered_data = data2[(data2[term_desc].astype(str) == filter_condition1) & (data2[college].astype(str) == filter_condition2)]
        
        
        major1_length = len(filtered_data[major1])

        result_label2.config(text=f"Length of MAJOR1: {major1_length}")
    else:
        result_label2.config(text="Please load a CSV file first.")


def calculate_percentage():
    """Calculate the percentage of the length of column 3 with the filter condition applied."""
    global data3
    if data3 is not None:
        filter_condition1 = filter_entry5.get()
        filter_condition2 = filter_entry6.get()
        filter_condition3 = filter_entry7.get()

        # Filter the data with the first two conditions
        filtered_data_first_two = data3[(data3["TERM_DESC"].astype(str) == filter_condition1) &
                                       (data3["COLLEGE"].astype(str) == filter_condition2)]
        
        # Filter the data with all three conditions
        filtered_data_all = filtered_data_first_two[(filtered_data_first_two["GENDER"].astype(str) == filter_condition3)]

        # Calculate lengths
        column3_length_after_first_two_filters = len(filtered_data_first_two["GENDER"])
        column3_length_after_all_filters = len(filtered_data_all["GENDER"])

        # Calculate percentage
        percentage = (column3_length_after_all_filters / column3_length_after_first_two_filters) * 100 if column3_length_after_first_two_filters != 0 else 0

        result_label3.config(text=f"Percentage of column 'GENDER' with filter condition: {percentage:.2f}%")
    else:
        result_label3.config(text="Please load a CSV file first.")


def calculate_length_DegreeType():
    """Calculate the length of the DEGREE_TYPE column after filtering."""
    global data4
    if data4 is not None:
        filter_condition1 = filter_entry8.get()
        filter_condition2 = filter_entry9.get()
        filter_condition3 = filter_entry10.get()

        # Filter the data
        filtered_data = data4[(data4["TERM_DESC"] == filter_condition1) &
                             (data4["COLLEGE"] == filter_condition2) &
                             (data4["DEGREE_TYPE"] == filter_condition3)]

        # Calculate the length of DEGREE_TYPE column
        degree_type_length = len(filtered_data["DEGREE_TYPE"])

        result_label4.config(text=f"Length of DEGREE_TYPE column after filtering: {degree_type_length}")
    else:
        result_label4.config(text="Please load a CSV file first.")


def calculate_length_ClassStanding():
    """Calculate the length of the CLASS_STANDING column after filtering."""
    global data5
    if data5 is not None:
        filter_condition1 = filter_entry11.get()
        filter_condition2 = filter_entry12.get()
        filter_condition3 = filter_entry13.get()

        # Filter the data
        filtered_data = data5[(data5["TERM_DESC"] == filter_condition1) &
                             (data5["COLLEGE"] == filter_condition2) &
                             (data5["CLASS_STANDING"] == filter_condition3)]

        # Calculate the length of DEGREE_TYPE column
        degree_type_length = len(filtered_data["CLASS_STANDING"])

        result_label5.config(text=f"Length of CLASS_STANDING column after filtering: {degree_type_length}")
    else:
        result_label5.config(text="Please load a CSV file first.")


def calculate_length_Ethnicity():
    """Calculate the length of the ETHNICITY column after filtering."""
    global data6
    if data6 is not None:
        filter_condition1 = filter_entry14.get()
        filter_condition2 = filter_entry15.get()
        filter_condition3 = filter_entry16.get()

        # Filter the data
        filtered_data = data6[(data6["TERM_DESC"] == filter_condition1) &
                             (data6["COLLEGE"] == filter_condition2) &
                             (data6["ETHNICITY"] == filter_condition3)]

        # Calculate the length of ETHNICITY column
        ethnicity_length = len(filtered_data["ETHNICITY"])

        result_label6.config(text=f"Length of ETHNICITY column after filtering: {ethnicity_length}")
    else:
        result_label6.config(text="Please load a CSV file first.")


def calculate_length_InternationalStudents():
    """Calculate the length of the HOME_COUNTRY column after filtering and return unique values."""
    global data7
    if data7 is not None:
        filter_condition1 = filter_entry17.get()
        filter_condition2 = filter_entry18.get()
        filter_condition3 = filter_entry19.get()

        # Filter the data
        filtered_data = data7[(data7["TERM_DESC"] == filter_condition1) &
                             (data7["COLLEGE"] == filter_condition2) &
                             (data7["HOME_COUNTRY"] != filter_condition3)]  # Use != for not equal

        # Calculate the length of HOME_COUNTRY column
        home_country_length = len(filtered_data["HOME_COUNTRY"])

        # Get unique values in the filtered HOME_COUNTRY column
        unique_values = filtered_data["HOME_COUNTRY"].unique().tolist()

        # Update result label
        result_label7.config(text=f"Length of HOME_COUNTRY column after filtering: {home_country_length}\nUnique values: {unique_values}")
    else:
        result_label7.config(text="Please load a CSV file first.")



root = tb.Window(themename="superhero")
root.title("Audits")
root.geometry('500x500')

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# First Tab
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Seats Filled')

header_frame1 = tk.Frame(tab1, bg="#990000", height=150)
header_frame1.pack(fill=tk.X, side=tk.TOP)

upload_button1 = tk.Button(header_frame1, text="Upload CSV", command=lambda: load_csv(1), bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
upload_button1.pack(pady=5)

filter_label1 = tk.Label(header_frame1, text="Enter Filter Condition for TERM_DESC:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label1.pack(pady=5)

filter_entry1 = tk.Entry(header_frame1, font=("Helvetica", 12))
filter_entry1.pack(pady=5)

filter_label2 = tk.Label(header_frame1, text="Enter Filter Condition for COLLEGE_NAME:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label2.pack(pady=5)

filter_entry2 = tk.Entry(header_frame1, font=("Helvetica", 12))
filter_entry2.pack(pady=5)

sum_button = tk.Button(header_frame1, text="Calculate Sum", command=calculate_sum, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
sum_button.pack(pady=5)

result_label1 = tk.Label(tab1, text="", font=("Helvetica", 12))
result_label1.pack(pady=10)

# Second Tab
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Total Majors')

header_frame2 = tk.Frame(tab2, bg="#990000", height=150)
header_frame2.pack(fill=tk.X, side=tk.TOP)

upload_button2 = tk.Button(header_frame2, text="Upload CSV", command=lambda: load_csv(2), bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
upload_button2.pack(pady=5)

filter_label3 = tk.Label(header_frame2, text="Enter Filter Condition for TERM_DESC:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label3.pack(pady=5)

filter_entry3 = tk.Entry(header_frame2, font=("Helvetica", 12))
filter_entry3.pack(pady=5)

filter_label4 = tk.Label(header_frame2, text="Enter Filter Condition for COLLEGE:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label4.pack(pady=5)

filter_entry4 = tk.Entry(header_frame2, font=("Helvetica", 12))
filter_entry4.pack(pady=5)

length_button = tk.Button(header_frame2, text="Calculate Length", command=calculate_length, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
length_button.pack(pady=5)

result_label2 = tk.Label(tab2, text="", font=("Helvetica", 12))
result_label2.pack(pady=10)

# Third Tab
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text='Percent Male/Female')

header_frame3 = tk.Frame(tab3, bg="#990000", height=150)
header_frame3.pack(fill=tk.X, side=tk.TOP)

upload_button3 = tk.Button(header_frame3, text="Upload CSV", command=lambda: load_csv(3), bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
upload_button3.pack(pady=5)

filter_label5 = tk.Label(header_frame3, text="Enter Filter Condition for TERM_DESC:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label5.pack(pady=5)

filter_entry5 = tk.Entry(header_frame3, font=("Helvetica", 12))
filter_entry5.pack(pady=5)

filter_label6 = tk.Label(header_frame3, text="Enter Filter Condition for COLLEGE:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label6.pack(pady=5)

filter_entry6 = tk.Entry(header_frame3, font=("Helvetica", 12))
filter_entry6.pack(pady=5)

filter_label7 = tk.Label(header_frame3, text="GENDER:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label7.pack(pady=5)

filter_entry7 = tk.Entry(header_frame3, font=("Helvetica", 12))
filter_entry7.pack(pady=5)

percentage_button = tk.Button(header_frame3, text="Calculate Percentage", command=calculate_percentage, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
percentage_button.pack(pady=5)

result_label3 = tk.Label(tab3, text="", font=("Helvetica", 12))
result_label3.pack(pady=10)

# Fourth Tab
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text='Degree Type')

header_frame4 = tk.Frame(tab4, bg="#990000", height=150)
header_frame4.pack(fill=tk.X, side=tk.TOP)

upload_button4 = tk.Button(header_frame4, text="Upload CSV", command=lambda: load_csv(4), bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
upload_button4.pack(pady=5)

filter_label8 = tk.Label(header_frame4, text="TERM_DESC:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label8.pack(pady=5)

filter_entry8 = tk.Entry(header_frame4, font=("Helvetica", 12))
filter_entry8.pack(pady=5)

filter_label9 = tk.Label(header_frame4, text="COLLEGE:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label9.pack(pady=5)

filter_entry9 = tk.Entry(header_frame4, font=("Helvetica", 12))
filter_entry9.pack(pady=5)

filter_label10 = tk.Label(header_frame4, text="DEGREE_TYPE:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label10.pack(pady=5)

filter_entry10 = tk.Entry(header_frame4, font=("Helvetica", 12))
filter_entry10.pack(pady=5)

number_button4 = tk.Button(header_frame4, text="Calculate Length", command=calculate_length_DegreeType, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
number_button4.pack(pady=5)

result_label4 = tk.Label(tab4, text="", font=("Helvetica", 12))
result_label4.pack(pady=10)

# Fifth Tab
tab5 = ttk.Frame(notebook)
notebook.add(tab5, text='Class Standing')

header_frame5 = tk.Frame(tab5, bg="#990000", height=150)
header_frame5.pack(fill=tk.X, side=tk.TOP)

upload_button5 = tk.Button(header_frame5, text="Upload CSV", command=lambda: load_csv(5), bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
upload_button5.pack(pady=5)

filter_label11 = tk.Label(header_frame5, text="TERM_DESC:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label11.pack(pady=5)

filter_entry11 = tk.Entry(header_frame5, font=("Helvetica", 12))
filter_entry11.pack(pady=5)

filter_label12 = tk.Label(header_frame5, text="COLLEGE:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label12.pack(pady=5)

filter_entry12 = tk.Entry(header_frame5, font=("Helvetica", 12))
filter_entry12.pack(pady=5)

filter_label13 = tk.Label(header_frame5, text="CLASS_STANDING:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label13.pack(pady=5)

filter_entry13 = tk.Entry(header_frame5, font=("Helvetica", 12))
filter_entry13.pack(pady=5)

number_button5 = tk.Button(header_frame5, text="Calculate Length", command=calculate_length_ClassStanding, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
number_button5.pack(pady=5)

result_label5 = tk.Label(tab5, text="", font=("Helvetica", 12))
result_label5.pack(pady=10)

# Sixth Tab
tab6 = ttk.Frame(notebook)
notebook.add(tab6, text='Race/Ethnicity')

header_frame6 = tk.Frame(tab6, bg="#990000", height=150)
header_frame6.pack(fill=tk.X, side=tk.TOP)

upload_button6 = tk.Button(header_frame6, text="Upload CSV", command=lambda: load_csv(6), bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
upload_button6.pack(pady=5)

filter_label14 = tk.Label(header_frame6, text="TERM_DESC:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label14.pack(pady=5)

filter_entry14 = tk.Entry(header_frame6, font=("Helvetica", 12))
filter_entry14.pack(pady=5)

filter_label15 = tk.Label(header_frame6, text="COLLEGE:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label15.pack(pady=5)

filter_entry15 = tk.Entry(header_frame6, font=("Helvetica", 12))
filter_entry15.pack(pady=5)

filter_label16 = tk.Label(header_frame6, text="ETHNICITY:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label16.pack(pady=5)

filter_entry16 = tk.Entry(header_frame6, font=("Helvetica", 12))
filter_entry16.pack(pady=5)

number_button6 = tk.Button(header_frame6, text="Calculate Length", command=calculate_length_Ethnicity, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
number_button6.pack(pady=5)

result_label6 = tk.Label(tab6, text="", font=("Helvetica", 12))
result_label6.pack(pady=10)


# Seventh Tab
tab7 = ttk.Frame(notebook)
notebook.add(tab7, text='Internation Students')

header_frame7 = tk.Frame(tab7, bg="#990000", height=150)
header_frame7.pack(fill=tk.X, side=tk.TOP)

user_label = tk.Label(header_frame7, fg="white", bg="#990000", font=("Helvetica", 12))
user_label.pack(side=tk.LEFT, padx=10)

upload_button7 = tk.Button(header_frame7, text="Upload CSV", command=lambda: load_csv(7), bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
upload_button7.pack(pady=5)

filter_label17 = tk.Label(header_frame7, text="TERM_DESC:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label17.pack(pady=5)

filter_entry17 = tk.Entry(header_frame7, font=("Helvetica", 12))
filter_entry17.pack(pady=5)

filter_label27 = tk.Label(header_frame7, text="COLLEGE:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label27.pack(pady=5)

filter_entry18 = tk.Entry(header_frame7, font=("Helvetica", 12))
filter_entry18.pack(pady=5)

filter_label37 = tk.Label(header_frame7, text="HOME_COUNTRY:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label37.pack(pady=5)

filter_entry19 = tk.Entry(header_frame7, font=("Helvetica", 12))
filter_entry19.pack(pady=5)

number_button7 = tk.Button(header_frame7, text="Calculate Length", command=calculate_length_InternationalStudents, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
number_button7.pack(pady=5)

result_label7 = tk.Label(root, text="", font=("Helvetica", 12))
result_label7.pack(pady=10)



root.mainloop()
