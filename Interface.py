import tkinter as tk
import numpy as np

def create_bitstring_interface():
    # Define the size of the canvas and the pixel size
    canvas_width = 280
    canvas_height = 280
    pixel_size = 10

    # Create a 28x28 matrix of zeros to represent the image
    image_matrix = np.zeros((28, 28))

    # Define the function to draw a pixel
    def draw_pixel(event):
        x, y = event.x, event.y
        x_pixel = x // pixel_size
        y_pixel = y // pixel_size
        image_matrix[x_pixel][y_pixel] = 1
        canvas.create_rectangle(x_pixel * pixel_size, y_pixel * pixel_size,
                                 (x_pixel + 1) * pixel_size, (y_pixel + 1) * pixel_size,
                                 fill='black')

    # Define the function to convert the image to a bit string
    def convert_to_bit_string():
        bit_string = ''
        for i in range(28):
            for j in range(28):
                bit_string += str(int(image_matrix[j][i]))
        return bit_string

    # Create the GUI window and canvas
    root = tk.Tk()
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, background='white')
    canvas.pack()

    # Bind the mouse click event to the draw_pixel function
    canvas.bind("<B1-Motion>", draw_pixel)

    # Add a button to convert the image to a bit string and close the window
    button = tk.Button(root, text="Convert to Bit String", command=lambda: (root.destroy()))
    button.pack()

    root.mainloop()

    return convert_to_bit_string()


