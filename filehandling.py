# File is used to store data permanently in memory.
# operations on file:
# 1 open a file.
# 2 read and write a file.
# 3 close a file.

# File Modes:
# 1 r: open a file for reading. (default mode)
# 2 w: open a file for writing. (overwrites the file if it exists)
# 3 a: open a file for appending. (creates a new file .if it does not exist)
# 4 rb: open a file for reading in binary mode.
# 5 wb: open a file for writing in binary mode.
# 6 ab: open a file for appending in binary mode.
# 7 r+: open a file for both reading and writing.
# 8 w+: open a file for both reading and writing. (overwrites the file if it exists)
# 9 a+: open a file for both reading and appending. (creates a new file if it does not exist)
# 10 x: open a file for exclusive creation. (fails if the file already exists)


# Example:open a file for reading.
# file = open ('example.txt','r')  
# print(file.read())
# file.close()

# Example:open a file for writing.
# file = open ('example.txt','w')
# file.write('Hello World')
# file.close()

# Example:open a file for appending.
# file = open ('example.txt','a')
# file.write('Hello World')
# file.closed()


