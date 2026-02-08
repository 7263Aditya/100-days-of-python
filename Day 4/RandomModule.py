import random
import my_module
print(random.randint(1,10))

# Module
print(my_module.fav_num)

# generating random floating point number
print(random.random()*10)

print(random.uniform(1,10))

res = random.randint(0,1)
if res == 1:
    print("Heads.")
else:
    print("Tails.")