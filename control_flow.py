total_conta = 200

disconto1 = 10
disconto2 = 20

if total_conta >= 100 and total_conta < 200:
    print("valor total e maior que 100, tem disconto de 10$")
    total_conta -= disconto1

elif total_conta >= 200:
    print('valor total e maior que 200, tem disconto de 20$')
    total_conta -= disconto2 

else:
    print("Total da conta e menor que 100, sem disconto!") 

print("Total da conta: " + str(total_conta))

