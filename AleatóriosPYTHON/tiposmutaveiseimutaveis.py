#Imutabilidade com int
print('Int imutável')
x = 10
print(f"Endereço inicial do x: {id(x)}")

x = x + 1
print(f"Endereço do x após mudar para 11: {id(x)}")


#Mutabilidade com list
print('list mutável')

minha_lista = [1, 2, 3]
print(f"Endereço inicial da lista {minha_lista}: {id(minha_lista)}")

# Adicionando um elemento (modificando a lista)
minha_lista.append(4)
print(f"Endereço da lista após o append {minha_lista}: {id(minha_lista)}")