from pasajero import Pasajero
from lista_manual import ListaPasajerosManual
from lista_python import ListaPasajerosPython
from ejercicios import menu_ejercicios
from almacenamiento import guardar, cargar

lista1 = ListaPasajerosManual(10)
lista2 = ListaPasajerosPython()


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('Debe ingresar un número entero.')


def leer_pasajero():
    while True:
        nombre = input('Nombre: ').strip()
        if nombre:
            break
        print('Escribe un nombre')
    while True:
        cedula = input('Cédula (10 dígitos): ').strip()
        if len(cedula) == 10 and cedula.isdigit():
            break
        print('La cédula debe tener 10 números')
    while True:
        edad = leer_entero('Edad: ')
        if 0 <= edad <= 120:
            break
        print('Edad no válida')
    return Pasajero(nombre, cedula, edad)


def cargar_datos_prueba(lista):
    datos = [
        ('Diana', '0923456789', 22),
        ('Ana', '0912345678', 28),
        ('Luis', '0987654321', 35),
        ('Beto', '0934567890', 16),
        ('Elena', '0901234567', 41),
    ]
    cargados = 0
    for nombre, cedula, edad in datos:
        if lista.añadir(Pasajero(nombre, cedula, edad)):
            cargados += 1
    print(f'{cargados} pasajeros de prueba cargados')


def mostrar_menu_lista(titulo):
    print(f'\n========== {titulo} ==========')
    print('1. Añadir pasajero')
    print('2. Listar pasajeros')
    print('3. Insertar en una posición')
    print('4. Buscar por cédula (lineal)')
    print('5. Buscar por cédula (binaria)')
    print('6. Modificar pasajero')
    print('7. Eliminar por posición')
    print('8. Eliminar por cédula')
    print('9. Ordenar ascendente')
    print('10. Ordenar descendente')
    print('11. Reversar')
    print('12. Copiar lista')
    print('13. Longitud')
    print('14. Filtrar mayores de edad')
    print('15. Nombres en mayúsculas')
    print('16. Buscar pasajeros por nombre')
    print('17. Estadísticas de edades')
    print('18. Ordenar por nombre')
    print('19. Guardar en JSON')
    print('20. Cargar desde JSON')
    print('C. Cargar datos de prueba')
    print('0. Volver')


def menu_lista(lista, titulo):
    while True:
        mostrar_menu_lista(titulo)
        opcion = input('Opción: ').strip().upper()
        if opcion == '0':
            break
        if opcion == 'C':
            cargar_datos_prueba(lista)
        elif opcion == '1':
            print('Pasajero añadido' if lista.añadir(leer_pasajero()) else 'No se pudo añadir (cédula repetida o lista llena)')
        elif opcion == '2':
            lista.listar()
        elif opcion == '3':
            pos = leer_entero('Posición: ')
            print('Pasajero insertado' if lista.insertar(pos, leer_pasajero()) else 'No se pudo insertar')
        elif opcion in ('4', '5'):
            if opcion == '5':
                print('Se ordenará por cédula antes de buscar')
            cedula = input('Cédula: ').strip()
            if opcion == '5':
                lista.ordenar_asc()
            pos = lista.buscar(cedula) if opcion == '4' else lista.buscar_binaria(cedula)
            if pos == -1:
                print('No existe')
            else:
                pasajero = lista.datos[pos] if isinstance(lista, ListaPasajerosManual) else lista.pasajeros[pos]
                print(f'Encontrado en [{pos}]: {pasajero}')
        elif opcion == '6':
            cedula = input('Cédula: ').strip()
            nombre = input('Nuevo nombre: ').strip()
            edad = leer_entero('Nueva edad: ')
            if nombre and 0 <= edad <= 120:
                print('Pasajero modificado' if lista.modificar(cedula, nombre, edad) else 'No existe')
            else:
                print('Nombre o edad no válidos')
        elif opcion == '7':
            eliminado = lista.eliminar_por_posicion(leer_entero('Posición: '))
            print(f'Eliminado: {eliminado}' if eliminado is not None else 'Posición no válida')
        elif opcion == '8':
            cedula = input('Cédula: ').strip()
            print('Pasajero eliminado' if lista.eliminar_por_valor(cedula) else 'No existe')
        elif opcion == '9':
            lista.ordenar_asc()
            lista.listar()
        elif opcion == '10':
            lista.ordenar_desc()
            lista.listar()
        elif opcion == '11':
            lista.reversar()
            lista.listar()
        elif opcion == '12':
            copia = lista.copiar()
            copia.reversar()
            print('--- COPIA (reversada) ---')
            copia.listar()
            print('--- ORIGINAL ---')
            lista.listar()
        elif opcion == '13':
            print(f'Hay {lista.longitud()} pasajeros')
        elif opcion == '14':
            lista.filtrar_mayores_de_edad().listar()
        elif opcion == '15':
            print(lista.nombres_en_mayusculas())
        elif opcion == '16':
            texto = input('Parte del nombre: ').strip()
            lista.buscar_por_nombre(texto).listar()
        elif opcion == '17':
            print('Pasajeros:', lista.longitud())
            print('Mayores de edad:', lista.contar_mayores())
            print(f'Promedio de edades: {lista.promedio_edades():.2f}')
        elif opcion == '18':
            lista.ordenar_por_nombre()
            lista.listar()
        elif opcion == '19':
            ruta = 'pasajeros_manual.json' if isinstance(lista, ListaPasajerosManual) else 'pasajeros_python.json'
            try:
                total = guardar(lista, ruta)
                print(f'Se guardaron {total} pasajeros en {ruta}')
            except OSError as error:
                print('Error al guardar:', error)
        elif opcion == '20':
            ruta = 'pasajeros_manual.json' if isinstance(lista, ListaPasajerosManual) else 'pasajeros_python.json'
            try:
                agregados, _ = cargar(lista, ruta)
                print(f'Se cargaron {agregados} pasajeros')
            except (OSError, ValueError) as error:
                print('No se pudieron cargar los datos:', error)
        else:
            print('Opción no válida')


def menu_lista1():
    menu_lista(lista1, 'LISTA 1 - desde cero')


def menu_lista2():
    menu_lista(lista2, 'LISTA 2 - list de Python')


def main():
    while True:
        print('\n=== SISTEMA DE PASAJEROS ===')
        print('1. Lista 1 (desde cero)')
        print('2. Lista 2 (list de Python)')
        print('3. Listar ejercicios')
        print('4. Salir')
        opcion = input('Opción: ').strip()
        if opcion == '1':
            menu_lista1()
        elif opcion == '2':
            menu_lista2()
        elif opcion == '3':
            menu_ejercicios()
        elif opcion == '4':
            print('¡Hasta pronto!')
            break
        else:
            print('Opción no válida')


if __name__ == '__main__':
    main()
