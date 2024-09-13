import random

tam = int(input('escolha o tamanho da senha: '))
senha = ''
for i in range(tam):
    caracteres = str(random.randint(0,9))
    senha+=(caracteres)

print(senha)
