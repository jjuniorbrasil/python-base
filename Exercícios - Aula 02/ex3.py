#EX 03

print('Informe um número: ')

x = int(input())

print('=========== TABUADA DO ' + str(x) + ' ===========')

for multi in range(1, 11):
    print(str(x) + " x " + str(multi) + " = " + str(x*multi))