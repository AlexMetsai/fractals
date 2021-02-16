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
    
    # cast pixel values to complex number
    # TODO
    
    # Assign a color with respect to the number 
    # of iterations that 'mandelbrot_fractal' returns.
    # TODO
    
    # Save to image
