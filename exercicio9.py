#Extração de Subconjuntos de Dados
#Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

primeiro_numero = int(input("digite o primeiro numero do intervalo --> "))
ultimo_numero = int(input("digite o último numero do intervalo --> "))
numeros = range(primeiro_numero,ultimo_numero)
pares = [x for x in numeros if x % 2 == 0]

print(pares)