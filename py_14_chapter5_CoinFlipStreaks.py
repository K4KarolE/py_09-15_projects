

import random


max_range = 100
counterTT = 0


for q in range(10000):
    counterH = 0
    value_list = []
    for i in range(0, max_range):
            value = random.randint(0,1)
            value_list.append(value)

    for p in range(max_range-6):
        if value_list[p] == value_list[p + 1] == value_list[p + 2] == value_list[p + 3] == value_list[p + 4] == value_list[p + 5] == value_list[p + 6]:
            counterTT +=1       
        
# what is a streak count? is it a duplicate when the streak is more than 6 digit long?        


print()
print(counterTT)

