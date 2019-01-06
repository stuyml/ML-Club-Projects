import math
import random

slope = 2.813853
yint = 4.6

f = open("train.csv", "w")
f.write("x,y\n")
for i in range(1000):
    #random.gauss(mu, sigma)
    x = random.gauss(12, 6)
    y = slope * x + yint + random.gauss(0,2)
    f.write(str(x)+","+str(y)+"\n")


f = open("test.csv", "w")
f.write("x,y\n")
for i in range(200):
    #random.gauss(mu, sigma)
    x = random.gauss(12, 6)
    y = slope * x + yint + random.gauss(0,2)
    f.write(str(x)+","+str(y)+"\n")
