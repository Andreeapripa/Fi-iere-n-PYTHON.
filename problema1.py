#1)	Din fişierul « numere.txt » se citesc două numere.
#  Afişaţi în fişierul « minim.txt » numărul cel mai mic. 
with open ('numere.txt', 'r') as f:
    a=f.readline()
    b=f.readline()
if int(a)>int(b):
    c=int(b)
if int(b)>int(a):
    c=int(a)
with open('minim.txt','w') as f:
    f.write(str(c))