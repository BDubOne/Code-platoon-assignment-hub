import os

Cwd = os.getcwd() # get current working directory -- dir code
print(Cwd)

abs_path = os.path.abspath('./notes.txt')

print(abs_path)  ###find absolute path to designate file

with open(abs_path, 'r') as file:
    for line in file:
        print(line)