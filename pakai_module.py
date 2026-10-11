import math
import datetime as dt

try:
    import random
except ModuleNotFoundError:
    random = None

print(math.sqrt(16))
print(math.pi)
if random is not None:
    print(random.randint(1, 6))
print(dt.date.today().year)