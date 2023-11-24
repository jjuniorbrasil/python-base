import math

def calculaLog(x, b):
    return math.log(x, b)

n = 2
b = 10

print('Log de \'' + str(n) + '\' na base \'' + str(b) + '\': ' + str(calculaLog(n, b)))