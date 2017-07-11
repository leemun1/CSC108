import math
type(math)

math.sqrt(9)
math.pi

radius = 5
print('area is', math.pi * radius ** 2)

from math import sqrt, pi # creates functions in current namespace
sqrt(9)

# restoring a module
import math
math.pi = 3
math.pi

import imp
math = imp.reload(math)
math.pi