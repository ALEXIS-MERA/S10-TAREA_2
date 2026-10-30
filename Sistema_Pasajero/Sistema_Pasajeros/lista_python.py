from bisect import bisect_left
from pasajero import Pasajero


class ListaPasajerosPython:
    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):
        if self.buscar(pasajero.cedula) != -1:
            return False
        self.pasajeros.append(pasajero)
        return True

    def listar(self):
        if not self.pasajeros:
            print('(lista vacía)')
        for i, pasajero in enumerate(self.pasajeros):
            print(f'[{i}] {pasajero}')

    def longitud(self):
        return len(self.pasajeros)

    def insertar(self, posicion, pasajero):
        if not 0 <= posicion <= len(self.pasajeros) or self.buscar(pasajero.cedula) != -1:
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    def buscar(self, cedula):
        posiciones = [i for i, p in enumerate(self.pasajeros) if p.cedula == cedula]
        return posiciones[0] if posiciones else -1

    def buscar_binaria(self, cedula):
        cedulas = [p.cedula for p in self.pasajeros]
        posicion = bisect_left(cedulas, cedula)
        return posicion if posicion < len(cedulas) and cedulas[posicion] == cedula else -1

    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        posicion = self.buscar(cedula)
        if posicion == -1:
            return False
        self.pasajeros[posicion].nombre = nuevo_nombre
        self.pasajeros[posicion].edad = nueva_edad
        return True

    def eliminar_por_posicion(self, posicion):
        if not 0 <= posicion < len(self.pasajeros):
            return None
        return self.pasajeros.pop(posicion)

    def eliminar_por_valor(self, cedula):
        antes = len(self.pasajeros)
        self.pasajeros = [p for p in self.pasajeros if p.cedula != cedula]
        return len(self.pasajeros) < antes

    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.cedula)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.cedula, reverse=True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
        nueva = ListaPasajerosPython()
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    def filtrar_mayores_de_edad(self):
        nueva = ListaPasajerosPython()
        nueva.pasajeros = [p for p in self.pasajeros if p.es_mayor_de_edad()]
        return nueva

    def nombres_en_mayusculas(self):
        return [p.nombre.upper() for p in self.pasajeros]

    def buscar_por_nombre(self, texto):
        nueva = ListaPasajerosPython()
        nueva.pasajeros = [p for p in self.pasajeros if texto.lower() in p.nombre.lower()]
        return nueva

    def contar_mayores(self):
        return len([p for p in self.pasajeros if p.edad >= 18])

    def promedio_edades(self):
        if not self.pasajeros:
            return 0
        return sum(p.edad for p in self.pasajeros) / len(self.pasajeros)

    def ordenar_por_nombre(self):
        self.pasajeros.sort(key=lambda p: p.nombre.lower())

    def obtener_pasajeros(self):
        return iter(self.pasajeros)

# En sort, key indica que se ordena usando la cedula.
# Sin key, Python intenta comparar pasajeros y da error.
# La copia es otra lista, pero contiene los mismos pasajeros.
# Si cambio un pasajero de la copia, cambia tambien en el original.
# insert mueve los elementos que estan despues de la posicion.
# Por eso insertar en medio puede tomar mas tiempo: O(n).
