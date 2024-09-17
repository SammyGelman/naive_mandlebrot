import numpy as np 
import random
import math

def gen_random_complex():
    # radius of the circle
    circle_r = 2

    # random angle
    alpha = 2 * math.pi * random.random()
    
    # random radius
    r = circle_r * math.sqrt(random.random())
    
    # calculating coordinates
    x = r * math.cos(alpha)
    y = r * math.sin(alpha)

    return complex(x, y)


def f(z, c):
    return z**2 + c

num_iterations = 150

set_size = 10000000

exploded = []
stability = []

    
for val in range(set_size):
    c = gen_random_complex()
    z = 0
    stability_index = 0

    flag = True

    for i in range(num_iterations):
        if flag:
            z = f(z, c)
            stability_index += 1

            if np.sqrt(z**2) >= 2:
                flag = False
                exploded.append(c)
                stability.append(stability_index)
                
#%% Plotting 
import matplotlib.pyplot as plt

# Extract real and imaginary parts from the complex numbers
real_parts = [z.real for z in exploded]
imaginary_parts = [z.imag for z in exploded]

# Create the scatter plot
plt.figure(figsize=(6,6), dpi=2000)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Use scatter plot with colors based on stability values
scatter = plt.scatter(real_parts, imaginary_parts, c=stability, cmap='viridis', s=.004, edgecolors='none')

# Add a colorbar to show the mapping of stability to colors
plt.colorbar(scatter, label='Stability')

# Set limits for better visualization (you can adjust based on your data)
plt.xlim(min(real_parts) - 1, max(real_parts) + 1)
plt.ylim(min(imaginary_parts) - 1, max(imaginary_parts) + 1)

# Labels and title
plt.xlabel('Real')
plt.ylabel('Im')
plt.title('Mandelbrot Set')

plt.grid(True)
plt.show()




