from PIL import Image, ImageDraw

max_iter = 80

def mandelbrot_fractal(c):
    z, n = 0, 0
    while abs(z) <=2 and n < max_iter:
        z = z*z + c
        n += 1
    return n
