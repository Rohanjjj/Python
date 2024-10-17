import tkinter as tk
from tkinter import messagebox
def browse_input_file(self):
        file_path = filedialog.askopenfilename(title="Select Input File")
        if file_path:
            self.input_file_var.set(file_path)

def browse_output_file(self):
    file_path = filedialog.asksaveasfilename(title="Select Output File")
    if file_path:
        self.output_file_var.set(file_path)