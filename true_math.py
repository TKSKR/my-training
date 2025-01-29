import math
def divide(first, second):
    if second == 0:
        return math.inf
    return first / second
print(divide(56, 8))
print(divide(234, 0))