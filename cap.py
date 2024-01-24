import tkinter as tk
from tkinter import filedialog
import pandas as pd
from pandastable import Table

def load_csv():
    """Load a CSV file and display its contents."""
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        data = pd.read_csv(file_path)
        pt = Table(data_frame, dataframe=data, showtoolbar=False, showstatusbar=True)
        pt.show()

# Create the main window
root = tk.Tk()
root.title("CSV File Viewer")

# Create a frame for the Table widget
data_frame = tk.Frame(root)
data_frame.pack(fill=tk.BOTH, expand=True)

# Add a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add menu items
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open CSV", command=load_csv)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Run the application
root.mainloop()
