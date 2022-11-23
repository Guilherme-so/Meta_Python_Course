    # mode = "r" Read Only (‘r’) : Open text file for reading. default mode
    # mode = "r+" Read and Write (‘r+’): Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exist.
    # mode = "w" Write Only (‘w’) : Open the file for writing. For the existing files, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exist.
    # mode = "w+" Write and Read (‘w+’) : Open the file for reading and writing. For an existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.
    # mode = "a" Append Only (‘a’): Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
    # mode = "a+" Append and Read (‘a+’) : Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.



# file = open('file_handling/test.txt', mode = 'r')

# data = file.readline()
# print(data)
# file.close()

# melhor porque fecha sozinho
with open("file_handling/test.txt", mode= 'r') as file:
    data = file.readline()
    print(data)