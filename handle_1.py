"""
# append mode:
    - it is used to create a file + add lines at the end of file
    - it does not perform truncate operation and overwrite operation
    - it is a writable mode
-----------------------------------------------------------

f = open('c.txt', 'a')
print(f.writable())
# it is used to create file + add contents at the end of file
# add some contents
f.write('This is append mode.\n')
f.write('We can add contents at the end.')
f.write('\nI am not perform truncate operation.')
==============================================================

# exclusive mode:
    - Rule: if file is not present then create a new file
    - but if file already present then throw an exception 'FileExistsError'
    - this is used to create a file only ones
    - it is a writable mode
--------------------------------------------------------------------

# create a new file d.txt with x mode
f = open('d.txt', 'x')
print(f.writable())
f.write('This is a exclusive mode.\n')
f.write('This is used to create a file only ones.')
------------------------------------------------------------------

# Another file extension is binary file img, audio, video
-----------------------------------------------------------------

# Lets try to read an image file from desktop
f = open('C:\\Users\\chava\\OneDrive\\Desktop\\image\\s.jpeg', 'rb')
# rb means read in binary mode
print(f.read())
------------------------------------------------------------------

f = open('C:\\Users\\chava\\OneDrive\\Desktop\\image\\ml_flow.jpeg', 'rb')
print(f.read())
-------------------------------------------------------------------

# Lets try to write an image file from desktop
f = open('C:\\Users\\chava\\OneDrive\\Desktop\\image\\s.jpeg', 'rb')
data = f.read()
f2 = open('C:\\Users\\chava\\OneDrive\\Desktop\\image\\s.jpg', 'wb')
# wb write in binary
f2.write(data)
--------------------------------------------------------------------

# Que. Read a text file and write contents to other files
# add the IFSC of data into i.txt
f = open('trans.txt')
f2 = open('i.txt', 'w', newline='\n')
data = f.readlines()
for i in data:
    f2.writelines(i.split(',')[1])
------------------------------------------------------------------

# lets create a new empty file
open('e.txt', 'w')
------------------------------------------------------------------

f = open('e.txt')
print(f.read())
-------------------------------------------------------------------

# find out mobile number present in the e.txt
f = open('e.txt')
for i in f.read():
    if i.isdigit():
        print(i, end= '')
---------------------------------------------------------

f = open('e.txt')
print(f.read().find('7'))
f.seek(42)
print(f.read())
-----------------------------------------------------------

f = open('e.txt')
print(f.read().split(':')[-1])
========================================================

# Read f.txt, it contains numbers
f = open('f.txt')
print(f.read())
----------------------------------------------

# it number contains the list of string
f = open('f.txt')
print(f.read())
print(f.read().split(','))
---------------------------------------------------

# check the number type
f = open('f.txt')
print(f)
data = f.read().split(',')
print(data)
for i in data:
    print(type(i))
--------------------------------------------------------

# read those numbers, display addition + average
f = open('f.txt')
print(f)
total = 0
data = f.read().split(',')
print(data)
for i in data:
    print(type(i))
    # default data type is str we need to typecast
    total += int(i)
print('all number addition is: ', total)
print('all number average is: ', total/len(data))
=================================================================

# Display Name and Age from g.txt
f = open('g.txt')
print(f.read())
--------------------------------------------------

f = open('g.txt')
data = f.readlines()
print(data)
---------------------------------------------------

f = open('g.txt')
data = f.readlines()
for i in data:
    print(i.split(',')[:2])
----------------------------------------------------

# now add Name and age data into h.txt
f = open('g.txt')
f2 = open('h.txt', 'w')
data = f.readlines()
for i in data:
    f2.writelines(i.split(',')[:2])
    f2.write('\n')
================================================================

f = open('C:\\Users\\chava\\OneDrive\\Desktop\\trans.txt')
print(f)
print(f.read())
=====================================================================

f2 = open('C:\\Users\\chava\\OneDrive\\Desktop\\trans2.txt', 'w')
f2.write('account number of state bank of india is: 3426785413.\n')
f2.write('account number of bank of india is: 1100005413.\n')
f2.write('account number of bank of maharashtra is: 6029078513')
====================================================================

f = open('C:\\Users\\chava\\OneDrive\\Desktop\\trans2.txt')
f2 = open('trans3.txt', 'w')
data = f.readlines()
for i in data:
    f2.writelines(i.split(',')[0])
=====================================================================
"""
