def main():
    #escribe tu código abajo de esta línea
    n = int(input('How many numbers: '))
t = 0
	
for i in range(0,n):
	num = float(input('Enter number : '))
t += num
	
avg = t/n
print('Average of ', n, ' numbers is :', avg)
    pass
if __name__=='__main__':
    main()
