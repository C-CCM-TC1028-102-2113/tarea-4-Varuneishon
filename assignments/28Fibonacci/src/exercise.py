
def main():
    #escribe tu código abajo de esta línea
    num = int(input("Enter a number: "))
n = 0
n1 = 1
for i in range(0, num):
           if(i <= 1):
                      fib = i
           else:
                      fib = n + n1
                      n = n1
                      n1 = fib
           print(fib)
    pass

if __name__=='__main__':
    main()
