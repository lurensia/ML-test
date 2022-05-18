import csv
 
a = open('bream_length.csv','r')
b = open('bream_weight.csv','r')
c = open('smelt_length.csv','r')
d = open('smelt_weight.csv','r')
rdr = csv.reader(a)
for line in rdr:
    print(line)
a.close()
print('=================')
rdr = csv.reader(b)
for line in rdr:
    print(line)
b.close()
print('=================')
rdr = csv.reader(c)
for line in rdr:
    print(line)
c.close()
print('=================')
rdr = csv.reader(d)
for line in rdr:
    print(line)
d.close()
print('=================')
 
 

