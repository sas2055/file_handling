"""
# WRITE OPERATION:

Modes used :
    All above modes are used to create a file+ performs Write operation
    'w' Write      open for writing, truncating the file first
    'a' append     open for writing, appending to the end of the file if it exists
    'x' exclusive  create a new file and open it for writing
------------------------------------------------------------------------------
# 'w' mode:
     - it is a writable mode
     - it is open for writing
     - w mode performs Truncate operation
     - remove old contents and add new contents
--------------------------------------------------------------
1. write:
    - in write operation ur content must be in string format
    - it does not accept only other format
    - it accepts only string data
----------------------------------------------------------

# lets create a new file using write mode
f = open('b.txt', mode = 'w')
print(f.writable())
f.write('This is b.txt file\n')
f.write('I am adding new content in this file\n')
f.write('Lets enjoy new operation')
# write all in one write
f.write('This is new file\nI am adding new content\nEnjoy')
# above new content is overwritten in b.txt
f.write(1234) #accepts only str data type
-----------------------------------------------------------

f = open('b.txt', mode = 'w')
f.write('this is a my new file. \nThis is my writen file. \nThis is interested topic.')
=====================================================================

2. writelines:
    - in writelines list of string + string is allowed as an input
    - int values not allowed
------------------------------------------------------------------

f = open('b.txt', 'w')
f.writelines('This is a python write function.\n')
f.writelines(['This is a my new file. \nThis is my writen file. \nThis is interested topic.'])
---------------------------------------------------------------------------------------

f = open('b.txt', 'w')
f.writelines(['Name is: shivansh\n', 'Age is: 30\n', 'Place is: Pune'])
f.writelines([12, 'A', '345', 'ASE'])   # int values not allowed
--------------------------------------------------------------

f = open('b.txt', 'w')
f.writelines('This is str we are\n supplying')
f.write(['A', 'F'])     # list is not allowed in write()
===========================================================================

# Seek() and Tell() functions in file handling
------------------------------------------------------------
1. tell():
    - it will tell current position of ur cursor in the file
    used for checking operation
--------------------------------------------------------------------------

f = open('b.txt')
print(f.tell())
# lets read some blocks
print(f.read(4))
print(f.tell())
==================================================================

2. seek():
    - bring the cursor to given position
----------------------------------------------------------------

f.seek(16)
print(f.read())
===========================================================

# read only transaction id
f = open('trans.txt', 'r')
f.seek(7)
print(f.read(12))
f.tell()
print(f.read(20))
==========================================================
"""



