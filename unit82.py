# November 1, 2016
# GUIs drawing prigram
# This drawing program will allow a user to select one of three shapes: a square, a circle, or a triangle

import Tkinter

def draw_shape(_=None):
    '''
    This function draws the corresponding shape with given position on the canvas
    :param _: Avoid error
    :return: Nothing
    '''
    global drawing

    # Get the xy position from the sliders
    x_scale = change_x.get()
    y_scale = change_y.get()

    # Draw a square
    if shape_selection.get() == 'Square':
        shape.delete(drawing)
        drawing = shape.create_rectangle(150 + x_scale, 150 + y_scale, 350 + x_scale, 350 + y_scale)

    # Draw a circle
    if shape_selection.get() == 'Circle':
        shape.delete(drawing)
        drawing = shape.create_oval(150 + x_scale, 150 + y_scale, 350 + x_scale, 350 + y_scale)

    # Draw a triangle
    if shape_selection.get() == 'Triangle':
        shape.delete(drawing)
        drawing = shape.create_polygon(150 + x_scale, 350 + y_scale, 250 + x_scale, 150 + y_scale, 350 + x_scale, 350 + y_scale, fill='white', outline='black')

# Set up tkinter window
root = Tkinter.Tk()
root.title('Draw Shapes')

# Title of the program
title_label = Tkinter.Label(root, text='Draw Shapes', font='Times 30 bold')
title_label.grid(row=1, column=1, columnspan=3)

# Label for shape selection
shape_selection_label = Tkinter.Label(root, text='Select a shape to draw:')
shape_selection_label.grid(row=2, column=1, columnspan=2)

# Shape selection radiobuttons
shape_selection = Tkinter.StringVar()

# Initiate the canvas
shape = Tkinter.Canvas(root, width=500, height=500)
shape.grid(row=4, column=1, columnspan=2)

# Establish the first drawing, the drawing variable
drawing = shape.create_text(250, 250,text='Please select a shape')

# Frame for radiobuttons
radiobutton_frame = Tkinter.Frame(root)
radiobutton_frame.grid(row=3, column=1, columnspan=2)

# Radiobutton for square
shape_square = Tkinter.Radiobutton(radiobutton_frame, text='Square', variable=shape_selection, value='Square', command=draw_shape)
shape_square.grid(row=1, column=1)

# Radiobutton for circle
shape_circle = Tkinter.Radiobutton(radiobutton_frame, text='Circle', variable=shape_selection, value='Circle', command=draw_shape)
shape_circle.grid(row=1, column=2)

# Radiobutton for triangle
shape_triangle = Tkinter.Radiobutton(radiobutton_frame, text='Triangle', variable=shape_selection, value='Triangle', command=draw_shape)
shape_triangle.grid(row=1, column=3)

# Slider for x position
change_x = Tkinter.Scale(root, from_=-125, to=125, orient='horizontal', command=draw_shape)
change_x.grid(row=5, column=2, sticky='W', padx=5)
# Label
change_x_label = Tkinter.Label(root, text='Move horizontally')
change_x_label.grid(row=5, column=1, sticky='E', padx=5)

# Frame for y position slider
change_y_frame = Tkinter.Frame(root)
change_y_frame.grid(row=4, column=3)

# Label
change_y_label = Tkinter.Label(change_y_frame, text='Move vertically')
change_y_label.grid(row=1, column=1, sticky='S')

# Slider for y position
change_y = Tkinter.Scale(change_y_frame, from_=-125, to=125, orient='vertical', command=draw_shape)
change_y.grid(row=2, column=1, sticky='N')

root.mainloop()



