import tkinter as tk
from tkinter import ttk, colorchooser
from tkinter import filedialog
import pandas as pd
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
        for menu in [x_menu, y_menu]:
            menu['menu'].delete(0, 'end')
            for column in data.columns:
                menu['menu'].add_command(label=column, command=tk._setit(x_var if menu is x_menu else y_var, column))
        x_var.set(data.columns[0])
        y_var.set(data.columns[1] if len(data.columns) > 1 else data.columns[0])

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
        graph_type_menu = ttk.OptionMenu(graph_window, graph_type_var, *graph_types, command=lambda _: plot_graph(graph_window, graph_type_var.get()))
        graph_type_menu.pack()

        # Color chooser
        color_var = tk.StringVar(graph_window)
        ttk.Button(graph_window, text="Choose Color", command=lambda: choose_color(graph_window, color_var)).pack()

        # Initial graph plot
        plot_graph(graph_window, graph_type_var.get())

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
        x_data = data[x_var.get()]
        y_data = data[y_var.get()] if graph_type != "Pie" else data[x_var.get()].value_counts()
        
        if graph_type == "Bar":
            ax.bar(x_data, y_data, color=color)
        elif graph_type == "Line":
            ax.plot(x_data, y_data, color=color)
        elif graph_type == "Scatter":
            ax.scatter(x_data, y_data, color=color)
    elif graph_type == "Pie":
        y_data.plot(kind='pie', ax=ax, autopct='%1.1f%%', colors=[color])
    elif graph_type == "Histogram":
        data[x_var.get()].plot(kind='hist', ax=ax, color=color)

    # Update labels and title dynamically
    ax.set_xlabel(x_var.get())
    ax.set_ylabel(y_var.get() if graph_type != "Pie" else "")
    ax.set_title(f"{graph_type} Graph")

    # Embedding the Matplotlib graph into the Tkinter GUI
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Load CSV button
ttk.Button(root, text="Load CSV", command=load_csv).pack()

header_frame = tk.Frame(root, bg="#990000", height=150)

# Variable selection for x and y axes
x_var = tk.StringVar(root)
y_var = tk.StringVar(root)
ttk.Label(root, text="X Axis:").pack()
x_menu = ttk.OptionMenu(root, x_var, "None")
x_menu.pack()
ttk.Label(root, text="Y Axis:").pack()
y_menu = ttk.OptionMenu(root, y_var, "None")
y_menu.pack()

graph_types = ["Bar", "Line", "Scatter"]  # Add more types as needed
graph_type_var = tk.StringVar()
graph_type_var.set(graph_types[0])  # default value
graph_type_menu = ttk.OptionMenu(header_frame, graph_type_var, *graph_types)
graph_type_menu.pack(pady=5)

# Button to open graph customization window
ttk.Button(root, text="Open Graph Window", command=open_graph_window).pack()

root.mainloop()
