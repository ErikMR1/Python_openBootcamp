peso= float(input('Ingresa tu peso: '))
altura = float(input('Ingresa tu altura en metros: '))
imc= int(peso//altura**2)

if imc<18:        
    print(f'Tu indice de masa corporal es: {imc} --> Peso Bajo')
elif imc >= 18 or imc<25:
    print(f'Tu indice de masa corporal es: {imc} --> Peso Normal')
elif imc >=25 or imc<30:
    print(f'Tu indice de masa corporal es: {imc} --> Sobrepeso')
elif imc >=30 or imc<40:
    print(f'Tu indice de masa corporal es: {imc} --> Obesisad')
elif imc>40:
    print(f'Tu indice de masa corporal es: {imc} --> Obesidad Extrema')

