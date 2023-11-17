#EX 06

f1 = 1
f2 = 2
c = 2

print('Termos Fibonacci (1-10)')
print('Termo 1: ' + str(f1))
print('Termo 2: ' + str(f2))

while c < 10:
    f3 = f2 + f1
    f1 = f2
    f2 = f3
    c += 1
    print('Termo ' + str(c) + ': ' + str(f3))
