# Visualizing fractals

A repository for visualizing fractals with python and various plotting libraries and methods. Under development.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


Implemented the visualization of a julia set, aside from the mandelbrot fractal. 
Below you can see one for *c = -0.7269 + j 0.1889*. 
It is encouraged to experiment with different parameters of *c* to witness on first hand the 
chaotic nature of these sets.

Additionally, I experimented with different (and hopefully better) visualization than the one used previously,
utilizing matplotlib. Of course, there's always room for improvement.

![mandelbrot](https://github.com/AlexMetsai/fractals/blob/main/output/julia_c_=_-0.7269_i0.1889_small.png?raw=true)

Another fractal from the julia sets is shown below, for *c = -0.4 + j 0.6*.
![mandelbrot](https://github.com/AlexMetsai/fractals/blob/main/output/julia_c_=_-0.4_i0.6.png?raw=true)

Below you can see a mandelbrot fractal, that was generated using the PIL module for visualization; this is the first 
visualization method implemented in this repo.

![mandelbrot](https://github.com/AlexMetsai/fractals/blob/main/output/mandelbrot_fractal_960_540.png?raw=true)


Planning to 
- [X] Planning to add more fractals aside from the mandelbrot one. PM me if I'm lazy.
- [ ] Experiment with even better visualization and add a few more sets. PM me if I'm lazy.
- [X] Improve performance with list comprehension (improvement is marginal, need to try something else).
- [ ] Improve performance with Cython. I'm not gonna promise anything about this. :-)

## Main dependencies:

- Python 3.6
- PIL 8.1.0
- matplotlib 3.3.4
