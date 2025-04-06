#Exercício 5: Detecção de Anomalias em Dados de Transações
#Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas.
# Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário 
# comercial (antes das 9h ou depois das 18h). Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, 
# verifique se ela é suspeita.

transacao = {'valor': 12000, 'hora': 20}

if transacao['valor'] > 10000 or not (transacao['hora'] >=9 and transacao['hora'] <=18):
    message = "Transação suspeita"
else:
    message = "transação normal"
print(message)