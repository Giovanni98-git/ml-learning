import math, statistics, random, os, glob

print(math.cos(math.pi))
print(math.exp(5))

random.seed(0)
print(random.choice(['jean','anne','julie']))

print(random.sample(range(100),10))
0
liste = [i for i in range(10)]
random.shuffle(liste)
print(liste)

print(os.getcwd())
d = {}
filenames = glob.glob("*.py")
for file in filenames:
    with open(file, 'r') as f:
        d[file] = f.read().splitlines()
print(d)