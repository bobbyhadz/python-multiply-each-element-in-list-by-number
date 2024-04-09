# Multiply each element in a list by a number in Python

# ✅ Multiply each element in a list by a number
import math

my_list = [2, 4, 6]

result = [item * 10 for item in my_list]
print(result)  # 👉️ [20, 40, 60]

# ------------------------------------------

# ✅ Multiply all elements in a list

my_list = [2, 4, 6]

result = math.prod(my_list)
print(result)  # 👉️ 48