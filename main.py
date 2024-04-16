import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import numpy as np
from pandastable import Table
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import matplotlib.pyplot as plt
from scipy.stats import norm
from pandas.api.types import is_numeric_dtype
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

root = tb.Window(themename="superhero")
root.title("Southern Utah University - College Sort")
root.geometry('500x500')

data1 = None  # Global variable to store loaded data for the first tab
data2 = None  # Global variable to store loaded data for the second tab
data3 = None  # Global variable to store loaded data for the third tab
data4 = None  # Global variable to store loaded data for the fourth tab
data5 = None  # Global variable to store loaded data for the fifth tab
data6 = None  # Global variable to store loaded data for the sixth tab
data7 = None  # Global variable to store loaded data for the seventh tab

column_var1 = tk.StringVar()
column_var2 = tk.StringVar()
column_var3 = tk.StringVar()
operator_var = tk.StringVar()
operator_var2 = tk.StringVar()
operator_var3 = tk.StringVar()
column_var_audit = tk.StringVar()
column_varX = tk.StringVar(root)
column_varY = tk.StringVar(root)

data = None  # Global variable to store loaded data

def display_data(dataframe):
    """Display the given DataFrame in the table_frame."""
    for widget in table_frame.winfo_children():
        widget.destroy()
    table = Table(table_frame, dataframe=dataframe, showstatusbar=True)
    table.show()


def load_csv_for_audits(tab_num):
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

def load_csv():
    """Load a CSV file and display its contents."""
    global data, column_var1, column_var2, column_var3, column_var_audit, column_varX, column_varY  # Use the global variable to store loaded data
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            data = pd.read_csv(file_path, encoding='utf-8')
            # for widget in table_frame.winfo_children():
            #     widget.destroy()
            # table = Table(table_frame, dataframe=data, showstatusbar=True) # Removed 'showtoolbar' option from table, can add back later if need be/want to
            # table.show()

            display_data(data)
            
            columns = data.columns.tolist()
            column_name_combobox['values'] = columns
            column_name_combobox2['values'] = columns
            column_name_combobox3['values'] = columns
            column_name_combobox4['values'] = columns
            column_menu1['values'] = columns
            column_menu2['values'] = columns
            if columns:
                column_var1.set(data.columns.tolist()[0])  # Set the default value to the first column name
                column_var2.set(data.columns.tolist()[0])
                column_var3.set(data.columns.tolist()[0])
                column_var_audit.set(data.columns.tolist()[0])
                column_varX.set(data.columns.tolist()[0])
                column_varY.set(data.columns.tolist()[0])
        except UnicodeDecodeError:
            data = pd.read_csv(file_path, encoding='latin-1')

