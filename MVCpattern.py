import tkinter

root = tkinter.Tk()

radius_intvar = tkinter.IntVar()
radius_intvar.set(100)  
y_intvar = tkinter.IntVar()
y_intvar.set(0)
x_intvar = tkinter.IntVar()
x_intvar.set(0)
x = 300
y = 300

def radius_changed(new_intval):
    r = radius_intvar.get() 
    xp = x_intvar.get()
    yp = y_intvar.get()
    canvas.coords(circle_item, x-r+xp, y-r+yp, x+r+xp, y+r+yp)


def y_posChange(new_intval):
    yp = y_intvar.get()
    xp = x_intvar.get()
    r = radius_intvar.get()
    canvas.coords(circle_item,x-r+xp,y-r+yp,x+r+xp,y+r+yp)


def x_posChange(new_intval):
    xp = x_intvar.get()
    yp = y_intvar.get()
    r = radius_intvar.get()
    canvas.coords(circle_item, x-r+xp, y-r+yp, x+r+xp, y+r+yp)


radius_slider = tkinter.Scale(root, from_=1, to=150, variable=radius_intvar,
                              label='Radius', command=radius_changed)
radius_slider.grid(row=1, column=0, sticky=tkinter.W)

y_change = tkinter.Scale(root,from_=-150, to=150,label = 'Y-Position',variable = y_intvar, command = y_posChange)
y_change.grid(row=0, column=3, sticky=tkinter.W)

text = tkinter.Label(root, text='Drag slider \nto adjust\ncircle.')
text.grid(row=1, column=3)

x_change = tkinter.Scale(root, from_=-150, to=150,label='X-Position', variable=x_intvar, command=x_posChange)
x_change.grid(row=2, column=3, sticky=tkinter.W)

text = tkinter.Label(root, text='Drag slider \nto adjust\ncircle.')
text.grid(row=0, column=0)

canvas = tkinter.Canvas(root, width=600, height=600, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)

r = radius_intvar.get()
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r,
                                 outline='#000000', fill='#00FFFF')

root.mainloop()
