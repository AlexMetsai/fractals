"""
Copyright (C) 2021 Alexandros I. Metsai
alexmetsai@gmail.com

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 3
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from PIL import Image, ImageDraw


def mandelbrot_fractal(c, max_iter):
    z, n = 0, 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n


if __name__ == "__main__":

    max_iter_ = 80

    # Set output image resolution.
    img_width = 1920
    img_height = 1080

    # plotting window
    x_leftmost, x_rightmost = -2, 2
    y_bottom, y_top = -1, 1

    # Create image.
    img = Image.new("RGB", (img_width, img_height), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    # For every pixel:
    #    - convert coordinates to complex number
    #    - assign a color w.r.t. the number of iterations
    #      returned by the 'mandelbrot_fractal' function.
    #    - draw color to map
    for x in range(img_width):
        for y in range(img_height):
            c_ = complex(x_leftmost + (x / img_width) * (x_rightmost - x_leftmost),
                         y_bottom + (y / img_height) * (y_top - y_bottom))
            iters = mandelbrot_fractal(c_, max_iter_)
            color = 255 - int(iters * 255 / max_iter_)
            draw.point([x, y], (color, color, color))

    # Save the generated image.
    img.save("mandelbrot_fractal.png", "PNG")
