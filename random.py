#random number
import random
random.seed(1)
for i in range(5):
    print('{:04.3f}'.format(random.uniform(1, 100)), end=' ')
print()

x=[[i] for i in range(0, 144)]
print(x)
