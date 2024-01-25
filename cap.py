import tkinter as tk
from tkinter import filedialog
import pandas as pd
from pandastable import Table

def load_csv():
    """Load a CSV file and display its contents."""
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        data = pd.read_csv(file_path)
        for widget in table_frame.winfo_children():
            widget.destroy()
        table = Table(table_frame, dataframe=data, showtoolbar=True, showstatusbar=True)
        table.show()

root = tk.Tk()
root.title("SUU")

root.geometry("1024x600")

header_frame = tk.Frame(root, bg="#990000", height=100)
header_frame.pack(fill=tk.X, side=tk.TOP)

title_label = tk.Label(header_frame, text="Student Analyzer", fg="white", bg="#990000", font=("Helvetica", 24))
title_label.pack(pady=20)

footer_frame = tk.Frame(root, bg="#cc0000", height=50)
footer_frame.pack(fill=tk.X, side=tk.BOTTOM)


user_label = tk.Label(footer_frame, fg="white", bg="#cc0000", font=("Helvetica", 12))
user_label.pack(side=tk.LEFT, padx=10)

upload_button = tk.Button(header_frame, text="Upload CSV", command=load_csv, bg="#0066cc", fg="white", font=("Helvetica", 12), bd=0)
upload_button.pack(pady=10)

table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
