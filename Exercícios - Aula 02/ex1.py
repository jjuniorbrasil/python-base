#EX 01 

x = int(input())

if x > 0:
    print('O número é positivo!')
elif x < 0:
    print('O número é negativo!')
else:
    print('O número é "0"')

print('O número é positivo!' if x > 0 else ('O número é negativo!' if x<0 else "'O número é zero!"))