"""
# READ OPERATION:
        - I have 3 options present in r mode
        - read(), readline(), readlines()
---------------------------------------------------------------------

1. read():
    - read() will read all the contents start to end
----------------------------------------------------------

f = open('A.txt')   # Default its read mode
# case sensitivity about file name is not an issue here
# but extension(.txt) + proper name u should give  while reading
print(f.read())
-----------------------------------------------------------

f = open('a.txt')
# now read the contents from a file
print(f)
print(f.read())
---------------------------------------------------------

f = open('handle.py')
print(f.read())
----------------------------------------------------------

# then other folder of file read
f = open('E:\\PycharmProjects\\Shital\\flow_control_blocks\\flow_1.py')
print(f.read(500))
print(f.readline())
----------------------------------------------------------

# suppose if u want to read some specific part
f = open('a.txt')
print(f.read(10))
print(f.read(20))
===============================================================

2. readline():
     - it reads one line at a time
--------------------------------------------------------------

f = open('a.txt')
print(f.readline())
print(f.readline())
---------------------------------------------------------------

# readline(limit):
        - it reads one line at a time
-------------------------------------------------------------

f = open('a.txt')
print(f.readline(5))    # will read 5 block from line1
print(f.readline(5))    # will read 5 block from line1
print(f.readline())     # will read remaining block from line1
print(f.readline())     # will read next line
---------------------------------------------------------------

# read a file from another directory
f = open('E:\\PycharmProjects\\Shital\\out.txt')
print(f)
print(f.readline())
print(f.readline(2000))
print(f.readline(5000))
print(f.readline())
print(f.readline())
-------------------------------------------------------------------

# read a file from desktop
f = open('C:\\Users\\chava\\OneDrive\\Desktop\\b.txt.txt')
print(f)
print(f.readline())
print(f.readline(10))
print(f.readline(3))
print(f.readline())
--------------------------------------------------------------------

f = open('a.txt')
print(f.read()) # used to read all the contents
print(f.readline()) # used to read one line at a time
================================================================

3. readlines():
    - it is used to read all the contents but
    - format is: list of string
    - means each line of a text file will be a one element of a list
---------------------------------------------------------------

f = open('a.txt')
print(f.readlines())
===============================================================

# Iterations using the read operation
1. read():
    - read a single block/char line by line
------------------------------------------------------

f = open('a.txt')
data = f.read()
for i in data:
    print(i)
========================================================

2. readlines():
    - read a first line character by character
---------------------------------------------------------

f = open('a.txt')
data = f.readline()
for i in data:
    print(i)
========================================================

3. readlines():
    - read a line by line
    - bcz its a list of string
    - so one line at a time it will read
    - All the lines will be visited
-------------------------------------------------------

f = open('a.txt')
data = f.readlines()
for i in data:
    print(i)
--------------------------------------------------------------

f = open('a.txt')
print(f.read(14))
print(f.read())
for i in range(3):
    print(f.read())
------------------------------------------------------------

# will read first 3 lines
f = open('a.txt')
for i in range(3):
    print(f.readline())
----------------------------------------------------------

# next two iteration are performed to empty lists
f = open('a.txt')
for i in range(3):
    print(f.readlines())
===========================================================
"""
