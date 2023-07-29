# Project Euler, Problem 9: Special Pythagorean Triplet
# There exists exactly one Pythagorean triplet for which a+b+c=1000. Find the product abc.
import math


# takes in possible Pythagorean triplet a, b, c
def is_pythagorean_triple(a, b, c):
    if a ** 2 + b ** 2 == c ** 2 and b.is_integer() and a.is_integer() and c.is_integer():
        # True if all values are integers and the equality a^2+b^2=c^2 holds, otherwise false
        return True
    else:
        return False


# starts a at 1
a = float(1)
# computes b based on a and the fact that a+b+c=1000
b = (1000 ** 2 - 2000 * a) / (2000 - 2 * a)
# computes c based on a and b
c = math.sqrt(a ** 2 + b ** 2)

while not is_pythagorean_triple(a, b, c):
    a += 1
    # iterates a whenever a, b, c is not a Pythagorean triple and then re-computes both b and c
    b = (1000 ** 2 - 2000 * a) / (2000 - 2 * a)
    c = math.sqrt(a ** 2 + b ** 2)

# Prints the following when a, b, c is a Pythagorean triple
print("The only Pythagorean triple for which a+b+c=1000 is a=", int(a), ", b=", int(b), ", c=", int(c))
print("The product abc=", int(a * b * c))
