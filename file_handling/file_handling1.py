    # mode = "r" Read Only (‘r’) : Open text file for reading. default mode
    # mode = "r+" Read and Write (‘r+’): Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exist.
    # mode = "w" Write Only (‘w’) : Open the file for writing. For the existing files, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exist.
    # mode = "w+" Write and Read (‘w+’) : Open the file for reading and writing. For an existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.
    # mode = "a" Append Only (‘a’): Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
    # mode = "a+" Append and Read (‘a+’) : Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.


# with open('file_handling/newfile.txt', 'w') as file:
    # \n significa new line, vai pra linha de baixo
    # file.writelines(['\nThis is a new file.', "\n this is a new line"])

# with open('file_handling/newfile.txt', 'a') as file:
    # file.writelines(['\nThis is a new file.', "\n this is a new line"])


try:
    with open('file_handling/newfile.txt', 'a') as file:
        file.writelines(['\nThis is a new file.', "\n this is a new line"])
except FileNotFoundError as err:
    print("Error: ", err)