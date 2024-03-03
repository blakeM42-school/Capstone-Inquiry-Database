import tkinter as tk
from tkinter import ttk, messagebox, filedialog
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
        column_varY.set(data.columns[1] if len(data.columns) > 1 else data.columns[0])

def open_graph_window():
    global data, x_var_graph, y_var_graph
    if data is not None:
        graph_window = tk.Toplevel(root)
        graph_window.title("Graph Customization")

        # Scrollable Canvas Setup
        canvas = tk.Canvas(graph_window)
        scrollbar = tk.Scrollbar(graph_window, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Variable Selection Setup
        x_var_graph = tk.StringVar(scrollable_frame)
        y_var_graph = tk.StringVar(scrollable_frame)
        x_var_graph.set(data.columns[0])
        y_var_graph.set(data.columns[1] if len(data.columns) > 1 else data.columns[0])

        ttk.Label(scrollable_frame, text="X Axis:").grid(row=0, column=0)
        x_menu_graph = ttk.OptionMenu(scrollable_frame, x_var_graph, *data.columns)
        x_menu_graph.grid(row=0, column=1)

        ttk.Label(scrollable_frame, text="Y Axis:").grid(row=1, column=0)
        y_menu_graph = ttk.OptionMenu(scrollable_frame, y_var_graph, *data.columns)
        y_menu_graph.grid(row=1, column=1)

        # Graph Type and Update Button
        graph_type_var = tk.StringVar(scrollable_frame)
        graph_types = ["Bar", "Line", "Scatter", "Pie", "Histogram"]
        graph_type_var.set(graph_types[0])
        ttk.OptionMenu(scrollable_frame, graph_type_var, *graph_types).grid(row=2, column=0, columnspan=2)
        ttk.Button(scrollable_frame, text="Update Graph", command=lambda: plot_graph(scrollable_frame, graph_type_var.get())).grid(row=3, column=0, columnspan=2)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

def plot_graph(frame, graph_type):
    # Clear previous graph
    for widget in frame.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg) or isinstance(widget, NavigationToolbar2Tk):
            widget.destroy()

    fig = Figure(figsize=(12, 6), tight_layout=True)
    ax = fig.add_subplot(111)

    # Basic graph plotting logic (needs to be adapted based on actual data and graph types)
    # if graph_type == "Bar":
    #     ax.bar(data[x_var_graph.get()], data[y_var_graph.get()])
    # elif graph_type == "Line":
    #     ax.plot(data[x_var_graph.get()], data[y_var_graph.get()])
    # elif graph_type == "Scatter":
    #     ax.scatter(data[x_var_graph.get()], data[y_var_graph.get()])
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
    else:
        messagebox.showwarning("Incompatible Graph Type", "The selected graph type is not compatible with the selected variables.")

    ax.set_xlabel(column_varX.get())
    ax.set_ylabel(column_varY.get())
    ax.set_title(f"{graph_type} Graph of {column_varX.get()} vs. {column_varY.get()}")
    # fig.autofmt_xdate(rotation=45)
    ax.tick_params(axis='x', labelrotation=45, labelsize=8)
    if graph_type in ["Line", "Scatter"]:
        ax.legend(title=column_varX.get())

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=2)

    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    canvas.get_tk_widget().grid(row=5, column=0, columnspan=2)

# Load CSV button
ttk.Button(root, text="Load CSV", command=load_csv).pack()

# Column selection for graph plotting
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
