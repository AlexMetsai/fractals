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


if __name__ == "__main__":

    max_iter_ = 300
    c_ = complex(-0.7269, 0.1889)

    # Set output image resolution.
    img_width = 1920
    img_height = 1080

    # plotting window
    x_leftmost, x_rightmost = -2, 2
    y_bottom, y_top = -1, 1
    plain = np.zeros((img_width, img_height))

    # For every pixel:
    #    - convert coordinates to complex number
    #    - assign a color w.r.t. the number of iterations
    #      returned by the 'mandelbrot_fractal' function.
    #    - draw color to map
    for x in range(img_width):
        for y in range(img_height):
            z_ = complex(x_leftmost + (x / img_width) * (x_rightmost - x_leftmost),
                         y_bottom + (y / img_height) * (y_top - y_bottom))
            iters = julia_set(z_, c_, max_iter_)
            color = iters / max_iter_
            plain[x, y] = color

    # Save the generated image.
    plain = np.rot90(plain)
    plt.imshow(plain, cmap='plasma', interpolation='nearest')
    plt.axis('off')
    plt.savefig("output/julia_c_=_-0.7269_i0.1889.png", bbox_inches='tight', pad_inches=0)
    plt.show()
