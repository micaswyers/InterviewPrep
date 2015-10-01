
import math
def math_test(x):
    if math.sqrt(x) == 1 or math.sqrt(x) % 1 == 0 or math.sqrt(x) < 1:
            yield x
    l = range(int(math.sqrt(x)))
    for item in l:
        factors = []
        factors.append(item)
        factors.extend((math_test(x-(item**2))))
        yield factors