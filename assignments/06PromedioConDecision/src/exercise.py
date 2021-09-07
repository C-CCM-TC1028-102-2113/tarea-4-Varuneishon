def main():
    #escribe tu código abajo de esta línea
   i = float(input('Please enter a number: '))
s = 0
c = 0

if i>0:
    c=1
    t=0
    while t>=0:
        i1 = float(input('Please enter another number: '))
        t=i1
        i=i+i1
        c=c+1
        a=i/c


    print(a)
else:
    print('no es valido')
    pass
if __name__=='__main__':
    main()
