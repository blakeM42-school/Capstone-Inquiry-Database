
import tkinter as tk
from tkinter import ttk, colorchooser
from tkinter import filedialog
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

        # Color chooser
        color_var = tk.StringVar(graph_window)
        ttk.Button(graph_window, text="Choose Color", command=lambda: choose_color(graph_window, color_var)).pack(pady=5)

        # Initial graph plot
        plot_graph(graph_window, graph_type_var.get())

        # Button to update graph
        ttk.Button(graph_window, text="Update Graph", command=lambda: plot_graph(graph_window, graph_type_var.get())).pack(pady=5)

def choose_color(graph_window, color_var):
    """Open a color chooser dialog and update the graph color."""
    color_code = colorchooser.askcolor(title="Choose color")[1]
    if color_code:
        color_var.set(color_code)
        plot_graph(graph_window, graph_type_var.get(), color_code)

def plot_graph(graph_window, graph_type, color='blue'):
    """Plot and update the graph in the separate window based on user selections."""
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    if graph_type in ["Bar", "Line", "Scatter"]:
        x_data = data[column_varX.get()]
        y_data = data[column_varY.get()] if graph_type != "Pie" else data[column_varX.get()].value_counts()
        
        if graph_type == "Bar":
            ax.bar(x_data, y_data, color=color)
        elif graph_type == "Line":
            ax.plot(x_data, y_data, color=color)
        elif graph_type == "Scatter":
            ax.scatter(x_data, y_data, color=color)
    elif graph_type == "Pie":
        y_data.plot(kind='pie', ax=ax, autopct='%1.1f%%', colors=[color])
    elif graph_type == "Histogram":
        data[column_varX.get()].plot(kind='hist', ax=ax, color=color)

    # Update labels and title dynamically
    ax.set_xlabel(column_varX.get())
    ax.set_ylabel(column_varY.get() if graph_type != "Pie" else "")
    ax.set_title(f"{graph_type} Graph")

    # Clear previous figures
    for widget in graph_window.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()

    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

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

# Added part for graph type selection and plotting
# graph_type_label = tk.Label(header_frame, text="Select Graph Type:", fg="white", bg="#990000", font=("Helvetica", 12))
# graph_type_label.pack(pady=5)

# graph_types = ["Bar", "Line", "Scatter"]  # Add more types as needed
graph_type_var = tk.StringVar()
# graph_type_var.set(graph_types[0])  # default value
# graph_type_menu = ttk.OptionMenu(header_frame, graph_type_var, *graph_types)
# graph_type_menu.pack(pady=5)

# plot_graph_button = tk.Button(header_frame, text="Plot Graph", command=lambda: plot_graph(column_entry.get()), bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
# plot_graph_button.pack(pady=5)

table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True)

# Frame for plotting graphs
plot_frame = tk.Frame(root)
plot_frame.pack(fill=tk.BOTH, expand=True)

# Variable selection for x and y axes
# x_var = tk.StringVar(root)
# y_var = tk.StringVar(root)
# ttk.Label(root, text="X Axis:").pack()
# x_menu = ttk.OptionMenu(root, x_var, "None")
# x_menu.pack()
# ttk.Label(root, text="Y Axis:").pack()
# y_menu = ttk.OptionMenu(root, y_var, "None")
# y_menu.pack()

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
