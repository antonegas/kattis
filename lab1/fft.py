"""
author: Anton Nilsson
testcase 1:
in:
1
2
1 0 5
1
0 -2

out:
3
0 -2 0 -10

"""

from math import pi, cos, sin, log

def pad_list(a: list[int], length: int = -1) -> list[int]:
    """
    Adds right padded zeros to a list.
    """
    if length == -1:
        length = len(a)
    if len(a) == 1:
        return a
    return a + [0] * (2**(int(log(length - 1)/log(2)) + 1) - len(a))

def strip_list(a: list[int]):
    """
    Removes right padded zeros in a list.
    """
    for i in reversed(range(len(a))):
        if a[i] != 0:
            return a[:i + 1]
    return []

def fft_helper(coefficients: list[complex], inverse: bool) -> list[complex]:
    """
    Converts a list of real or complex numbers to or from the frequency domain using fast Fourier transform.

    algorithm: XXX
    time complexity: O(n*logn)
    where:
    - n is the number coefficients.
    why:
    - XXX
    reference: https://cp-algorithms.com/algebra/fft.html#implementation

    parameters:
    - coefficients: a list of coefficients or a frequencies.
    - inverse: a boolean stating if the function is calculating the inverse ft or not.
    returns:
    - 
    """

    if len(coefficients) == 1:
        return coefficients
    
    a0 = fft_helper(coefficients[::2], inverse)
    a1 = fft_helper(coefficients[1::2], inverse)

    angle = 2 * pi / len(coefficients)
    if inverse:
        angle = -angle

    w = complex(1, 0)
    wn = complex(cos(angle), sin(angle))

    result = coefficients

    for a0_i, a1_i, i in zip(a0, a1, range(len(a0))):
        result[i] = a0_i + w * a1_i
        result[i + len(coefficients) // 2] = a0_i - w * a1_i

        if inverse:
            result[i] = result[i] / 2
            result[i + len(coefficients) // 2] = result[i + len(coefficients) // 2] / 2

        w = w * wn

    return result

def polynomial_multiplication(a: list[int], b: list[int]) -> list[int]:
    """
    Multiplies two polynomials using fast Fourier transformation.

    algorithm: XXX
    time complexity: O(n*logn)
    where:
    - n is the number of coefficients in the polynomials.
    why:
    - XXX
    reference: https://cp-algorithms.com/algebra/fft.html#implementation

    parameters:
    - a: a list of coefficients in a polynomial given on the form a1 + a2x + ... + anx^n.
    - b: a list of coefficients in a polynomial given on the form b1 + b2x + ... + bnx^n.
    returns:
    - The result of multiplying the polynomial a and b given on the same form.
    """

    fa = a[:]
    fb = b[:]
    n = 1

    while n < len(fb) + len(fa):
        n = n << 1

    fa = pad_list(fa, n)
    fb = pad_list(fb, n)

    fa = fft(fa)
    fb = fft(fb)

    for i in range(n):
        fa[i] *= fb[i]

    fa = fft_inverse(fa)

    return [*map(lambda x: round(x.real), fa)]

def fft(coefficients: list[int]) -> list[complex]:
    """
    Calculates the Fourier transform of a list of coefficients.
    """
    return fft_helper([*map(lambda x: complex(x, 0), pad_list(coefficients))], False)

def fft_inverse(coefficients: list[complex]) -> list[complex]:
    """
    Calculates the inverse Fourier transform of a list of frequencies.
    """
    return [*map(lambda x: complex(x.real, 0), fft_helper(coefficients, True))]

if __name__ == "__main__":
    output = list()
    data = open(0, "r").read()

    first_polynomial = [*map(int, data.split("\n")[2].split(" "))]
    second_polynomial = [*map(int, data.split("\n")[4].split(" "))]

    multiplied_polynomial = strip_list(polynomial_multiplication(first_polynomial, second_polynomial))

    output.append(str(len(multiplied_polynomial) - 1))
    output.append(" ".join(map(str, multiplied_polynomial)))

    open(1, "w").write("\n".join(output))