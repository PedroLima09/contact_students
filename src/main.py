import customtkinter as ctk
from tkinter import messagebox
from student.sender import Student

def send_data():
    """
    It takes all the values from the interface widgets, checks that the name is not empty and checks the phone number is valid.
    """
    student_name = name_entry.get()
    student_number = number_entry.get()
    selected_time = time_combo.get()
    selected_reason = reason_combo.get()
    st = Student(student_name, student_number, selected_time, selected_reason)
    if not student_name:
        messagebox.showerror("Error", "Please enter the student's name.")
        return
    if len(student_number) != 11:
        messagebox.showerror("Error", "The student number must have 11 digits.")
        return

    st.send_message()
    
    
    # Show the Sucess Alert 
    messagebox.showinfo("Success", "Data sent successfully!")

    
app = ctk.CTk()
app._set_appearance_mode("dark")
app.geometry("500x650")
app.title("App")

# Title
title_label = ctk.CTkLabel(app, text="Contact Students", font=("Arial", 24))
title_label.pack(pady=20)

# Student name
name_label = ctk.CTkLabel(app, text="Student Name:")
name_label.pack(pady=10)
name_entry = ctk.CTkEntry(app)
name_entry.pack(pady=10, padx=20, fill="x")

# Student number
number_label = ctk.CTkLabel(app, text="Student Phone Number:")
number_label.pack(pady=10)
number_entry = ctk.CTkEntry(app)
number_entry.pack(pady=10, padx=20, fill="x")

# Time selector
time_label = ctk.CTkLabel(app, text="Select Time:")
time_label.pack(pady=10)
times = [f"{i:02d}:00 as {i+1:02d}:00" for i in range(7, 22)] 
time_combo = ctk.CTkComboBox(app, values=times)
time_combo.pack(pady=10, padx=20, fill="x")

# Reason selector
reason_label = ctk.CTkLabel(app, text="Reason:")
reason_label.pack(pady=10)
reasons = ["Replacement", "Tutoring", "Undeclared"]
reason_combo = ctk.CTkComboBox(app, values=reasons)
reason_combo.pack(pady=10, padx=20, fill="x")

# Send button
send_button = ctk.CTkButton(app, text="Send", command=send_data)
send_button.pack(pady=20)

# Copyright label
copyright_label = ctk.CTkLabel(app, text="© Pedro Lima")
copyright_label.pack(side="bottom", padx=10, pady=10)

app.mainloop()
 



    
