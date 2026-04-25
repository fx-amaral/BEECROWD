
def maior(x,y):
    m = (x+y+abs(x-y))//2
    return m

valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
print(f'{maior(maior(a,b),c)} eh o maior')


