import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import pandas as pd

# Initialize the Tkinter application
root = tk.Tk()
root.title("Data Cleaning and Preprocessing Tool")
root.geometry("800x600")

# Global variable for DataFrame
data = None

# Function to upload a file
def upload_file():
    global data
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    
    if file_path:
        try:
            if file_path.endswith('.csv'):
                data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                data = pd.read_excel(file_path)

            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, data.head().to_string())

            messagebox.showinfo("Success", "File uploaded successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")

# Function to remove missing data
def handle_missing_data():
    global data
    if data is not None:
        data.dropna(inplace=True)
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, data.head().to_string())
        messagebox.showinfo("Success", "Missing data removed!")
    else:
        messagebox.showwarning("No Data", "Please upload a file first.")

# Function to fill missing data
def fill_missing_data():
    global data
    if data is not None:
        fill_value = simpledialog.askstring("Input", "Enter value to fill missing data:")
        if fill_value is not None:
            data.fillna(fill_value, inplace=True)
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, data.head().to_string())
            display_data()
            messagebox.showinfo("Success", "Missing data filled!")
    else:
        messagebox.showwarning("No Data", "Please upload a file first.")

#Function to display data in a table
def display_data():
    if data is not None:
        # Clear the existing table
        for widget in frame.winfo_children():
            widget.destroy()

        # Create a treeview widget
        tree = ttk.Treeview(frame)
        tree["columns"] = list(data.columns)
        tree["show"] = "headings"

        # Set column headings
        for col in data.columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=120)

        # Insert data into the table
        for i, row in data.iterrows():
            tree.insert("", "end", values=list(row))

        tree.pack(fill="both", expand=True)
# Function to remove duplicate rows
def remove_duplicates():
    global data
    if data is not None:
        data.drop_duplicates(inplace=True)
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, data.head().to_string())
        messagebox.showinfo("Success", "Duplicates removed!")
    else:
        messagebox.showwarning("No Data", "Please upload a file first.")

# Function to rename a column
def rename_column():
    global data
    if data is not None:
        old_name = simpledialog.askstring("Input", "Enter column name to rename:")
        new_name = simpledialog.askstring("Input", "Enter new column name:")
        if old_name in data.columns and new_name:
            data.rename(columns={old_name: new_name}, inplace=True)
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, data.head().to_string())
            messagebox.showinfo("Success", "Column renamed!")
        else:
            messagebox.showwarning("Invalid Input", "Column name not found or invalid input.")
    else:
        messagebox.showwarning("No Data", "Please upload a file first.")

# Function to export cleaned data
def export_data():
    global data
    if data is not None:
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
        if save_path:
            try:
                if save_path.endswith('.csv'):
                    data.to_csv(save_path, index=False)
                elif save_path.endswith('.xlsx'):
                    data.to_excel(save_path, index=False)
                messagebox.showinfo("Success", f"Data exported successfully to {save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")
    else:
        messagebox.showwarning("No Data", "Please upload a file first.")

# Creating buttons for user actions
upload_button = tk.Button(root, text="Upload Data", command=upload_file)
upload_button.pack(pady=10)

text_output = tk.Text(root, height=15, width=80)
text_output.pack(pady=10)

missing_data_button = tk.Button(root, text="Remove Missing Data", command=handle_missing_data)
missing_data_button.pack(pady=5)

fill_missing_button = tk.Button(root, text="Fill Missing Data", command=fill_missing_data)
fill_missing_button.pack(pady=5)

remove_duplicates_button = tk.Button(root, text="Remove Duplicates", command=remove_duplicates)
remove_duplicates_button.pack(pady=5)

rename_column_button = tk.Button(root, text="Rename Column", command=rename_column)
rename_column_button.pack(pady=5)

export_button = tk.Button(root, text="Export Cleaned Data", command=export_data)
export_button.pack(pady=10)

# Run the application
root.mainloop()
