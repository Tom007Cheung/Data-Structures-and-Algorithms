import math

def karatsuba(num1, num2):
    """
    The Karatsuba algorithm was the first multiplication algorithm
asymptotically faster than the quadratic "grade school" algorithm.
The Toom–Cook algorithm is a faster generalization of Karatsuba's
method, and the Schönhage–Strassen algorithm is even faster,
for sufficiently large n.
    """

    if (num1 < 10) or (num2 < 10):
        return num1 * num2
    # calculates the size of the numbers
    m = max(num1, num2)
    m2 = math.floor(m/2)

    # split the digit sequences in the middle
    #   high1, low1 = str.split(num1, m2)
    #   high2, low2 = str.split(num2, m2)
    high1 = num1[:m2]
    low1 = num1[m2:]
    high2 = num2[:m2]
    low2 = num2[m2:]

    # calls made to numbers approximately half the size
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    return z2 * math.pow(10, m2*2) + ((z1 - z2 - z0) * math.pow(10, m2)) + z0

print(karatsuba(12345, 6789))