def filter_and_save():
    """Filter the loaded data and save it as a new CSV file."""
    global data   # Access the global variable containing loaded data
    if data is not None:
        selected_column = column_var1.get()
        filter_condition = filter_entry.get().strip()  # Get filter condition from entry widget
        additional_selected_column = column_var2.get()  # Get additional column name from entry widget
        additional_filter_condition = additional_filter_entry.get().strip()  # Get additional filter condition from entry widget
        last_selected_column = column_var3.get()
        last_filter_condition = last_filter_entry.get().strip()
        selected_operator = operator_var.get().strip()
        selected_operator2 = operator_var2.get().strip()
        selected_operator3 = operator_var3.get().strip()
        audit_selected_column = column_var_audit.get()
        audit_filter_condition = filter_entry.get().strip()

        try:
            numeric_filter_condition = float(filter_condition)
            is_numeric = True
        except ValueError:
            numeric_filter_condition = filter_condition  
            is_numeric = False
    
        result = data.copy()
        if selected_column and filter_condition and selected_operator in ['=']:
            result = result[result[selected_column].astype(str).str.strip() == filter_condition] 
        
        if selected_operator in ['<'] and is_numeric:
            result = result[data[selected_column].astype(float) < numeric_filter_condition]
        elif selected_operator in ['<='] and is_numeric:
            result = result[data[selected_column].astype(float) <= numeric_filter_condition]
        elif selected_operator in ['>'] and is_numeric:
            result = result[data[selected_column].astype(float) > numeric_filter_condition]
        elif selected_operator in ['>='] and is_numeric:
            result = result[data[selected_column].astype(float) >= numeric_filter_condition]
        

        try:
            numeric_filter_condition2 = float(additional_filter_condition)
        except ValueError:
            numeric_filter_condition2 = additional_filter_condition
            is_numeric = False
        
        if additional_selected_column and additional_filter_condition and selected_operator2 in ['=']:
            result = result[result[additional_selected_column].astype(str).str.strip() == additional_filter_condition]

        if selected_operator2 in ['<'] and is_numeric:
            result = result[data[additional_selected_column].astype(float) < numeric_filter_condition2]
        elif selected_operator2 in ['<='] and is_numeric:
            result = result[data[additional_selected_column].astype(float) <= numeric_filter_condition2]
        elif selected_operator2 in ['>'] and is_numeric:
            result = result[data[additional_selected_column].astype(float) > numeric_filter_condition2]
        elif selected_operator2 in ['>='] and is_numeric:
            result = result[data[additional_selected_column].astype(float) >= numeric_filter_condition2]


        try:
            numeric_filter_condition3 = float(last_filter_condition)
        except ValueError:
            numeric_filter_condition3 = last_filter_condition
            is_numeric = False
            
        if last_selected_column and last_filter_condition and selected_operator3 in ['=']:
            result = result[result[last_selected_column].astype(str).str.strip() == last_filter_condition]

        if selected_operator3 in ['<'] and is_numeric:
            result = result[data[last_selected_column].astype(float) < numeric_filter_condition3]
        elif selected_operator3 in ['<='] and is_numeric:
            result = result[data[last_selected_column].astype(float) <= numeric_filter_condition3]
        elif selected_operator3 in ['>'] and is_numeric:
            result = result[data[last_selected_column].astype(float) > numeric_filter_condition3]
        elif selected_operator3 in ['>='] and is_numeric:
            result = result[data[last_selected_column].astype(float) >= numeric_filter_condition3]

        # if audit_selected_column and audit_filter_condition:
        #     result = result[data[audit_selected_column] == audit_filter_condition]
        

        if not result.empty:
            save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if save_path:
                result.to_csv(save_path, index=False)
                display_data(pd.read_csv(save_path))
        else:
            tk.messagebox.showinfo("No results", "The filter conditions did not match any data.")
    else:
        tk.messagebox.showwarning(title=None, message="Please load a CSV file first.")

def update_column_options():
    """Update column options for graph plotting based on loaded data."""
    if data is not None:
        column_menu1['menu'].delete(0, 'end')
        column_menu2['menu'].delete(0, 'end')
        for column in data.columns:
            column_menu1['menu'].add_command(label=column, command=tk._setit(column_varX, column))
            column_menu2['menu'].add_command(label=column, command=tk._setit(column_varY, column))
        column_varX.set(data.columns[0])
        column_varY.set(data.columns[1] if len(data.columns) > 1 else data.columns[0])

def open_graph_window():
    """Open a separate window for graph customization and plotting."""
    global data
    if data is not None:
        # Create window for graph
        graph_window = tk.Toplevel(root)
        graph_window.title("Southern Utah University - Graph Window")

        # Plot desired graph in window
        plot_graph(graph_window, graph_type_var.get(), graph_color_var.get())
        
