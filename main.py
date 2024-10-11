# Import necessary librabies
from tkinter import *

# Setting up Main window
root = Tk()
root.geometry("400x300")
root.title("main")

#Functio to open New (Top level) window
def topwin():
    # Setting up Top window
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    # Adding a label widget to Top window
    l2 = Label(top, text="This is toplevel window")
    l2.pack()

    top.mainloop()


# Adding a label and buttton widget to root (Main) window
l = Label(root, text="This is main window")
btn = Button(root, text="Click here eto open another window", command=topwin)

# Arranging widgets
l.pack()
btn.pack()

root.mainloop()