# EX 01

print('Digite seu nome: ')
print('Saudações, ' + input() + '.\n')

# EX 02

print('Insira sua idade: ')
print('Idade em dias: ' + str(int(input()) * 365) + '.')

# EX 03

print('\nDigite dois números: ')
x = int(input())
y = int(input())

print('\nAdição: ' + str(x + y))
print('Subtração: ' + str(x - y))
print('Multiplicação: ' + str(x * y))
print('Divisão: ' + str(x / y))

# EX 04

print('\nDigite um número: ')
x = int(input())

if (x % 2 == 0): print(str(x) + ' é par.')
else: print(str(x) + ' é ímpar.')

# EX 05

print('\nInforme a temperatura (ºC): ')
t = float(input())
print('A temperatura em Fahrenheit (ºF) é: ' + str((t * 1.8) + 32))

# EX 06

print('Informe o tamanho em metros: ')
m = float(input())
print('Valor em centímetros: ' + str(m * 100))

# EX 07

print('\nDigite dois números: ')
x = int(input())
y = int(input())
print(float(x / y))

# EX 08

print('\nInforme a altura do retângulo: ')
a = float(input())
print('Informe a largura do retângulo: ')
l = float(input())
print('Área do retângulo: ' + str(a * l) + ' u.a.')

# EX 09

print('\nDigite um número: ')
x = int(input())

if (x > 0): print(str(x) + ' é positivo.')
elif (x < 0): print(str(x) + ' é negativo.')
else: print('O número informado é zero.')

# EX 10

print('\nInforme o raio do círculo: ')
r = int(input())

print('Área do círculo: ' + str(3.14 * r**2))
print('Perímetro do círculo: ' + str(2 * r * 3.14))

# EX 11

print('\nInforme o valor em dólar: ')
d = int(input())

print('Valor em Euro: ' + str(d * 0.85))

# EX 12

print('\nInforme, em sequência, os lados (A, B e C) do triângulo: ')

a = float(input())
b = float(input())
c = float(input())
s = (a + b + c) / 2

import math

a = math.sqrt(s * (s - a) * (s - b) * (s - c))

print('Área do triângulo: ' + str(a) + ' u.a.')

# EX 13

print('\nDigite um número: ')
x = int(input())

# EX 14/15

print('\nDigite um número: ')
x = int(input())
