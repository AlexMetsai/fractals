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
    
    # For every pixel:
    #    - convert coordinates to complex number
    #    - assign a color w.r.t. the number of iterations
    #      returned by the 'mandelbrot_fractal' function.
    #    - draw color to map
    for x in range(img_width):
        for y in range(img_height):
            c = complex(re_start + (x/img_width)*(re_end - re_start),
                        img_start + (y/img_height)*(img_end - img_start))
            iters = mandelbrot_fractal(c)
            color = 255 - int(iters*255/max_iter)
            draw.point([x,y], (color, color, color))
    
    # Save the generated image.
    img.save("mandelbrot_fractal.png", "PNG")