def plot_graph(graph_window, graph_type, colors, color='blue'):
    """Plot and update the graph in the separate window based on user selections."""
    # Create figure for desired graph for plotting   
    fig = Figure(figsize=(12, 6), dpi=100)
    ax = fig.add_subplot(111)

    # Generate a color map for unique values on the x-axis
    unique_vals = data[column_varX.get()].unique()
    if colors == "viridis":
        colors = plt.cm.get_cmap('viridis', len(unique_vals))
    elif colors == "brg":
        colors = plt.cm.get_cmap('brg', len(unique_vals))
    elif colors == "gnuplot":
        colors = plt.cm.get_cmap('gnuplot', len(unique_vals))
    elif colors == "gist_rainbow":
        colors = plt.cm.get_cmap('gist_rainbow', len(unique_vals))
    elif colors == "rainbow":
        colors = plt.cm.get_cmap('rainbow', len(unique_vals))
    elif colors == "turbo":
        colors = plt.cm.get_cmap('turbo', len(unique_vals))
    elif colors == "jet":
        colors = plt.cm.get_cmap('jet', len(unique_vals))
    elif colors == "nipy_spectral":
        colors = plt.cm.get_cmap('nipy_spectral', len(unique_vals))

    # Generate graph based on selected input
    if graph_type == "Bar":
        # For each unique value in the x-axis column, plot a bar with the mean of the y-axis values.
        for i, val in enumerate(unique_vals):
            subset = data[data[column_varX.get()] == val]
            ax.bar(val, subset[column_varY.get()].mean(), color=colors(i))  # Use mean or another aggregate for bars.
            labs = ax.bar(val, subset[column_varY.get()].mean(), color=colors(i))
            ax.bar_label(labs)

    elif graph_type == "Horizontal Bar":
        # For each unique value in the x-axis column, plot a bar with the mean of the y-axis values.
        for i, val in enumerate(unique_vals):
            subset = data[data[column_varX.get()] == val]
            ax.barh(val, subset[column_varY.get()].mean(), color=colors(i))  # Use mean or another aggregate for bars.
            ax.tick_params(axis='y', labelrotation=45, labelsize=8)
            labs = ax.barh(val, subset[column_varY.get()].mean(), color=colors(i))
            ax.bar_label(labs)

    elif graph_type == "Line":
        data_sorted = data.sort_values(by=column_varX.get())
        # x = pd.to_numeric(data_sorted[column_varX.get()], errors='coerce').dropna()
        # y = pd.to_numeric(data_sorted[column_varY.get()], errors='coerce').dropna()
        ax.plot(data_sorted[column_varX.get()], data_sorted[column_varY.get()], color='blue') 
        
    elif graph_type == "Scatter":
        # Extract x and y data, remove null values for line of best fit
        x = pd.to_numeric(data[column_varX.get()], errors='coerce').dropna()
        y = pd.to_numeric(data[column_varY.get()], errors='coerce').dropna()
        ax.scatter(x, y, c='blue', label='Data Points') # Create scatter plot
        m, b = np.polyfit(x, y, 1) # Calculate coefficients for the line of best fit
        x_fit = np.linspace(x.min(), x.max(), 100) # Generate x values for the line of best fit (from min to max x)
        y_fit = m * x_fit + b # Generate y values for the line of best fit
        ax.plot(x_fit, y_fit, 'r-', label=f'Best Fit: y={m:.2f}x+{b:.2f}') # Plot the line of best fit
        ax.legend()
        
    elif graph_type == "Pie":
        counts = data[column_varX.get()].value_counts()
        ax.pie(counts, labels=counts.index, autopct='%1.1f%%', colors=[colors(i) for i in range(len(counts))])
        ax.axis('equal')
        ax.legend()

    elif graph_type == "Histogram":
        column_data = data[column_varX.get()] # Actual data for the histogram 
        if is_numeric_dtype(column_data): # Check if data is numeric
            mu, sigma = np.mean(column_data), np.std(column_data)  # Mean and standard deviation
            n, bins, patches = ax.hist(column_data, bins='auto', color='skyblue', alpha=0.7, rwidth=0.85, density=True) # Plot histogram
            y = norm.pdf(bins, mu, sigma) # Add a line of best fit (normal PDF)
            ax.plot(bins, y, '--', color='red')  # Red dashed line for best fit
        else: # Display error and close graph window if data is not numeric
            tk.messagebox.showwarning(title=None, message="Invalid type of data. Please enter numeric data.")

    # Set labels for graph
    ax.set_xlabel(column_varX.get())
    ax.set_ylabel(column_varY.get())
    ax.set_title(f"{graph_type} Graph of {column_varX.get()} vs. {column_varY.get()}")

    # Change labels if histogram
    if graph_type == "Histogram":
        ax.set_ylabel("Density")
        ax.set_title(f"{graph_type} of {column_varX.get()}")

    if graph_type == "Bar":
        ax.set_ylabel(f"Mean of {column_varY.get()}")

    # Adjust labels if horizontal bar graph
    if graph_type == "Horizontal Bar":
        ax.set_xlabel(column_varY.get())
        ax.set_ylabel(f"Mean of {column_varX.get()}")

    if graph_type == "Pie":
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.set_title(f"Pie Graph of {column_varX.get()}")

    # Rotate x-axis labels so they fit in window
    ax.tick_params(axis='x', labelrotation=45, labelsize=8)

    # Have graph fit to borders of window
    fig.tight_layout()

    # Embedding the Matplotlib graph into the Tkinter GUI
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Embedding toolbar for Matplotlib graph
    toolbar = GraphNavigationToolbar(canvas, graph_window)
    toolbar.update()

