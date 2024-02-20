import tkinter as tk
from tkinter import filedialog
import csv
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to handle file selection button click
def on_button_click():
    file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv")])
    if file_path:
        label.config(text="Selected file: " + file_path)

        # Enable the button to list unique values
        button_list_home_states.config(state=tk.NORMAL)
        # Disable the button to plot the bar chart until unique values are listed
        button_plot_bar_chart.config(state=tk.DISABLED)

# Function to list all unique values in the "HOME_STATE" column
def list_unique_home_states():
    file_path = label.cget("text").replace("Selected file: ", "")
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)  # Get the header row

            if "HOME_STATE" in header:
                home_state_index = header.index("HOME_STATE")
                home_states = [row[home_state_index] for row in csv_reader if len(row) > home_state_index]

                # Enable the button to plot the bar chart
                button_plot_bar_chart.config(state=tk.NORMAL)
            else:
                label_search_result.config(text="Column 'HOME_STATE' not found in the CSV file.")
                # Disable the button to plot the bar chart if 'HOME_STATE' column is not found
                button_plot_bar_chart.config(state=tk.DISABLED)
    except Exception as e:
        label_search_result.config(text="Error: " + str(e))
        # Disable the button to plot the bar chart in case of an error
        button_plot_bar_chart.config(state=tk.DISABLED)

# Function to handle bar chart button click
def on_bar_chart_button_click():
    file_path = label.cget("text").replace("Selected file: ", "")
    home_states = get_home_states(file_path)

    # Calculate frequency using Counter
    frequencies = Counter(home_states)

    # Plot the bar chart with vertical state names
    fig, ax = plt.subplots()
    bars = ax.bar(frequencies.keys(), frequencies.values(), color='skyblue')

    # Set labels and title
    ax.set_xlabel('HOME_STATE')
    ax.set_ylabel('Frequency')
    ax.set_title('Bar Chart of HOME_STATE Frequencies')

    # Display the bar chart in the Tkinter window with a vertical scrollbar
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Add vertical scrollbar
    scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=canvas.get_tk_widget().yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.get_tk_widget().configure(yscrollcommand=scrollbar.set)

    # Rotate x-axis tick labels vertically
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=90, ha="center")

# Function to get the home states from the CSV file
def get_home_states(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Get the header row
        home_state_index = header.index("HOME_STATE")
        home_states = [row[home_state_index] for row in csv_reader if len(row) > home_state_index]
    return home_states

# Create the main window
window = tk.Tk()
window.title("Heat Map Prototype")

# Create a button to select a CSV file
button_select_file = tk.Button(window, text="Select CSV File", command=on_button_click)
button_select_file.pack()

# Create a label to display the selected file path
label = tk.Label(window, text="No file selected")
label.pack()

# Create a button to list unique values in the HOME_STATE column
button_list_home_states = tk.Button(window, text="List Unique HOME_STATE", command=list_unique_home_states, state=tk.DISABLED)
button_list_home_states.pack()

# Create a label to display the search result
label_search_result = tk.Label(window, text="")
label_search_result.pack()

# Create a button to plot the bar chart
button_plot_bar_chart = tk.Button(window, text="Plot Bar Chart", command=on_bar_chart_button_click, state=tk.DISABLED)
button_plot_bar_chart.pack()

# Start the GUI event loop
window.mainloop()















