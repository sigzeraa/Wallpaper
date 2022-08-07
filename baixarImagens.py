import random
#Generate 5 random numbers between 10 and 30

for i in range(30):
    randomlist = random.sample(range(0, 14), 10)
    print(randomlist)
    with open('readme.txt', 'w') as f:
        f.write(randomlist)