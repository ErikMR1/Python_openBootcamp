inicio=int(input('Ingresa el numero de inicio: '))
fin=int(input('Ingresa elnumero de fin: '))

for i in range(inicio,fin+1):
    if i%2!=0:
        print(i)