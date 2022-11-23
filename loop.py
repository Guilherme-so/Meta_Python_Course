favoritas = ["Pudin", "Açai", "Sorvete", "Torta", "Mousse", "Brigadeiro"]


# FOR LOOP

# for sobremesa in favoritas:
#     print("Uma das minhas sobremesa favorita e: " + sobremesa )

# PARA PEGA O ID
# for idx, sobremesa in enumerate(favoritas):
#     print(idx, "Uma das minhas sobremesa favorita e: " + sobremesa)

# PARA SELECIONAR UMA COISA DENTRO DO LOOP
for sobremesa in favoritas:
    if sobremesa == "Pudin":
        print("Sim " + sobremesa + " e minha sobremesa favorita!")
        break
else:
    print("Minha sobremesa favorita nao ta na lista")

# CONTAGEM
# for eachNumber in range(11):
#     print(eachNumber)


# ___________________________________________________________________________________


# WHILE LOOP


# count = 0

# while count < len(favoritas):
#     print(count, "Uma das minhas sobremesa favorita e: " + favoritas[count])
#     count += 1


# contagem while loop

# count = 0

# while count < 20:
#     print(count)
#     count += 1



# contagem regressiva while loop

# count = 20

# while count > 0:
#     print(count)
#     count -= 1