# Exemplo de arquivo.
# 100 linhas , cada linha um numero

arquivo = open('arquivo.txt','w')
for linha in range(1,101):
    arquivo.write(f'{linha}\n')
arquivo.close()

# arquivo = open('arquivo.txt','r')
# for linha in arquivo.readlines():
#     print(linha)
# arquivo.close()

with open('pares.txt','w') as pares, open('impares.txt','w') as impares:
    for n in range(0,1000):
        if n % 2 == 0:
            pares.write(f'{n} é par\n')
        else:
            impares.write(f'{n} é impar\n')
