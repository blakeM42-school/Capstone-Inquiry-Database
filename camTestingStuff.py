import tkinter as tk
from tkinter import ttk, filedialog, Scrollbar
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initial setup
root = tk.Tk()
root.title("Data Visualization Tool")

data = None  # Global variable for loaded data

def load_csv():
    """Load a CSV file and display its contents."""
    global data
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        data = pd.read_csv(file_path)
        update_column_options()

def update_column_options():
    """Update column options for graph plotting based on loaded data."""
    if data is not None:
        for var, menu in [(x_var_graph, x_menu_graph), (y_var_graph, y_menu_graph)]:
            menu['menu'].delete(0, 'end')
            for column in data.columns:
                menu['menu'].add_command(label=column, command=tk._setit(var, column))
        x_var_graph.set(data.columns[0])
        y_var_graph.set(data.columns[1] if len(data.columns) > 1 else data.columns[0])

def transform_variables(column_name):
    """Transform variables to appropriate types if necessary."""
    if data[column_name].dtype == np.object_:
        try:
            data[column_name] = pd.to_numeric(data[column_name])
        except ValueError:
            data[column_name] = data[column_name].astype('category')

def open_graph_window():
    """Open a separate window for graph customization and plotting."""
    global data, x_var_graph, y_var_graph, x_menu_graph, y_menu_graph
    if data is not None:
        graph_window = tk.Toplevel(root)
        graph_window.title("Graph Customization")

        # Make the graph window scrollable
        canvas = tk.Canvas(graph_window)
        scrollbar_y = tk.Scrollbar(graph_window, orient="vertical", command=canvas.yview)
        scrollbar_x = tk.Scrollbar(graph_window, orient="horizontal", command=canvas.xview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        # Graph type selection
        graph_type_var = tk.StringVar(scrollable_frame)
        graph_type_var.set("Bar")  # default value
        graph_types = ["Bar", "Line", "Scatter", "Pie", "Histogram"]
        ttk.Label(scrollable_frame, text="Graph Type:").grid(row=0, column=0)
        graph_type_menu = ttk.OptionMenu(scrollable_frame, graph_type_var, *graph_types)
        graph_type_menu.grid(row=0, column=1)

        # Variables for axes
        x_var_graph = tk.StringVar(scrollable_frame)
        y_var_graph = tk.StringVar(scrollable_frame)
        x_var_graph.set(data.columns[0])
        y_var_graph.set(data.columns[1] if len(data.columns) > 1 else data.columns[0])

        # Dropdown for X Axis
        ttk.Label(scrollable_frame, text="X Axis:").grid(row=1, column=0)
        x_menu_graph = ttk.OptionMenu(scrollable_frame, x_var_graph, *data.columns)
        x_menu_graph.grid(row=1, column=1)

        # Dropdown for Y Axis
        ttk.Label(scrollable_frame, text="Y Axis:").grid(row=2, column=0)
        y_menu_graph = ttk.OptionMenu(scrollable_frame, y_var_graph, *data.columns)
        y_menu_graph.grid(row=2, column=1)

        # Update button
        update_button = ttk.Button(scrollable_frame, text="Update Graph",
                                   command=lambda: plot_graph(scrollable_frame, graph_type_var.get(), x_var_graph.get(), y_var_graph.get()))
        update_button.grid(row=3, column=0, columnspan=2)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")

def plot_graph(graph_window, graph_type, x_var_val, y_var_val):
    """Plot and update the graph in the separate window based on user selections."""
    transform_variables(x_var_val)
    if y_var_val != x_var_val:
        transform_variables(y_var_val)

    # Clear previous figures if any
    for widget in graph_window.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()

    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Plot according to the selected graph type
    if graph_type == "Bar":
        data.groupby(x_var_val)[y_var_val].mean().plot(kind='bar', ax=ax)
    elif graph_type == "Line":
        data.plot(kind='line', x=x_var_val, y=y_var_val, ax=ax)
    elif graph_type == "Scatter":
        data.plot(kind='scatter', x=x_var_val, y=y_var_val, ax=ax)
    elif graph_type == "Pie" and y_var_val == x_var_val:
        data[x_var_val].value_counts().plot(kind='pie', ax=ax, autopct='%1.1f%%')
    elif graph_type == "Histogram":
        data[x_var_val].plot(kind='hist', ax=ax, bins=30)

    ax.set_xlabel(x_var_val, fontsize=10)
    ax.set_ylabel(y_var_val, fontsize=10)
    ax.set_title(f"{graph_type} Graph of {x_var_val} vs. {y_var_val}", fontsize=12)
    ax.tick_params(axis='x', labelrotation=45, labelsize=8)

    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Load CSV button
ttk.Button(root, text="Load CSV", command=load_csv).pack()

# Button to open graph customization window
ttk.Button(root, text="Open Graph Window", command=open_graph_window).pack()

root.mainloop()
