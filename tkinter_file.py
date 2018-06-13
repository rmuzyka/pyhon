import ttk
from Tkinter import Tk
from ttk import *
from Tkinter import *
from PIL import Image, ImageTk

# root = Tk()
# ttk.Button(root, text='Hi!').grid()
# root.mainloop()


def calculate(*args):
    x = 0.762/2 if is_child.get() == 'yes' else 0.762
    x = x * shoes_dict[str(shoes_type.get())]
    try:
        value = float(steps.get())
        if sex.get() == 'male':
            meters.set(value * x)
        if sex.get() == 'female':
            meters.set(value * x * 0.75)
    except ValueError:
        pass


root = Tk()
root.title('Steps to Meters')

mainframe = ttk.Frame(root, padding="3 3 12 12", borderwidth=10, relief='raised')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

steps = StringVar()
meters = StringVar()
is_child = StringVar()
sex = StringVar()
username = StringVar()
shoes_type = StringVar()

# >>> print type(meters)
# <type 'instance'>

check = ttk.Checkbutton(mainframe, text='Child steps',
                        command=calculate,
                        variable=is_child,
                        onvalue='yes', offvalue='no').grid(column=2, row=5)

male = ttk.Radiobutton(mainframe, text='Male', command=calculate, variable=sex, value='male').grid(row=4, sticky=W)
female = ttk.Radiobutton(mainframe, text='Female', command=calculate, variable=sex, value='female').grid(row=5, sticky=W)

name_entry = ttk.Entry(mainframe, textvariable=username, width=10).grid(column=1, row=0, sticky=W)
steps_entry = ttk.Entry(mainframe, width=2, textvariable=steps)
steps_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
button = ttk.Button(mainframe, text='Calculate', command=calculate).grid(column=3, row=3, sticky=W)
# print is_child.get()
# print check.instate(['alternate'])

ttk.Label(mainframe, text='Your name').grid(column=0, row=0, sticky=E)
ttk.Label(mainframe, text='steps').grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text='is equivalent to').grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text='meters').grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text=('Dear %s, your' % username.get())).grid(column=1, row=1, sticky=E)

shoes = ttk.Combobox(mainframe, textvariable=shoes_type)
shoes.bind(('<<ComboxSelected>>', calculate))
shoes['values'] = ('sneakers', 'high heels', 'sandals', 'flip-flops', 'trainers', 'male elegant')
shoes_dict = {'sneakers': 1, 'high heels': 0.5, 'sandals': 0.7, 'flip-flops': 0.6, 'trainers': 0.9, 'male elegant': 0.8}
print shoes_type.get()

#   DISPLAYING IMAGES
# image = ImageTk.PhotoImage(Image.open('images.gif'))
# ttk.Label(mainframe, image=image).grid(column=0)
# img = Image.open('images.gif')
# print img.size


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

steps_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()