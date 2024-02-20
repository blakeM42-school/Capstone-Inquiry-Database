import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
from pandastable import Table
import ttkbootstrap as tb

data = None  # Global variable to store loaded data

def load_csv():
    """Load a CSV file and display its contents."""
    global data  # Use the global variable to store loaded data
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            data = pd.read_csv(file_path, encoding='utf-8')
        except UnicodeDecodeError:
            # Try reading with a different encoding (e.g., 'latin-1')
            data = pd.read_csv(file_path, encoding='latin-1')

        for widget in table_frame.winfo_children():
            widget.destroy()
        table = Table(table_frame, dataframe=data, showtoolbar=True, showstatusbar=True)
        table.show()

def filter_and_save():
    """Filter the loaded data and save it as a new CSV file."""
    global data  # Access the global variable containing loaded data
    if data is not None:
        column_name = column_entry.get()  # Get column name from entry widget
        filter_condition = filter_entry.get()  # Get filter condition from entry widget
        result = data[data[column_name] == filter_condition]
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        
        if save_path:
            result.to_csv(save_path, index=False)
    else:
        print("Please load a CSV file first.")


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

# Initialize the main window
root = tb.Window(themename="superhero")
root.title("Southern Utah University - College Sort")
root.geometry('500x500')

# Create the notebook (tab controller)
notebook = ttk.Notebook(root)

# Create the frames for each tab
general_frame = ttk.Frame(notebook)  # General tab content
audit_frame = ttk.Frame(notebook)    # Audit tab content

# Add frames to notebook as tabs
notebook.add(general_frame, text='General')
notebook.add(audit_frame, text='Audit')
notebook.pack(expand=True, fill='both')

# Now, replicate your existing UI components inside general_frame
# For example:
header_frame = tk.Frame(general_frame, bg="#990000", height=150)
header_frame.pack(fill=tk.X, side=tk.TOP)

footer_frame = tk.Frame(general_frame, bg="#cc0000", height=50)
footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

user_label = tk.Label(footer_frame, fg="white", bg="#cc0000", font=("Helvetica", 12))
user_label.pack(side=tk.LEFT, padx=10)

upload_button = tk.Button(header_frame, text="Upload CSV", command=load_csv, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
upload_button.pack(pady=5)

column_label = tk.Label(header_frame, text="Enter Column Name:", fg="white", bg="#990000", font=("Helvetica", 12))
column_label.pack(pady=5)

column_entry = tk.Entry(header_frame, font=("Helvetica", 12))
column_entry.pack(pady=5)

filter_label = tk.Label(header_frame, text="Enter Filter Condition:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label.pack(pady=5)

filter_entry = tk.Entry(header_frame, font=("Helvetica", 12))
filter_entry.pack(pady=5)

filter_button = tk.Button(header_frame, text="Filter and Save", command=filter_and_save, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
filter_button.pack(pady=5)

table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True)
# You can create a separate UI for the 'Audit' tab in audit_frame
# For example, just a label for now


header_frame2 = tk.Frame(audit_frame, bg="#990000", height=150)
header_frame2.pack(fill=tk.X, side=tk.TOP)

footer_frame2 = tk.Frame(audit_frame, bg="#cc0000", height=50)
footer_frame2.pack(fill=tk.X, side=tk.BOTTOM)

user_label2 = tk.Label(footer_frame2, fg="white", bg="#cc0000", font=("Helvetica", 12))
user_label2.pack(side=tk.LEFT, padx=10)

upload_button2 = tk.Button(header_frame2, text="Upload CSV", command=load_csv, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
upload_button2.pack(pady=5)

column_label2 = tk.Label(header_frame2, text="Enter Column Name:", fg="white", bg="#990000", font=("Helvetica", 12))
column_label2.pack(pady=5)

column_entry2 = tk.Entry(header_frame2, font=("Helvetica", 12))
column_entry2.pack(pady=5)

filter_label2 = tk.Label(header_frame2, text="Enter Filter Condition:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label2.pack(pady=5)

filter_entry2 = tk.Entry(header_frame2, font=("Helvetica", 12))
filter_entry2.pack(pady=5)

filter_button2 = tk.Button(header_frame2, text="Filter and Save", command=filter_and_save, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
filter_button2.pack(pady=5)

table_frame2 = tk.Frame(root)
table_frame2.pack(fill=tk.BOTH, expand=True)

# ... Additional UI setup for the 'Audit' tab ...

# Continue with the rest of your application setup


column_varX = tk.StringVar(general_frame)
column_varY = tk.StringVar(general_frame)
ttk.Label(general_frame, text="Select X-Axis:").pack()
column_menu1 = ttk.OptionMenu(general_frame, column_varX, "None")
column_menu1.pack(pady=5)
ttk.Label(general_frame, text="Select Y-Axis:").pack()
column_menu2 = ttk.OptionMenu(general_frame, column_varY, "None")
column_menu2.pack(pady=5)


root.mainloop()






# column_menu1 = ttk.OptionMenu(root, column_varX, "None")
