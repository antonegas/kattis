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

def fft_helper(a: list[complex], inverse: bool) -> list[complex]:
    """
    Converts a list of real or complex numbers to or from the frequency domain using fast Fourier transform.

    algorithm: Fast Fourier transform uses divide and conquer to split the problem into equal parts. 
    It uses the fact that a polynomial: A(x) = a_0+a_1x+...+a_(n-1)x^(n-1) = A0(x^2) + x*A1(x^2), where 
    A1(x) = a_0 + a2x + ... + a_(n-2)x^(n/2-1), A2(x) = a_1 + a_3x + ... + a_(n-1)x^(n/2-1). This can then
    be applied down to AN(x) = a_k.
    time complexity: O(n*logn)
    where:
    - n is the number elements in a.
    why:
    - logn from the number of times A(x) can be split in half.
    - n from applying A(x) = A0(x^2) + x*A1(x^2).
    reference: https://cp-algorithms.com/algebra/fft.html#implementation

    parameters:
    - a: a list of coefficients or a frequencies (of length 2^k).
    - inverse: a boolean stating if the function is calculating the inverse ft or not.
    returns:
    - If not the inverse: a list of the frequencies.
    - If the inverse: a list of the coefficients.
    """

    # Base case.
    if len(a) == 1:
        return a
    
    # Split the polynomial a into a0 and a1.
    a0 = fft_helper(a[::2], inverse)
    a1 = fft_helper(a[1::2], inverse)

    # Determine the incrementing angle for the transform.
    angle = 2 * pi / len(a)
    if inverse:
        angle = -angle

    w = complex(1, 0)
    wn = complex(cos(angle), sin(angle))

    result = a

    # Calculate the fourier/inverse fourier transform.
    for a0_i, a1_i, i in zip(a0, a1, range(len(a0))):
        result[i] = a0_i + w * a1_i
        result[i + len(a) // 2] = a0_i - w * a1_i

        if inverse:
            result[i] = result[i] / 2
            result[i + len(a) // 2] = result[i + len(a) // 2] / 2

        w = w * wn

    return result

def polynomial_multiplication(a: list[int], b: list[int]) -> list[int]:
    """
    Multiplies two polynomials using fast Fourier transformation.

    algorithm: Doing polynomial multiplications in naively requires n^2. Doing the same
    thing in the frequency domain requires 2*n operations. Converting to and from the 
    frequency domain can be done using FFT and inverse FFT.
    time complexity: O(n*logn)
    where:
    - n is the number of coefficients in the polynomials.
    why:
    - O(n*logn) from doing FFT and inverse FFT.
    - O(n) from doing multiplications in the frequency domain.
    - O(n*logn+n) = O(n*logn)
    reference: https://cp-algorithms.com/algebra/fft.html#implementation

    parameters:
    - a: a list of integer coefficients in a polynomial given on the form a1 + a2x + ... + anx^n.
    - b: a list of integer coefficients in a polynomial given on the form b1 + b2x + ... + bnx^n.
    returns:
    - The result of multiplying the polynomial a and b given on the same form.
    """

    # The maximum number of coefficients in the resulting polynomial will be the sum of 
    # the number of coefficients. In order to perform FFT on the length of the list needs
    # to be a power of 2.
    n = 1

    while n < len(a) + len(b):
        n = n << 1

    # Both the lists of coefficients are converted to the frequency domain. As before the 
    # length of the lists needs to be a power of 2.
    frequency_domain_a = fft(pad_list(a[:], n))
    frequency_domain_b = fft(pad_list(b[:], n))

    # In the frequency domain |a| + |b| multiplications needs to be performed as compared
    # to |a| * |b| which would be needed when just multiplying the coefficients.
    for i in range(n):
        frequency_domain_a[i] *= frequency_domain_b[i]

    # To get back to the resulting coefficients inverse FFT is used.
    frequency_domain_a = fft_inverse(frequency_domain_a)

    # The resulting coefficients should also be integers.
    return [*map(lambda x: round(x.real), frequency_domain_a)]

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