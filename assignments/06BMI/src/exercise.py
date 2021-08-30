def main():
    #escribe tu código abajo de esta línea
    peso = float(input('Peso en kg: '))
    alt = float(input('Altura en m: '))

    if (alt > 0) and (peso > 0):

        indi = peso / alt**2

        if (indi < 20):
            print('PESO BAJO')
        elif (20 <= indi < 25):
            print('NORMAL')
        elif (25 <= indi < 30):
            print('SOBREPESO')
        elif (30 <= indi < 40):
            print('OBESIDAD')
        elif (indi >= 40):
            print('OBESIDAD MORBIDA')
    else:
        print('Revisa tus datos, alguno de ellos es erróneo.')
        
    






if __name__=='__main__':
    main()