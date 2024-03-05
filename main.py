import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
from pandastable import Table
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

root = tb.Window(themename="superhero")
root.title("Southern Utah University - College Sort")
root.geometry('500x500')

column_var1 = tk.StringVar()
column_var2 = tk.StringVar()
column_var3 = tk.StringVar()
column_var_audit = tk.StringVar()
column_varX = tk.StringVar(root)
column_varY = tk.StringVar(root)

data = None  # Global variable to store loaded data

def load_csv():
    """Load a CSV file and display its contents."""
    global data, column_var1, column_var2, column_var3, column_var_audit, column_varX, column_varY  # Use the global variable to store loaded data
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            data = pd.read_csv(file_path, encoding='utf-8')
            for widget in table_frame.winfo_children():
                widget.destroy()
            table = Table(table_frame, dataframe=data, showstatusbar=True) # Removed 'showtoolbar' option from table, can add back later if need be/want to
            table.show()
            
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

        print(data.head())  # Prints the first 5 rows of the DataFrame

        selected_column = column_var1.get()
        filter_condition = filter_entry.get().strip()  # Get filter condition from entry widget
        additional_selected_column = column_var2.get()  # Get additional column name from entry widget
        additional_filter_condition = additional_filter_entry.get().strip()  # Get additional filter condition from entry widget
        last_selected_column = column_var3.get()
        last_filter_condition = last_filter_entry.get().strip()
        audit_selected_column = column_var_audit.get()
        audit_filter_condition = filter_entry.get().strip()

    

        result = data
        if selected_column and filter_condition:
            result = result[result[selected_column].astype(str).str.strip() == filter_condition]
        
        if additional_selected_column and additional_filter_condition:
            result = result[result[additional_selected_column].astype(str).str.strip() == additional_filter_condition]
        
        if last_selected_column and last_filter_condition:
            result = result[result[last_selected_column].astype(str).str.strip() == last_filter_condition]

        # if audit_selected_column and audit_filter_condition:
        #     result = result[data[audit_selected_column] == audit_filter_condition]
        
        print(f"Filter on {selected_column} for {filter_condition}")
        print(f"Data type in DataFrame: {data[selected_column].dtype}")
        print(f"Type of filter condition: {type(filter_condition)}")
    

        if not result.empty:
            save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if save_path:
                result.to_csv(save_path, index=False)
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
        graph_window = tk.Toplevel(root)
        graph_window.title("Graph Customization")

        # Initial graph plot
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
    # Add more color types if needed as project continues

    # Generate graph based on selected input
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
        # column_varY = None
        data[column_varX.get()].hist(ax=ax, bins=len(unique_vals), color=[colors(i) for i in range(len(unique_vals))])
    # Add more graph types if needed as project continues

    # Set labels for graph
    ax.set_xlabel(column_varX.get())
    ax.set_ylabel(column_varY.get())
    ax.set_title(f"{graph_type} Graph of {column_varX.get()} vs. {column_varY.get()}")

    # if graph_type == "Bar" | graph_type == "Line" | graph_type == "Pie":
    #     ax.set_title(f"{graph_type} Graph of {column_varX.get()} vs. {column_varY.get()}")
    # elif graph_type == "Scatter": 
    #     ax.set_title(f"{graph_type} Plot of {column_varX.get()} vs. {column_varY.get()}")
    # elif graph_type == "Histogram":
    #     ax.set_title(f"{graph_type} of {column_varX.get()} vs. {column_varY.get()}")

    ax.tick_params(axis='x', labelrotation=45, labelsize=8)
    if graph_type in ["Line", "Scatter"]:
        ax.legend(title=column_varX.get())

    # Embedding the Matplotlib graph into the Tkinter GUI
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Embedding toolbar for Matplotlib graph
    toolbar = GraphNavigationToolbar(canvas, graph_window)
    toolbar.update()
    # canvas.get_tk_widget().pack()

class GraphNavigationToolbar(NavigationToolbar2Tk):
    # Class for navigation bar
    toolitems = [t for t in NavigationToolbar2Tk.toolitems if
                t[0] in ('Home', 'Pan', 'Zoom', 'Save')] # Only keep necessary buttons

notebook = ttk.Notebook(root)

general_frame = ttk.Frame(notebook)  # General tab content
audit_frame = ttk.Frame(notebook)    # Audit tab content
# graph_frame = ttk.Frame(notebook)    # Graph tab content

notebook.add(general_frame, text='General')
notebook.add(audit_frame, text='Audit')
# notebook.add(graph_frame, text='Graph')
notebook.pack(expand=True, fill='both')

# Now, replicate your existing UI components inside general_frame
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
filter_label.grid(row=3, column=0, padx=10, pady=5, sticky='ew')

filter_entry = tk.Entry(header_frame, font=("Helvetica", 12))
filter_entry.grid(row=4, column=0, padx=10, pady=5, sticky='ew')

# Additional filter conditions
additional_column_label = tk.Label(header_frame, text="Enter Additional Column Name:", fg="white", bg="#990000", font=("Helvetica", 12))
additional_column_label.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

column_name_combobox2 = ttk.Combobox(header_frame, textvariable=column_var2, state="readonly")
column_name_combobox2.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

additional_filter_label = tk.Label(header_frame, text="Enter Additional Filter Condition:", fg="white", bg="#990000", font=("Helvetica", 12))
additional_filter_label.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

additional_filter_entry = tk.Entry(header_frame, font=("Helvetica", 12))
additional_filter_entry.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

#last filter conditions
last_column_label = tk.Label(header_frame, text="Enter Additional Column Name:", fg="white", bg="#990000", font=("Helvetica", 12))
last_column_label.grid(row=1, column=2, padx=10, pady=5, sticky='ew')

column_name_combobox4 = ttk.Combobox(header_frame, textvariable=column_var3, state="readonly")
column_name_combobox4.grid(row=2, column=2, padx=10, pady=5, sticky='ew')

last_filter_label = tk.Label(header_frame, text="Enter Additional Filter Condition:", fg="white", bg="#990000", font=("Helvetica", 12))
last_filter_label.grid(row=3, column=2, padx=10, pady=5, sticky='ew')


last_filter_entry = tk.Entry(header_frame, font=("Helvetica", 12))
last_filter_entry.grid(row=4, column=2, padx=10, pady=5, sticky='ew')

filter_button = tk.Button(header_frame, text="Filter and Save", command=filter_and_save, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
filter_button.grid(row=5, column=1, columnspan=1, sticky='ew', padx=10, pady=10)

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

column_name_combobox3 = ttk.Combobox(header_frame2, textvariable=column_var_audit, state="readonly")
column_name_combobox3.pack(pady=5)

filter_label2 = tk.Label(header_frame2, text="Enter Filter Condition:", fg="white", bg="#990000", font=("Helvetica", 12))
filter_label2.pack(pady=5)

filter_entry2 = tk.Entry(header_frame2, font=("Helvetica", 12))
filter_entry2.pack(pady=5)

filter_button2 = tk.Button(header_frame2, text="Filter and Save", command=filter_and_save, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
filter_button2.pack(pady=5)

table_frame2 = tk.Frame(root)
table_frame2.pack(fill=tk.BOTH, expand=True)

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
graph_types = ["Bar", "Bar", "Line", "Scatter", "Pie", "Histogram"]
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






