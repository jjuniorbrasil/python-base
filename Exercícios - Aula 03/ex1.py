def somaPrimeiros(n):
    if n<0:
        return 0
    if n == 0 or n == 1:
        return n
    else:
        return n + somaPrimeiros(n-1)
    
x = 3

resultado = somaPrimeiros(x)

print(resultado)