class GraphNavigationToolbar(NavigationToolbar2Tk):
    # Class for navigation bar
    toolitems = [t for t in NavigationToolbar2Tk.toolitems if
                t[0] in ('Home', 'Pan', 'Subplots', 'Zoom', 'Save')] # Only keep necessary buttons

notebook = ttk.Notebook(root)

general_frame = ttk.Frame(notebook)  # General tab content
# graph_frame = ttk.Frame(notebook)    # Graph tab content

notebook.add(general_frame, text='General')
notebook.pack(expand=True, fill='both')

header_frame = tk.Frame(general_frame, bg="#990000", height=150)
header_frame.pack(fill=tk.X, side=tk.TOP)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)


footer_frame = tk.Frame(general_frame, bg="#cc0000", height=50)

user_label = tk.Label(footer_frame, fg="white", bg="#cc0000", font=("Helvetica", 12))

upload_button = tk.Button(header_frame, text="Upload CSV", command=load_csv, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
upload_button.grid(row=0, column=1, columnspan=1, sticky='ew', padx=10, pady=5)

column_label = tk.Label(header_frame, text="Enter Column Name:", fg="white", bg="#990000", font=("Helvetica", 12))
column_label.grid(row=1, column=0, padx=10, pady=5, sticky='ew')

column_name_combobox = ttk.Combobox(header_frame, textvariable=column_var1, state="readonly")
column_name_combobox.grid(row=2, column=0, padx=10, pady=5, sticky='ew')

filter_label = tk.Label(header_frame, text="Enter Filter Condition:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label.grid(row=5, column=0, padx=10, pady=5, sticky='ew')

filter_entry = tk.Entry(header_frame, font=("Helvetica", 12))
filter_entry.grid(row=6, column=0, padx=10, pady=5, sticky='ew')

operator_label = tk.Label(header_frame, text="Enter Operator:", fg="white", bg="#990000", font=("Helvetica", 12))
operator_label.grid(row=3, column=0, padx=10, pady=5, sticky='ew')

operator_combobox = ttk.Combobox(header_frame, textvariable=operator_var, state="readonly")
operator_combobox['values'] = ['=', '<', '<=', '>', '>=']
operator_combobox.grid(row=4, column=0, padx=10, pady=5, sticky='ew')
operator_var.set('=')

# Additional filter conditions
additional_column_label = tk.Label(header_frame, text="Enter Additional Column Name:", fg="white", bg="#990000", font=("Helvetica", 12))
additional_column_label.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

column_name_combobox2 = ttk.Combobox(header_frame, textvariable=column_var2, state="readonly")
column_name_combobox2.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

additional_filter_label = tk.Label(header_frame, text="Enter Additional Filter Condition:", fg="white", bg="#990000", font=("Helvetica", 12))
additional_filter_label.grid(row=5, column=1, padx=10, pady=5, sticky='ew')

additional_filter_entry = tk.Entry(header_frame, font=("Helvetica", 12))
additional_filter_entry.grid(row=6, column=1, padx=10, pady=5, sticky='ew')

operator_label2 = tk.Label(header_frame, text="Enter Operator:", fg="white", bg="#990000", font=("Helvetica", 12))
operator_label2.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

operator_combobox2 = ttk.Combobox(header_frame, textvariable=operator_var2, state="readonly")
operator_combobox2['values'] = ['=', '<', '<=', '>', '>=']
operator_combobox2.grid(row=4, column=1, padx=10, pady=5, sticky='ew')
operator_var2.set('=')

#last filter conditions
last_column_label = tk.Label(header_frame, text="Enter Additional Column Name:", fg="white", bg="#990000", font=("Helvetica", 12))
last_column_label.grid(row=1, column=2, padx=10, pady=5, sticky='ew')

column_name_combobox4 = ttk.Combobox(header_frame, textvariable=column_var3, state="readonly")
column_name_combobox4.grid(row=2, column=2, padx=10, pady=5, sticky='ew')

last_filter_label = tk.Label(header_frame, text="Enter Additional Filter Condition:", fg="white", bg="#990000", font=("Helvetica", 12))
last_filter_label.grid(row=5, column=2, padx=10, pady=5, sticky='ew')


last_filter_entry = tk.Entry(header_frame, font=("Helvetica", 12))
last_filter_entry.grid(row=6, column=2, padx=10, pady=5, sticky='ew')

operator_label3 = tk.Label(header_frame, text="Enter Operator:", fg="white", bg="#990000", font=("Helvetica", 12))
operator_label3.grid(row=3, column=2, padx=10, pady=5, sticky='ew')

operator_combobox3 = ttk.Combobox(header_frame, textvariable=operator_var3, state="readonly")
operator_combobox3['values'] = ['=', '<', '<=', '>', '>=']
operator_combobox3.grid(row=4, column=2, padx=10, pady=5, sticky='ew')
operator_var3.set('=')

filter_button = tk.Button(header_frame, text="Filter and Save", command=filter_and_save, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
filter_button.grid(row=7, column=1, columnspan=1, sticky='ew', padx=10, pady=10)

table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True)

# First Tab
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Seats Filled')

header_frame1 = tk.Frame(tab1, bg="#990000", height=150)
header_frame1.pack(fill=tk.X, side=tk.TOP)

upload_button1 = tk.Button(header_frame1, text="Upload CSV", command=lambda: load_csv_for_audits(1), bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
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

upload_button2 = tk.Button(header_frame2, text="Upload CSV", command=lambda: load_csv_for_audits(2), bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
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

upload_button3 = tk.Button(header_frame3, text="Upload CSV", command=lambda: load_csv_for_audits(3), bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
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

upload_button4 = tk.Button(header_frame4, text="Upload CSV", command=lambda: load_csv_for_audits(4), bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
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

upload_button5 = tk.Button(header_frame5, text="Upload CSV", command=lambda: load_csv_for_audits(5), bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
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

upload_button6 = tk.Button(header_frame6, text="Upload CSV", command=lambda: load_csv_for_audits(6), bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
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

upload_button7 = tk.Button(header_frame7, text="Upload CSV", command=lambda: load_csv_for_audits(7), bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
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

# Items for graphing purposes
graph_button_frame = tk.Frame(root) # Frame/box for graphing options/buttons
graph_button_frame.pack()
graph_type_var = tk.StringVar()
# Option to select first variable to plot against
column_menu1_label = ttk.Label(graph_button_frame, text="Select X-Axis:")
column_menu1_label.grid(row=0, column=0, padx=5, pady=5)
column_menu1_label.grid_rowconfigure(0, weight=1) 
column_menu1 = ttk.Combobox(graph_button_frame, textvariable=column_varX, state="readonly")
column_menu1.grid(row=1, column=0, padx=5, pady=5)
column_menu1.grid_rowconfigure(0, weight=1) 
# Option to select second variable to plot against
column_menu2_label = ttk.Label(graph_button_frame, text="Select Y-Axis:")
column_menu2_label.grid(row=0, column=1, padx=5, pady=5)
column_menu2 = ttk.Combobox(graph_button_frame, textvariable=column_varY, state="readonly")
column_menu2.grid(row=1, column=1, padx=5, pady=5)
# Option to select graph type
graph_type_var = tk.StringVar(root)
graph_type_var.set("Bar")  # default value
graph_types = ["Bar", "Bar", "Horizontal Bar", "Line", "Scatter", "Pie", "Histogram"]
graph_type_label = ttk.Label(graph_button_frame, text="Graph Type:")
graph_type_label.grid(row=0, column=2, padx=5, pady=5)
graph_types_button = ttk.OptionMenu(graph_button_frame, graph_type_var, *graph_types)
# graph_types_button = ttk.Combobox(graph_button_frame, textvariable=graph_types, state="readonly")
graph_types_button.grid(row=1, column=2, padx=5, pady=5)
# Option to select graph color scheme
graph_color_var = tk.StringVar(root)
graph_color_var.set("viridis")  # default matplotlib colormap
color_types = ["viridis", "viridis", "brg", "gnuplot", "gist_rainbow", "rainbow", "turbo", "jet", "nipy_spectral"] # [Add more colors if time/desired]
graph_color_label = ttk.Label(graph_button_frame, text="Color Palette:")
graph_color_label.grid(row=0, column=3, padx=5, pady=5)
graph_color_button = ttk.OptionMenu(graph_button_frame, graph_color_var, *color_types)
# graph_color_button = ttk.Combobox(graph_button_frame, textvariable=color_types, state="readonly")
graph_color_button.grid(row=1, column=3, padx=5, pady=5)
# Button to open window containing graph
ttk.Button(root, text="Open Graph Window", command=open_graph_window).pack(side=BOTTOM, pady=10)

# Continue with the rest of your application setup

root.mainloop()