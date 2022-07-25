"""
# Read and Write operations over CSV file
# CSV:
    - Comma separated values
    - it is used to read the content
    - it is read data string format
    - To perform operations related to csv file we need CSV module
------------------------------------------------------------

import csv
# Create a new csv file
f = open('sample.csv', 'w', newline='\n')
wr = csv.writer(f)
print(wr)
# use writerow function to add values as a list of string
wr.writerow(['Name', 'Age', 'Salary'])
wr.writerow(['Shivansh', 23, 45000])
wr.writerow(['Ajit', 27, 55000])
wr.writerow(['Sujit', 25, 95000])
wr.writerow(['Vijay', 22, 45000])
==================================================================

import csv
f = open('test.csv', 'a', newline='\n')
wr = csv.writer(f)
# wr.writerow(['Name', 'Age', 'Weight'])
n = int(input('How many records you want to add? '))
for i in range(n):
    nm = input('Enter the name of Student: ')
    age = int(input('Enter the age: '))
    wt = int(input('Enter the weight: '))
    wr.writerow([nm, age, wt])
=============================================================

import csv
f = open('test.csv', 'w', newline='\n')
wr = csv.writer(f)
wr.writerow(['Name', 'Age', 'Weight'])
n = int(input('How many records you want to add? '))
for i in range(n):
    nm = input('Enter the name of Student: ')
    age = int(input('Enter the age: '))
    wt = int(input('Enter the weight: '))
    wr.writerow([nm, age, wt])
wr.writerow('\n')
wr.writerow('\n')
wr.writerow('\n')
wr.writerow(['Sujit', 34, 70])
===============================================================

# Read Operation over CSV
import csv
f = open('sample.csv')
print(f.read())
----------------------------------------------------------------

import csv
f = open('sample.csv')
rd = csv.reader(f)
print(rd)
print(list(rd))
# Can we add above list as a multiple record at a time
=================================================================

# in below example, we need to take care of close operation
# In python we have solution on this
# which does auto closing of a file
f = open('a.txt')
print('Before close(): ', f.closed)
f.close()
print('After close(): ', f.closed)
==============================================================

Syntax:
with open(filename.ext) as f:
    Operations related to file inside a block
Outside the scope ur file will get closed automatically
-------------------------------------------------------------

with open('a.txt') as f:
    print(f.readline())
    print('Is file closed(inside): ', f.closed)
print('Is file closed (outside): ', f.closed)
==============================================================

with open('b.txt', 'w') as f:
    f.write('This is b.txt file\n')
    f.write('I am adding new content in this file\n')
    f.write('Lets enjoy new operation\n')
===========================================================

# can we add list of list in csv
import csv
f = open('sample_1.csv', 'w', newline= '\n')
wr = csv.writer(f)
wr.writerow(['Name', 'Mb_no', 'Place', 'Dist.'])
d = [['Meet', '9766583090', 'Khed', 'Pune'], ['Ajit', '9733452096', 'Pimpri', 'Pune'],
        ['Amit', '9762093091', 'Patan', 'Satara'], ['Sumit', '9766543071', 'Amba', 'Kolhapur']]
for i in range(len(d)):
    wr.writerow([d[i][0], d[i][1], d[i][2], d[i][3]])
===================================================================
"""