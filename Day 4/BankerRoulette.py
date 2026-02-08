import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1

random_friends = random.choice(friends)
print(random_friends)

# option 2
print(friends[random.randint(0,4)])
