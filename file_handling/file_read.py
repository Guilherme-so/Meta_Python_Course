# file.read ler todo o arquivo
with open('file_handling/newfile.txt', mode= 'r') as file:
    file =  file.read()
    # print(file)


# file.readline ler so a primeira linha do arquivo
with open('file_handling/newfile.txt', mode= 'r') as file:
    readline =  file.readline()
    # print(readline)

# file.readlines e uma list "ARRAY" em Javascript!
with open('file_handling/newfile.txt', mode= 'r') as file:
    readlines =  file.readlines()
    # print(readline)    
    # for lines in readlines:
        # print(lines)


# tambem da pra passar parametro de quantas letras quer
with open('file_handling/newfile.txt', mode= 'r') as file:
    readline =  file.readline(10)
    print(readline)
