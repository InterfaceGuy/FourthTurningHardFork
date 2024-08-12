from manim import *
import numpy as np
from scipy.special import factorial

RED = "#FF644E"
BLUE = "#00a2ff"

class TaylorSeries(Scene):
    def construct(self):
        # Set the range for the x-axis
        x_range = (-12, 12)

        # Define the custom function
        def custom_function(x):
            return np.sin(2 * (x + 0)) * np.exp(2 * (x + 0) / 10) / 3

        # Function to compute nth derivative using finite differences
        def nth_derivative(func, x, n, dx=1e-5):
            if n == 0:
                return func(x)
            x_points = np.linspace(x - dx, x + dx, n + 1)
            y_points = func(x_points)
            for _ in range(n):
                y_points = np.gradient(y_points, x_points)
            return y_points[-1]

        # Define the function for the Taylor expansion
        def taylor_expansion(x, n, a=0):
            x_eval = np.full_like(x, a)
            summation = np.zeros_like(x)
            for i in range(n + 1):
                derivative = nth_derivative(custom_function, a, i)
                term = derivative * (x - a)**i / factorial(i)
                summation += term
            return summation

        # Create axes
        axes = Axes(
            x_range=x_range,
            y_range=(-2, 2),
            x_length=12,
            y_length=6,
            tips=False,
            axis_config={"include_ticks": False},
        )

        # Plot the custom function curve
        custom_curve = axes.plot(custom_function, color=RED)
        taylor_curve = axes.plot(lambda x: taylor_expansion(x, 10), color=BLUE)

        # Animate the plots
        self.add(axes, custom_curve, taylor_curve)
        self.wait(2)