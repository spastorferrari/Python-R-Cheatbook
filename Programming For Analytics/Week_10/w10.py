import os
os.chdir('C:\\Users\\Sebastian Pasotr\\Documents\\Data_Coding\\Python Root\\Week_10')

file = open('newfile.txt', 'w')
file.write('Hello world in the new file \n')
file.write('and another line \n')
file.close()

# We can run terminal commands in python by using !terminalcommand
!more newfile.txt

# we cannot read a file unless we specify 'r'
file = open('newfile.txt', 'r')
# read() works like a cursor
myfilecontents = file.read() # reads everything in the file
myfilecontents1 = file.readlines() # reads [] since you're at the end of file
myfilecontents1
file.close()

# with statements allow you to nest entire operation and closes file automatically
with open('w10test.txt', 'w') as file:
    file.write('This is what you can do with a: \n')
    file.write('WITH STATEMENT.')
