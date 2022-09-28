

import random

value_list = []
max_range = 100
counter = 0

for i in range(0, max_range):
    value = random.randint(0,1)
    value_list.append(value)


for p in range(0, max_range-6):
    if value_list[p] == value_list[p + 1] == value_list[p + 2] == value_list[p + 3] == value_list[p + 4] == value_list[p + 5] == value_list[p + 6]:
        counter = 1


print()
print(value_list)
print(counter)

