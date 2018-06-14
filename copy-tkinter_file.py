import ttk
from Tkinter import Tk
from ttk import *
from Tkinter import *
from PIL import Image, ImageTk

# root = Tk()
# ttk.Button(root, text='Hi!').grid()
# root.mainloop()




root = Tk()
root.title('Steps to Meters')

mainframe = ttk.Frame(root, padding="3 3 12 12", borderwidth=10, relief='raised')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

onevar = BooleanVar()
twovar = BooleanVar()
onevar.set(True)
twovar.set(False)
one = ttk.Checkbutton(mainframe, text='one', variable=onevar, onvalue=True)
two = ttk.Checkbutton(mainframe, text='two', variable=twovar, onvalue=True)



steps = StringVar()
meters = StringVar()
is_child = StringVar()
sex = StringVar()
username = StringVar()
shoes_type = StringVar()

# >>> print type(meters)
# <type 'instance'>




canvas = Canvas(mainframe)
canvas.create_line(10,10,200,50)

last_x, last_y = 0, 0


def xy(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y


def add_line(event):
    global last_x, last_y
    canvas.create_line((last_x, last_y, event.x, event.y))
    last_x, last_y = event.x, event.y
    
# def set_color


canvas.columnconfigure(0, weight=1)
canvas.rowconfigure(0, weight=1)

# canvas = Canvas(mainframe)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", add_line)


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)



root.mainloop()