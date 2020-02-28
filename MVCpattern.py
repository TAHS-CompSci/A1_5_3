import tkinter

root = tkinter.Tk()

red_intvar = tkinter.IntVar()
red_intvar.set(127)
green_intvar = tkinter.IntVar()
green_intvar.set(127)
blue_intvar = tkinter.IntVar()
blue_intvar.set(127)
radius_intvar = tkinter.IntVar()
radius_intvar.set(100)  
y_intvar = tkinter.IntVar()
y_intvar.set(0)
x_intvar = tkinter.IntVar()
x_intvar.set(0)
x = 300
y = 300
shapes = []

def color_changed(new_intval):
    tk_color_string = color(red_intvar, green_intvar, blue_intvar)
    editor.insert(tkinter.END, tk_color_string + '\n')
    editor.see(tkinter.END)
    canvas.itemconfigure(circle_item,fill = tk_color_string)


def hexstring(slider_intvar):
    slider_int = slider_intvar.get()
    slider_hex = hex(slider_int)
    slider_hex_digits = slider_hex[2:]
    if len(slider_hex_digits) == 1:
        slider_hex_digits = '0' + slider_hex_digits
    return slider_hex_digits


def color(r, g, b):
    rx = hexstring(r)
    gx = hexstring(g)
    bx = hexstring(b)
    return '#'+rx+gx+bx

def shape_changed(new_intval):
    r = radius_intvar.get() 
    xp = x_intvar.get()
    yp = y_intvar.get()
    canvas.coords(circle_item, x-r+xp, y-r+yp, x+r+xp, y+r+yp)


radius_slider = tkinter.Scale(root, from_=1, to=150, variable=radius_intvar,
                              label='Radius', command=shape_changed)
radius_slider.grid(row=1, column=0, sticky=tkinter.W)

y_change = tkinter.Scale(root,from_=-150, to=150,label = 'Y-Position',variable = y_intvar, command = shape_changed)
y_change.grid(row=0, column=0, sticky=tkinter.W)

x_change = tkinter.Scale(root, from_=-150, to=150,label='X-Position', variable=x_intvar, command=shape_changed)
x_change.grid(row=2, column=0, sticky=tkinter.W)

red_slider = tkinter.Scale(root, from_=0, to=255, variable=red_intvar,
                           orient=tkinter.HORIZONTAL,
                           label='Red', command=color_changed)
red_slider.grid(row=0, column=2, sticky=tkinter.E)
green_slider = tkinter.Scale(root, from_=0, to=255, variable=green_intvar,
                             orient=tkinter.HORIZONTAL,
                             label='Green', command=color_changed)
green_slider.grid(row=1, column=2, sticky=tkinter.E)
blue_slider = tkinter.Scale(root, from_=0, to=255, variable=blue_intvar,
                            orient=tkinter.HORIZONTAL,
                            label='Blue', command=color_changed)
blue_slider.grid(row=2, column=2, sticky=tkinter.E)

canvas = tkinter.Canvas(root, width=600, height=600, background='#000000')
canvas.grid(row=0, rowspan=3, column=4)

editor = tkinter.Text(root, width=10)
editor.grid(column=5, row=0, rowspan=3)

r = radius_intvar.get()
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r,
                                 outline='#000000', fill='#00FFFF')

startx, starty = 300, 300

def down(event):  
    global startx, starty  
    startx = event.x  
    starty = event.y


def up(event):
    tk_color_string = color(red_intvar, green_intvar, blue_intvar)
    r = (startx-event.x)**2 + (starty-event.y)**2  
    r = int(r**.5)
    new_shape = canvas.create_rectangle(
        x-r, y-r, x+r, y+r, outline=tk_color_string)
    shapes.append(new_shape)  

canvas.bind('<Button-1>', down)
canvas.bind('<ButtonRelease-1>', up)


root.mainloop()
