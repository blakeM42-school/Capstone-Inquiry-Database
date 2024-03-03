import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

# Initial setup
root = tk.Tk()
root.title("Data Visualization Tool")

data = None  # Global variable for loaded data


def load_csv():
    global data
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        data = pd.read_csv(file_path)
        update_column_options()

# def update_column_options():
#     if data is not None:
#         for menu in [x_menu_graph, y_menu_graph]:
#             menu["menu"].delete(0, "end")
#             for column in data.columns:
#                 menu["menu"].add_command(label=column, command=lambda value=column: var.set(value))
#         x_var_graph.set(data.columns[0])
#         y_var_graph.set(data.columns[0])

def update_column_options():
    """Update column options for graph plotting based on loaded data."""
    if data is not None:
        column_menu1['menu'].delete(0, 'end')
        column_menu2['menu'].delete(0, 'end')
        for column in data.columns:
            column_menu1['menu'].add_command(label=column, command=tk._setit(column_varX, column))
            column_menu2['menu'].add_command(label=column, command=tk._setit(column_varY, column))
        column_varX.set(data.columns[0])
        column_varY.set(data.columns[0])

def open_graph_window():
    global x_var_graph, y_var_graph, color_var
    graph_window = tk.Toplevel(root)
    graph_window.title("Graph Customization")

    # Variable Selection Setup
    x_var_graph = tk.StringVar(graph_window)
    y_var_graph = tk.StringVar(graph_window)
    x_var_graph.set(data.columns[0])
    y_var_graph.set(data.columns[1] if len(data.columns) > 1 else data.columns[0])

    ttk.Label(graph_window, text="X Axis:").pack()
    x_menu_graph = ttk.OptionMenu(graph_window, x_var_graph, *data.columns)
    x_menu_graph.pack()

    ttk.Label(graph_window, text="Y Axis:").pack()
    y_menu_graph = ttk.OptionMenu(graph_window, y_var_graph, *data.columns)
    y_menu_graph.pack()

    # Graph Type and Update Button
    graph_type_var = tk.StringVar(graph_window)
    graph_types = ["Bar", "Line", "Scatter", "Pie", "Histogram"]
    graph_type_var.set(graph_types[0])
    ttk.OptionMenu(graph_window, graph_type_var, *graph_types).pack()
    ttk.Button(graph_window, text="Update Graph", command=lambda: plot_graph(graph_window, graph_type_var.get())).pack()

    # Save Graph Button
    ttk.Button(graph_window, text="Save Graph", command=save_graph).pack()

    # Color Palette Option
    ttk.Label(graph_window, text="Color Palette:").pack()
    color_var = tk.StringVar(graph_window)
    color_var.set("viridis")  # default matplotlib colormap
    ttk.OptionMenu(graph_window, color_var, *plt.colormaps(), command=lambda _: plot_graph(graph_window, graph_type_var.get())).pack()

def plot_graph(frame, graph_type):
    for widget in frame.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg) or isinstance(widget, NavigationToolbar2Tk):
            widget.destroy()

    fig = Figure(figsize=(5, 4), tight_layout=True)
    ax = fig.add_subplot(111)

    # Adjust this plotting logic to fit your data and graph types
    if graph_type == "Bar":
        ax.bar(data[x_var_graph.get()], data[y_var_graph.get()], color=plt.set_cmap(color_var.get()))
    # Add other graph types here

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    canvas.get_tk_widget().pack()

def save_graph(fig):
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    if file_path:
        fig.savefig(file_path)

# Load CSV button
ttk.Button(root, text="Load CSV", command=load_csv).pack()

# color_var = tk.StringVar(root)
column_varX = tk.StringVar(root)
column_varY = tk.StringVar(root)
# ttk.Label(root, text="Select X-Axis:").pack()
column_menu1 = ttk.OptionMenu(root, column_varX, "None")
# column_menu1.pack(pady=5)
# ttk.Label(root, text="Select Y-Axis:").pack()
column_menu2 = ttk.OptionMenu(root, column_varY, "None")
# column_menu2.pack(pady=5)

# Button to open graph customization window
ttk.Button(root, text="Open Graph Window", command=open_graph_window).pack()

root.mainloop()
