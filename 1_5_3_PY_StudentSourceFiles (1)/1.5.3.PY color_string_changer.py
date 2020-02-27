#####
# color_string_changer.py
# 
# Creates two Scales and a Text view. Updates Text based on the Scales
# 
# (c) 2013 PLtW
# version 11/1/2013
####

import tkinter # Often people import tkinter as *

#####
# Create root window 
####
root = tkinter.Tk()
root.wm_title('Hexadecimal Explorer')

#####
# Create Model
######
# Create two IntVar's and initialize them to 127
red_intvar = tkinter.IntVar() 
red_intvar.set(127) 
green_intvar = tkinter.IntVar()
green_intvar.set(127)

######
# Create Controller
#######
# Event handler for slider
def color_changed(new_intval):
    # Controller updates the view by pulling data from model
    editor.insert(tkinter.END, '#' + \
                               hexstring(red_intvar) + \
                               hexstring(green_intvar) + '00\n')
    editor.see(tkinter.END) # scroll the Text window to see the new bottom line
            
# Instantiate and place sliders
red_slider = tkinter.Scale(root, from_=0, to=255, variable=red_intvar, 
                           orient=tkinter.HORIZONTAL,   
                           label='Red', command=color_changed)
red_slider.grid(row=1, column=0, sticky=tkinter.E)
green_slider = tkinter.Scale(root, from_=0, to=255, variable=green_intvar,  
                             orient=tkinter.HORIZONTAL,
                             label='Green', command=color_changed)
green_slider.grid(row=2, column=0, sticky=tkinter.E)
# Create and place directions for the user
Text = tkinter.Label(root, Text='Drag slider \nto adjust\ncolor code.')
Text.grid(row=0, column=0)

######
# Create View
#######
# Create a Text editor window for displaying information
editor = tkinter.Text(root, width=10)
editor.grid(column=1, row=0, rowspan=3)

######
# Function to convert IntVar data from Scale widget to two hex digits as string
# for a Canvas widget color argument
#######

def hexstring(slider_intvar):
    '''A function to prepare data from controller's widget for view's consumption
    
    slider_intvar is an IntVar between 0 and 255, inclusive
    hexstring() returns a 2-character string representing a value in hexadecimal
    '''
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

#######
# Event Loop
#######
root.mainloop()