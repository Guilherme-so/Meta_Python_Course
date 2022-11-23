preços = [100, 200, 300, 400, 500, 1000];

# 10% de juros
def calcularPreco(preco):
  return round(preco * 1.1, 2);

total_preco = list(map(calcularPreco, preços))
print(total_preco)


# def taxa_juros(total, taxa):
#     return (total * taxa ) / 100.00

# print("Taxa de juros: ",  taxa_juros(100, 3))