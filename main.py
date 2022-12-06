import time


def menu():
    print('MENU DE OPCIONES'
          '\n1- Calcular Totales y Mostrarlos'
          '\n4- SALIR')
    op = int(input('Ingrese su opcion: '))
    return op


def calcular(fd):
    kwtg = float(input('Primero ingrese el valor actual del kgwt: '))
    print('Ingrese los consumos anteriores de cada local')
    carniceria_a = float(input('Ingrese el consumo anterior en KGWTS para Carniceria: '))
    verdu_a = float(input('Ingrese el consumo anterior en KGWTS para Verduleria: '))
    almacen_a = float(input('Ingrese el consumo anterior en KGWTS para Almacen: '))
    libreria_a = float(input('Ingrese el consumo anterior en KGWTS para Libreria: '))
    panaderia_a = float(input('Ingrese el consumo anterior en KGWTS para Panaderia: '))
    dietetica_a = float(input('Ingrese el consumo anterior en KGWTS para Dietetica: '))
    print('-'*10, 'GUARDANDO DATOS', '-'*10)
    time.sleep(1)
    print('Ahora Ingrese los consumos actuales')
    carniceria = float(input('Consumo actual en KGWTS para Carniceria: '))
    verdu = float(input('Consumo actual en KGWTS para Verduleria: '))
    almacen = float(input('Consumo actual en KGWTS para Almacen: '))
    libreria = float(input('Consumo actual en KGWTS para Libreria: '))
    panaderia = float(input('Consumo actual en KGWTS para Panaderia: '))
    dietetica = float(input('Consumo actual en KGWTS para Dietetica: '))

    print('-'*10, 'CALCULANDO', '-'*10)
    time.sleep(1)
    # Calculo el consumo real
    carniceria_sf = round(carniceria - carniceria_a)
    verdu_sf = round(verdu - verdu_a, 4)
    almacen_sf = round(almacen - almacen_a, 4)
    libreria_sf = round(libreria - libreria_a, 4)
    panaderia_sf = round(panaderia - panaderia_a, 4)
    dietetica_sf = round(dietetica - dietetica_a, 4)

    # Calculo el monto a pagar
    carniceria_f = round(carniceria_sf * kwtg, 4)
    verdu_f = round(verdu_sf * kwtg, 4)
    almacen_f = round(almacen_sf * kwtg, 4)
    libreria_f = round(libreria_sf * kwtg, 4)
    panaderia_f = round(panaderia_sf * kwtg, 4)
    dietetica_f = round(dietetica_sf * kwtg, 4)

    print('-'*10, 'MOSTRANDO DATOS DE CADA LOCAL', '-'*10)
    time.sleep(1)
    print('CARNICERIA: \nConsumo: ', carniceria_sf, '\nPago: ', carniceria_f, '\n---------------------------')
    print('VERDULERIA: \nConsumo: ', verdu_sf, '\nPago: ', verdu_f, '\n---------------------------')
    print('ALMACEN: \nConsumo: ', almacen_sf, '\nPago: ', almacen_f, '\n---------------------------')
    print('LIBRERIA: \nConsumo: ', libreria_sf, '\nPago: ', libreria_f, '\n---------------------------')
    print('PANADERIA: \nConsumo: ', panaderia_sf, '\nPago: ', panaderia_f, '\n---------------------------')
    print('DIETETICA: \nConsumo: ', dietetica_sf, '\nPago: ', dietetica_f, '\n---------------------------')

    print('-'*10, 'MOSTRANDO DATOS TOTALES', '-'*10)
    time.sleep(1)
    a = round(carniceria_sf + verdu_sf + almacen_sf + libreria_sf + panaderia_sf + dietetica_sf, 4)
    b = round(carniceria_f + verdu_f + almacen_f + libreria_f + panaderia_f + dietetica_f, 4)
    print('El Consumo total es: ', a, '\n---------------------------')
    print('El monto a pagar total es: ', b, '\n---------------------------')
    # Abrimos archivo de texto para guardar los datos
    open(fd, 'at')
    for line in fd:
        print(a, b)


def main():
    fd = 'diciembre.txt'
    op = 0
    while op != 6:
        op = menu()
        if op == 1:
            calcular(fd)
        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            print('Hasta Luego! ')
        else:
            print('Ingrese una opcion correcta')


if __name__ == '__main__':
    main()
