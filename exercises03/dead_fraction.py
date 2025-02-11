"""
author: Anton Nilsson
testcase 1:
in:
0.2...
0.20...
0.474612399...
0

out:
2/9
1/5
1186531/2500000

testcase 2:
in:
0.83636...
0.12344...
0.3789789...
0.9...
0.3...
0.512512...
0.748181...
0.1111...
0.314...
0.009...
0.003...
0

out:
46/55
1111/9000
631/1665
1/1
1/3
512/999
823/1100
1/9
283/900
1/100
1/300

"""

from math import gcd

def dead_fraction(number: str) -> str:
    decimals = number[2:-3]

    simplest_numerator = float("inf")
    simplest_denominator = float("inf")

    for i in range(1, len(decimals) + 1):
        numerator = int(decimals) - int(f"0{decimals}"[:-i])
        denominator = 10**(len(decimals)) - 10**(len(decimals) - i)
        common_divisor = gcd(numerator, denominator)
        
        if simplest_denominator > denominator // common_divisor:
            simplest_denominator = denominator // common_divisor
            simplest_numerator = numerator // common_divisor
    
    return f"{simplest_numerator}/{simplest_denominator}"

if __name__ == "__main__":
    output = list()
    data = open(0, "r").read()
    numbers = data.split("\n")[:-2]

    for number in numbers:
        output.append(dead_fraction(number))

    open(1, "w").write("\n".join(output))