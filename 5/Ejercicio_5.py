year=int(input("Ingresa el año: "))

def es_bisiesto(año):
    if(año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        resultado = f'El {año} es bisiesto'
        return resultado
    else:
        resultado = f'El {año} no es bisiesto'
        return resultado
   
print(es_bisiesto(year))
