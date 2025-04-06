#Exercício 4: Validação de Dados de Entrada
#Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições e imprima 
# "Dados de usuário válidos" ou o erro específico encontrado.

idade = int(input("Digite a idade do usuário -->"))

if idade < 18 or idade > 65:
    message = 'Idade Inválida. Deve ser entre 18 e 65 anos'
else:
    email = input("Digite o e-mail --> ")
    valida_email1 = '@' in email
    valida_email2 = '.' in email    
    if valida_email1 == True and valida_email2 == True:
        message = 'Dados do usuário Válidos'
    else:
        message = 'Email inválido'
print (message)