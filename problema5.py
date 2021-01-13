#5)	Afişaţi tabla înmulţirii cu numărul n. Exemplu: pentru n=5, 
# se va afişa pe verticală 1x5=5  2x5=10 3x5=15 4x5=20 5x5=25 6x5=30 7x5=35 8x5=40 9x5=45 10x5=50. 
#Din fişierul « numar.txt » se citeşte un număr, 
# în fişierul « inmultire.txt » - se înscrie tabla înmulţirii cu acest număr.
with open ('numar.txt', 'r') as f:
    n=int(f.readline())
with open ('inmultire.txt', 'w') as f:
    f.write('1*'+str(n)+'='+str(n*1)+'\n')
    f.write('2*'+str(n)+'='+str(n*2)+'\n')
    f.write('3*'+str(n)+'='+str(n*3)+'\n')
    f.write('4*'+str(n)+'='+str(n*4)+'\n')
    f.write('5*'+str(n)+'='+str(n*5)+'\n')
    f.write('6*'+str(n)+'='+str(n*6)+'\n')
    f.write('7*'+str(n)+'='+str(n*7)+'\n')
    f.write('8*'+str(n)+'='+str(n*8)+'\n')
    f.write('9*'+str(n)+'='+str(n*9)+'\n')
    f.write('10*'+str(n)+'='+str(n*10)+'\n')
