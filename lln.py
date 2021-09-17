import numpy
from numpy.lib.nanfunctions import nanargmax
from numpy.random import randn

while True:
    try:
        n = int(input("Specify sample size: "))
        break
    except ValueError:
        print("Please enter an integer")

counter=0
for idx, val in enumerate(randn(n)):
    if abs(val)<1:
        counter+=1
        
ratio=round(counter/n*100,3)

print(f'Out of {n} samples, the values was within +-1 in {ratio}%.')
