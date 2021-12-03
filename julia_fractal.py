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

import numpy as np
import matplotlib.pyplot as plt
import time


def julia_set(z, c, max_iter):
    """
    Fractals arising from julia sets can be obtained in a similar manner to mandelbrot fractals,
    by keeping 'c' constant and letting 'z' be a value of the complex plain.

    :param z:
    :param c:
    :param max_iter:
    :return n: number of iterations
    """
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n


def draw_julia_set(img_width, img_height, formula, c, loopy_way=True):
    """
    For every pixel:
       - convert coordinates to complex number
       - assign a color w.r.t. the number of iterations
         returned by the 'julia_set' function.
       - draw color to map

    :param img_width:
    :param img_height:
    :param formula: The formula determining if a point belong to a julia set.
    :param c:
    :param loopy_way: Use a plain double loop or a list comprehension for the second dimension. The second way is more
                      efficient for large resolutions but also less readable.
    :return n: number of iterations
    """

    # Plotting window
    x_leftmost, x_rightmost = -2, 2
    y_bottom, y_top = -1, 1
    plain = np.zeros((img_width, img_height))

    start = time.time()

    # Draw
    if loopy_way:
        for x in range(img_width):
            for y in range(img_height):
                z_ = complex(x_leftmost + (x / img_width) * (x_rightmost - x_leftmost),
                             y_bottom + (y / img_height) * (y_top - y_bottom))
                iters = formula(z_, c, max_iter_)
                color = iters / max_iter_
                plain[x, y] = color
    else:
        for x in range(img_width):
            zeds = [complex(x_leftmost + (x / img_width) * (x_rightmost - x_leftmost),
                            y_bottom + (y / img_height) * (y_top - y_bottom)) for y in range(img_height)]
            plain[x] = [julia_set(z_, c_, max_iter_) / max_iter_ for z_ in zeds]

    print(f"Time taken to calculate the fractal{time.time() - start}")

    return plain


if __name__ == "__main__":

    # Set maximum number of iterations and the parameter 'c'.
    max_iter_ = 300
    c_ = complex(-0.7269, 0.1889)

    # Set image resolution.
    img_width_ = 1920
    img_height_ = 1080

    # Draw the set
    plain_ = draw_julia_set(img_width_, img_height_, formula=julia_set, c=c_)

    # Save the generated image.
    plain_ = np.rot90(plain_)
    plt.imshow(plain_, cmap='plasma', interpolation='nearest')
    plt.axis('off')
    plt.savefig(f"output/julia_c_=_{c_.real}_i{c_.imag}.png", bbox_inches='tight', pad_inches=0, dpi=500)
    plt.show()
