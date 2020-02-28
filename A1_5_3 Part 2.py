import tkinter 
root = tkinter.Tk()

radius_intvar = tkinter.IntVar()
radius_intvar.set(100)
green_intvar = tkinter.IntVar()
green_intvar.set(0)
red_intvar = tkinter.IntVar()
red_intvar.set(0)
x = 150
y = 150
# Event handler for slider
def radius_changed(new_intval):
    # Get data from model 
    # Could do this: r = int(new_intval)
    r = radius_intvar.get()
    # Controller updating the view 
    canvas.coords(circle_item, x-r, y-r, x+r, y+r)
# Instantiate and place slider 
radius_slider = tkinter.Scale(root, from_=1, to=15, label="Radius", command = radius_changed)

radius_slider.grid(row=1, column=0, sticky=w)
# Create and place directions for the user 
text = tkinter.Label(root, text='Drag slider \n to adjust \n circle.')
text.grid(row=0, column=0)
# Create and place a canvas 
canvas = tkinter.Canvas(root, width=300, heaigh=300, background="#FFFFFF")
canvas.grid(row=0, rowspan=2, column=1)

# Create a circle on the canvas to match the initial model 
r = radius_intvar.get()                        
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, outline="#000000", fill="#00FFFF")


green_slider = tkinter.Scale(root, from_=0, to = 255, variable = green_intvar, orient = tkinter.HORIZONTAL, label='Green', command=color_changed)
green_slider.grid(row = 2, column = 0, sticky=tkinter)

# Create a text editor window for displaying information
editor = Tkinter.Text(root, width=10)
editor.grid(column=1, row=0, rowspan=3)
#####
# Function to convert IntVar data to two hex digits as string 
# for a Canvas widget color argument 
##### 

def hexstring(slider_intvar): 

    # Get an integer from an IntVar 
    slider_int = slider_intvar.get()
    # Convert to hex 
    slider_hex = hex(slider_int)
    # Drop the 0x at the beginning of the hex string 
    slider_hex_digits = slider_hex[2:]
    # Ensure two digits of hexadecimal: 
    if len(slider_hex_digits)==1:
        slider_hex_digits = '0' + slider_hex_digits 
        return slider_hex_digits  
#####
# Event Loop
#####
root.mainloop()


    
