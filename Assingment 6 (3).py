from tkinter import *
from PIL import ImageTk  # require pillow for jpeg images
window = Tk()
window.title("Login Page.")
window.geometry("996x560+70+50")
window.resizable(False, False)

#setting background image
bgimage = ImageTk.PhotoImage(file='bg2.jpg')
bglabel = Label(window, image=bgimage)
bglabel.place(x=0, y=0)

#adding header
header = Label(window, text='LOGIN INFO')
header.config(font=("Helvetica", 30, 'bold'), bg="#C72928",fg='white')
header.place(x=120, y=60)
#line below header
frame1 = Frame(window, width=450, height=2, bg="white")
frame1.place(x=50, y=130)

#USERNAME
username_label = Label(window, text='Username:')
username_label.config(font=("Helvetica", 12, 'bold'),bg="#C72928",fg='white')
username_label.place(x=100, y=170)
username_entry = Entry(window, width=20, font=("Helvetica", 11),fg='black')
username_entry.place(x=200, y=170)
#placeholder
username_entry.insert(0, "Enter Username")
#delete placeholder on click
username_entry.bind("<Button-1>", lambda event: username_entry.delete(0, END))

#PASSWORD
pass_label = Label(window, text='Password:')
pass_label.config(font=("Helvetica", 12, 'bold'),bg="#C72928",fg='white')
pass_label.place(x=100, y=210)
pass_entry = Entry(window, width=20, font=("Helvetica", 11),fg='black')
pass_entry.place(x=200, y=210)
#placeholder
pass_entry.insert(0, "Enter Password")
#delete placeholder on click
pass_entry.bind("<Button-1>", lambda event: pass_entry.delete(0, END))
#CLOSE
window.mainloop()
