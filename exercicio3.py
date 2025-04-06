#Exercício 3: Filtragem de Logs por Severidade
#Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 
# 'ERROR'. Dado um registro de log em formato de dicionário como 
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
print(log)
verdade = 'ERROR' in log


if log['level'] == 'ERROR':
    message = "Nível ALTO de severidade"
else:
    message = "Nível BAIXO de severidade"

print(message)