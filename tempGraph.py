
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
import pandas as pd
from pandastable import Table
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data = None  # Global variable to store loaded data

def load_csv():
    """Load a CSV file and display its contents."""
    global data  # Use the global variable to store loaded data
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            data = pd.read_csv(file_path, encoding='utf-8')
            update_column_options()
        except UnicodeDecodeError:
            # Try reading with a different encoding (e.g., 'latin-1')
            data = pd.read_csv(file_path, encoding='latin-1')
            update_column_options()

        for widget in table_frame.winfo_children():
            widget.destroy()
        table = Table(table_frame, dataframe=data, showstatusbar=True)
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

def open_graph_window():
    """Open a separate window for graph customization and plotting."""
    global data
    if data is not None:
        graph_window = tk.Toplevel(root)
        graph_window.title("Graph Customization")

        # Dropdown for selecting the graph type
        graph_type_var = tk.StringVar(graph_window)
        graph_type_var.set("Bar")  # default value
        graph_types = ["Bar", "Line", "Scatter", "Pie", "Histogram"]
        ttk.Label(graph_window, text="Graph Type:").pack()
        ttk.OptionMenu(graph_window, graph_type_var, *graph_types).pack(pady=5)

        # Button to update graph
        ttk.Button(graph_window, text="Update Graph", command=lambda: plot_graph(graph_window, graph_type_var.get())).pack(pady=5)

        # Initial graph plot
        plot_graph(graph_window, graph_type_var.get())
        
def plot_graph(graph_window, graph_type, color='blue'):
    """Plot and update the graph in the separate window based on user selections."""
    # Clear previous figures
    for widget in graph_window.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()
   
    fig = Figure(figsize=(12, 6), dpi=100)
    ax = fig.add_subplot(111)

    # Generate a color map for unique values on the x-axis
    unique_vals = data[column_varX.get()].unique()
    colors = plt.cm.get_cmap('viridis', len(unique_vals))

    if graph_type in ["Bar", "Line", "Scatter"]:
        for i, val in enumerate(unique_vals):
            subset = data[data[column_varX.get()] == val]
            if graph_type == "Bar":
                ax.bar(val, subset[column_varY.get()].mean(), color=colors(i))  # Example: mean value for bars
            elif graph_type == "Line":
                ax.plot(subset[column_varX.get()], subset[column_varY.get()], color=colors(i), label=val)
            elif graph_type == "Scatter":
                ax.scatter(subset[column_varX.get()], subset[column_varY.get()], color=colors(i), label=val)
    elif graph_type == "Pie":
        counts = data[column_varX.get()].value_counts()
        ax.pie(counts, labels=counts.index, autopct='%1.1f%%', colors=[colors(i) for i in range(len(counts))])
    elif graph_type == "Histogram":
        data[column_varX.get()].hist(ax=ax, bins=len(unique_vals), color=[colors(i) for i in range(len(unique_vals))])

    ax.set_xlabel(column_varX.get())
    ax.set_ylabel(column_varY.get())
    ax.set_title(f"{graph_type} Graph of {column_varX.get()} vs. {column_varY.get()}")
    # fig.autofmt_xdate(rotation=45)
    ax.tick_params(axis='x', labelrotation=45, labelsize=8)
    if graph_type in ["Line", "Scatter"]:
        ax.legend(title=column_varX.get())

    # Embedding the Matplotlib graph into the Tkinter GUI
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root = tb.Window(themename="superhero")
root.title("Southern Utah University - College Sort")
# root.iconbitmap('gonza/Code/Capstone-Inquiry-Database/favicon.ico')
root.geometry('500x500')

header_frame = tk.Frame(root, bg="#990000", height=150)
header_frame.pack(fill=tk.X, side=tk.TOP)

footer_frame = tk.Frame(root, bg="#cc0000", height=50)
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

graph_type_var = tk.StringVar()

table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True)

# Column selection for graph plotting
column_varX = tk.StringVar(root)
column_varY = tk.StringVar(root)
ttk.Label(root, text="Select X-Axis:").pack()
column_menu1 = ttk.OptionMenu(root, column_varX, "None")
column_menu1.pack(pady=5)
ttk.Label(root, text="Select Y-Axis:").pack()
column_menu2 = ttk.OptionMenu(root, column_varY, "None")
column_menu2.pack(pady=5)

ttk.Button(root, text="Open Graph Window", command=open_graph_window).pack()

root.mainloop()
