import sys
import numpy as np
from scipy.io import wavfile

with open('coeffs.txt') as file:
    coeffs = file.readlines()

file = sys.argv[1]

rate, data = wavfile.read(file)
# for i in y:
    # 
# data = y
for  i, sample in enumerate(data):
    product = 0
    sum = 0
    # coeffs = a
    for j, coeff in enumerate(coeffs):
        if i-j < 0:
            # product = 0
            sum += 0
        else:
            product = float(coeff) * data[i-j]
            sum += product

    data[i] += sum
    # data[i] = sum

rate = int(rate/2)

newdata = data[::2]

wavfile.write('newname.wav', rate, newdata.astype(np.int16))