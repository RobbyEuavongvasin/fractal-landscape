import noise
import numpy as np
from PIL import Image
import random

# Define the size of the image
width = 800
height = 800

# Create a numpy array to hold the fractal data
fractal = np.zeros((height, width))

# Define the properties of the fractal
octaves = 8
persistence = 0.5
lacunarity = 2.0
scale = 100.0

# Generate the fractal
for y in range(height):
    for x in range(width):
        fractal[y][x] = noise.pnoise2(x / scale, y / scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)

# Normalize the fractal data
fractal = (fractal + 1) / 2

# Generate a random color map
color_map = np.zeros((256, 3))
for i in range(256):
    color_map[i] = [random.random(), random.random(), random.random()]

# Create an image from the fractal data
image = Image.fromarray((fractal * 255).astype(np.uint8))
image.putpalette(color_map.ravel())
image = image.convert("P")

# Save the image
image.save("fractal_landscape.png")
