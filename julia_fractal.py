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

max_iter = 100


def julia_fractal(z, c):
    """
    Fractals arising from julia sets can be obtained in a similar manner to mandelbrot fractals,
    by keeping 'c' constant and letting 'z' be a value of the complex plain.

    :param z:
    :param c:
    :return n: number of iterations
    """
    n = 0
    while abs(z) <=2 and n < max_iter:
        z = z*z + c
        n += 1
    return n
