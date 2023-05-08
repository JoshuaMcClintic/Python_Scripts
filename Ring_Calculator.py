# This python script will calculate the area of a ring, or the outer portion of a double circle, using a formula
# I created after noticing a similarity between the area formulas for circles and triangles. A guide to how I got
# there should also be on my GitHub. The formula assumes that the only given values are the circumferences of the
# two circles that make up the ring. ((C_Large^2) - (C_Small^2)) / (4π)

import math

c_large = float(input("Enter the circumference of the larger circle: "))

c_small = float(input("Enter the circumference of the smaller circle: "))

ring_area = ((c_large**2) - (c_small**2)) / (4 * math.pi)

print(f"The are of the ring is {ring_area}.")