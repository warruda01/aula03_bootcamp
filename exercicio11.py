#Leitura de Dados até Flag
#Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") 
# seja fornecida.
entrada = str(input("Digite a palavra -->")).strip().upper()

while entrada != "SAIR":
    entrada = str(input("Digite a palavra -->")).strip().upper()
