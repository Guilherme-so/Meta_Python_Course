# List e "ARRAY" em Javascript

list1 = [0, 1, 2 ,3 , 4, 5]


list1.append(6)
# precisa do id para adicionanr
list1.insert(len(list1), 7)
list1.extend([8, 9, 10, 11])



# Deleta da lista

list1.pop(0)

del list1[-1]

print(list1)



# Interagir com a lista

for n in list1:
    print(n)


count = 0

while count < len(list1):
    print(list1[count]);
    count += 1
