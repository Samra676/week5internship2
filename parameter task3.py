 # Task 1:Write a function `calculate_area` that takes radius and returns area of a circle.

import math

def calculate_area(radius):
    return math.pi * radius * radius

# Function ko call karna aur output print karna
radius = 5  # yahan koi bhi number de sakte hain
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
