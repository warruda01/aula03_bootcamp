#6. Contagem de Palavras em Textos

#Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto_usuario = str(input('Digite um texto --> ')).strip().upper()
texto = texto_usuario.split()
quant = len(texto)



for i in range (0, len(texto)):
    cont = 0
    for j in range(0,len(texto)):
        if texto[i] == texto[j]:
            cont += 1
    print("{} - Aparece {} vezes".format(texto[i], cont))