
def main():
    #Escribe tu código debajo de esta línea
    def pin(x):
        for i in range(1,x+1):
                print(str("*")*i)


u = int(input("Escribe un numero: "))
pin(u)
    pass


if __name__=='__main__':
    main()
