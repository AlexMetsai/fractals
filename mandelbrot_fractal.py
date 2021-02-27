from PIL import Image, ImageDraw

max_iter = 80

def mandelbrot_fractal(c):
    z, n = 0, 0
    while abs(z) <=2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

if __name__ == "__main__":
    
    # Set output image resolution.
    img_width  = 1920
    img_height = 1080
    
    # plotting window
    x_leftmost, x_rightmost = -2, 2
    y_top, y_bottom         = -1, 1
    
    # Create image.
    img  = Image.new("RGB", (img_width, img_height), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # For every pixel, assign a color w.r.t. the number of iterations
    # returned by the 'mandelbrot_fractal' function.
    for x in range(img_width):
        for y in range(img_height):
    
    # cast pixel values to complex number
    # TODO
    
    # Assign a color with respect to the number 
    # of iterations that 'mandelbrot_fractal' returns.
    # TODO
    
    # Save to image
