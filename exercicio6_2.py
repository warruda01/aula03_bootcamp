#frase = str(input('Digite uma frase --> ')).strip().upper()
frase = 'O dia está dia bonito'
palavras = frase.split()
contagem_palavras = {} #Criando um dicionário

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1
    
print(contagem_palavras)


# print(frase_separada)
# cont = 0
# for i in range(0,len(frase_separada)):
#     for j in range(0, len(frase_separada)):
#         if frase_separada[i] == frase_separada[j]:
#             cont +=1
#     print("{} - aparece {} vezes.".format(frase_separada[i],cont))
