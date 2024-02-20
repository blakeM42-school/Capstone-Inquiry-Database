import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
from pandastable import Table
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("Southern Utah University - College Sort")
root.geometry('500x500')

column_var = tk.StringVar()

data = None  # Global variable to store loaded data


def load_csv():
    """Load a CSV file and display its contents."""
    global data, column_var  # Use the global variable to store loaded data
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            data = pd.read_csv(file_path, encoding='utf-8')
            for widget in table_frame.winfo_children():
                widget.destroy()
            table = Table(table_frame, dataframe=data, showtoolbar=True, showstatusbar=True)
            table.show()
            
            column_name_combobox['values'] = data.columns.tolist()
            if data.columns.tolist():
                column_var.set(data.columns.tolist()[0])  # Set the default value to the first column name
        except UnicodeDecodeError:
            data = pd.read_csv(file_path, encoding='latin-1')


def filter_and_save():
    """Filter the loaded data and save it as a new CSV file."""
    global data  # Access the global variable containing loaded data
    if data is not None:
        selected_column = column_var.get()
        filter_condition = filter_entry.get().strip()  # Get filter condition from entry widget
        result = data[data[selected_column] == filter_condition]
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        
        if save_path:
            result.to_csv(save_path, index=False)
    else:
        tk.messagebox.showwarning(title=None, message="Please load a CSV file first.")

notebook = ttk.Notebook(root)

general_frame = ttk.Frame(notebook)  # General tab content
audit_frame = ttk.Frame(notebook)    # Audit tab content
graph_frame = ttk.Frame(notebook)    # Graph tab content

notebook.add(general_frame, text='General')
notebook.add(audit_frame, text='Audit')
notebook.add(graph_frame, text='Graph')
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

column_name_combobox = ttk.Combobox(header_frame, textvariable=column_var, state="readonly")
column_name_combobox.pack(pady=5)

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

column_name_combobox2 = ttk.Combobox(header_frame2, textvariable=column_var, state="readonly")
column_name_combobox2.pack(pady=5)

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


root.mainloop()






# column_menu1 = ttk.OptionMenu(root, column_varX, "None")
