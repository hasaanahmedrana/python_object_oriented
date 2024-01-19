import tkinter as tk
from tkinter import ttk, messagebox

class CGPACalculator(tk.Tk):
    def _init_(self):
        super()._init_()

        self.title("CGPA Calculator")

        self.courses = []
        self.courses.append(('OOP', 3))
        self.courses.append(('OOP Lab', 1))
        self.courses.append(('English', 2))
        self.courses.append(('IST', 2))

        full_window_frame = ttk.Frame(self)
        full_window_frame.grid(row=0, column=0, padx=10, pady=10)

        self.course_name_label = ttk.Label(full_window_frame, text="Course Name")
        self.course_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.course_name_var = tk.StringVar()
        self.course_name_entry = ttk.Entry(full_window_frame, width=50)
        self.course_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.course_name_entry["textvariable"] = self.course_name_var

        self.credit_hours_label = ttk.Label(full_window_frame, text="Credit Hours")
        self.credit_hours_label.grid(row=1, column=0, padx=10, pady=10)

        self.credit_hours_var = tk.IntVar()
        self.credit_hours_entry = ttk.Entry(full_window_frame, justify="right", width=20)
        self.credit_hours_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.credit_hours_entry["textvariable"] = self.credit_hours_var

        self.percent_marks_label = ttk.Label(full_window_frame, text="Percentage Marks")
        self.percent_marks_label.grid(row=2, column=0, padx=10, pady=10)

        self.percent_marks_var = tk.IntVar()
        self.percent_marks_entry = ttk.Entry(full_window_frame, justify="right", width=20)
        self.percent_marks_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.percent_marks_entry["textvariable"] = self.percent_marks_var

        self.calculate_cgpa_button = ttk.Button(full_window_frame, text="Calculate CGPA")
        self.calculate_cgpa_button.grid(row=3, column=0, padx=10, pady=10)
        self.calculate_cgpa_button.bind('<Button-1>', self.calculate_cgpa)

    def calculate_cgpa(self, event):
        total_credit_hours = sum(course[1] for course in self.courses)
        weighted_sum = sum(course[1] * self.percent_marks_var.get() / 100 for course in self.courses)
        cgpa = weighted_sum / total_credit_hours

        messagebox.showinfo(title="CGPA Calculation", message=f"CGPA: {cgpa:.2f}")

def main():
    CGPACalculator().mainloop()

main()