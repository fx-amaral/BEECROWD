medidas = input().split()
a = float(medidas[0])
b = float(medidas[1])
c = float(medidas[2])
pi = 3.14159

print(f'TRIANGULO: {(a*c)/2:.3f}')
print(f'CIRCULO: {pi*c**2:.3f}')
print(f'TRAPEZIO: {((a+b)*c)/2:.3f}')
print(f'QUADRADO: {b*b:.3f}')
print(f'RETANGULO: {a*b:.3f}')