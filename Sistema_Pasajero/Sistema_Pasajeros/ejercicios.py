from pasajero import Pasajero
from lista_python import ListaPasajerosPython


def ejercicio_t1():
    print('\nT1 - CRUD de pasajeros')
    lista = ListaPasajerosPython()
    lista.añadir(Pasajero('Diana', '0923456789', 22))
    lista.añadir(Pasajero('Ana', '0912345678', 28))
    lista.añadir(Pasajero('Luis', '0987654321', 35))
    print('Pasajeros iniciales:')
    lista.listar()
    pos = lista.buscar('0912345678')
    print(f'Buscar Ana: [{pos}] {lista.pasajeros[pos]}')
    lista.modificar('0912345678', 'Ana María', 29)
    print('Después de modificar:')
    lista.listar()
    lista.eliminar_por_valor('0987654321')
    print('Después de eliminar a Luis:')
    lista.listar()
    lista.pasajeros.sort(key=lambda p: p.nombre)
    print('Ordenados por nombre:')
    lista.listar()


def ejercicio_t2():
    nombres = ['Ana', 'Luis', 'Diana', 'Beto', 'Elena']
    notas = [8, 6, 10, 7, 5]
    total = 0
    mayor = notas[0]
    menor = notas[0]
    mejor = nombres[0]
    aprobados = 0
    for i in range(len(notas)):
        total += notas[i]
        if notas[i] > mayor:
            mayor = notas[i]
            mejor = nombres[i]
        if notas[i] < menor:
            menor = notas[i]
        if notas[i] >= 7:
            aprobados += 1
    print(f'\nT2 - Estadísticas de notas')
    print(f'Manual: Promedio {total / len(notas):.2f} · Máx {mayor} ({mejor}) · Mín {menor} · Aprobados {aprobados} de {len(notas)}')
    mejor_python = nombres[notas.index(max(notas))]
    aprobados_python = [n for n in notas if n >= 7]
    print(f'Python: Promedio {sum(notas) / len(notas):.2f} · Máx {max(notas)} ({mejor_python}) · Mín {min(notas)} · Aprobados {len(aprobados_python)} de {len(notas)}')


def ejercicio_t3():
    datos = [5, 2, 8, 1, 9, 3, 7]
    manual = datos[:]
    for vuelta in range(len(manual) - 1):
        hubo_swap = False
        for i in range(len(manual) - 1 - vuelta):
            if manual[i] > manual[i + 1]:
                manual[i], manual[i + 1] = manual[i + 1], manual[i]
                hubo_swap = True
        if not hubo_swap:
            break
    descendente = datos[:]
    descendente.sort(reverse=True)
    palabras = ['python', 'a', 'código', 'el']
    print('\nT3 - Ordenar una lista')
    print('Manual:', manual)
    print('Python ascendente:', sorted(datos))
    print('Python descendente:', descendente)
    print('Palabras por longitud:', sorted(palabras, key=len))


def ejercicio_p1():
    numeros = [1, 3, 2, 3, 4, 3, 5]
    valor = 3
    cantidad = 0
    for numero in numeros:
        if numero == valor:
            cantidad += 1
    print('\nP1 - Contar apariciones')
    print(f'Manual: {valor} aparece {cantidad} veces')
    print(f'Python: {valor} aparece {numeros.count(valor)} veces')
    print(f'Comprensión: {len([x for x in numeros if x == valor])} veces')


def ejercicio_p2():
    numeros = [1, 2, 3, 4, 5]
    inversa = []
    for i in range(len(numeros) - 1, -1, -1):
        inversa.append(numeros[i])
    print('\nP2 - Invertir una lista')
    print('Manual:', inversa)
    print('Python (slicing):', numeros[::-1])
    print('Python (reversed):', list(reversed(numeros)))
    print('Comprensión:', [numeros[i] for i in range(len(numeros) - 1, -1, -1)])


def ejercicio_p3():
    numeros = [1, 3, 2, 3, 4, 1, 5, 2]
    unicos = []
    for numero in numeros:
        if numero not in unicos:
            unicos.append(numero)
    print('\nP3 - Números únicos')
    print('Manual:', unicos)
    print('Python:', list(dict.fromkeys(numeros)))


def ejercicio_p4():
    numeros = [5, 2, 9, 7, 9, 3, 8]
    mayor = None
    segundo = None
    for numero in numeros:
        if mayor is None or numero > mayor:
            segundo = mayor
            mayor = numero
        elif numero != mayor and (segundo is None or numero > segundo):
            segundo = numero
    comprobacion = sorted(set(numeros))[-2]
    print('\nP4 - Segundo mayor')
    print(f'Manual: Mayor {mayor} · Segundo {segundo}')
    print(f'Python: Segundo {comprobacion}')


def ejercicio_p5():
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10]
    resultado = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    print('\nP5 - Fusionar dos listas ordenadas')
    print('Manual:', resultado)
    print('Python:', sorted(a + b))


EJERCICIOS = [
    ('T1', 'CRUD de pasajeros con clase Pasajero + list', 'taller', ejercicio_t1),
    ('T2', 'Estadísticas de una lista de notas', 'taller', ejercicio_t2),
    ('T3', 'Ordenar una lista (bubble sort)', 'taller', ejercicio_t3),
    ('P1', 'Contar apariciones de un valor', 'propuesto', ejercicio_p1),
    ('P2', 'Invertir una lista', 'propuesto', ejercicio_p2),
    ('P3', 'Números únicos', 'propuesto', ejercicio_p3),
    ('P4', 'Segundo mayor', 'propuesto', ejercicio_p4),
    ('P5', 'Fusionar dos listas ordenadas', 'propuesto', ejercicio_p5),
]


def menu_ejercicios():
    while True:
        talleres = [e for e in EJERCICIOS if e[2] == 'taller']
        propuestos = [e for e in EJERCICIOS if e[2] == 'propuesto']
        print('\n--- DESARROLLADOS (taller) ---')
        for codigo, titulo, _, _ in talleres:
            print(f'{codigo}. {titulo}')
        print('--- PROPUESTOS ---')
        for codigo, titulo, _, _ in propuestos:
            print(f'{codigo}. {titulo}')
        print('0. Volver')
        codigo = input('Código: ').strip().upper()
        if codigo == '0':
            break
        encontrados = [e for e in EJERCICIOS if e[0] == codigo]
        if encontrados:
            encontrados[0][3]()
        else:
            print('Código no válido')
