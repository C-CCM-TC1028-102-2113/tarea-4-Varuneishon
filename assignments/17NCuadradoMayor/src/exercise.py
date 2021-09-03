

def main():
    #Escribe tu código debajo de esta línea
    n = int(input("Escribe un numero: "))
x=1
a=[]
for i in range(n+1):
        if i**2 >= n:
                a.append(i)
                print(min(a))
    pass

if __name__=='__main__':
    main()
