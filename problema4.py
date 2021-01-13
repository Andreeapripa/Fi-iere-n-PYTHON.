#4)	Ion şi Vasile joacă următorul joc: Ion spune un număr iar Vasile trebuie să găsească
#  cinci numere consecutive, crescătoare, numărul din mijloc fiind cel ales de Ion. 
with open ('input.txt','r') as f:
    a=f.readline()
with open ('output.txt','w') as f:
    f.write(str(int(a)-2)) 
    f.write(str(int(a)-1))
    f.write(a)
    f.write(str(int(a)+1))
    f.write(str(int(a)+2))