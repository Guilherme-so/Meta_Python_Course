cliente_leal = True
total_conta = 124


if cliente_leal and total_conta > 100:
    #da 20% disconto
    total_conta -= (float(total_conta)/ 100) * 20
    print("Desconto de 20 porcento aplicado")

elif total_conta > 100:
    #da 10% disconto
    total_conta  -= (float(total_conta)/ 100) * 10
    print("Desconto de 10 porcento aplicado")

else:
    #Opps. Sem disconto.
    print('Sorry, no discount ...')

print('Total Conta: ', float(total_conta))