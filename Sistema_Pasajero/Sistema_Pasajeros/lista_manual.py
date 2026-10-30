from pasajero import Pasajero


class ListaPasajerosManual:
    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def añadir(self, pasajero):
        if self.cantidad >= self.capacidad or self.buscar(pasajero.cedula) != -1:
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad += 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print('(lista vacía)')
        for i in range(self.cantidad):
            print(f'[{i}] {self.datos[i]}')

    def longitud(self):
        return self.cantidad

    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > self.cantidad or self.cantidad >= self.capacidad:
            return False
        if self.buscar(pasajero.cedula) != -1:
            return False
        for i in range(self.cantidad, posicion, -1):
            self.datos[i] = self.datos[i - 1]
        self.datos[posicion] = pasajero
        self.cantidad += 1
        return True

    def buscar(self, cedula):
        for i in range(self.cantidad):
            if self.datos[i].cedula == cedula:
                return i
        return -1

    def buscar_binaria(self, cedula):
        izq = 0
        der = self.cantidad - 1
        while izq <= der:
            medio = (izq + der) // 2
            if self.datos[medio].cedula == cedula:
                return medio
            if self.datos[medio].cedula < cedula:
                izq = medio + 1
            else:
                der = medio - 1
        return -1

    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        posicion = self.buscar(cedula)
        if posicion == -1:
            return False
        self.datos[posicion].nombre = nuevo_nombre
        self.datos[posicion].edad = nueva_edad
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            return None
        eliminado = self.datos[posicion]
        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]
        self.cantidad -= 1
        self.datos[self.cantidad] = None
        return eliminado

    def eliminar_por_valor(self, cedula):
        posicion = self.buscar(cedula)
        if posicion == -1:
            return False
        self.eliminar_por_posicion(posicion)
        return True

    def ordenar_asc(self):
        for vuelta in range(self.cantidad - 1):
            for i in range(self.cantidad - 1 - vuelta):
                if self.datos[i].cedula > self.datos[i + 1].cedula:
                    aux = self.datos[i]
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = aux

    def ordenar_desc(self):
        for vuelta in range(self.cantidad - 1):
            for i in range(self.cantidad - 1 - vuelta):
                if self.datos[i].cedula < self.datos[i + 1].cedula:
                    aux = self.datos[i]
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = aux

    def reversar(self):
        izq = 0
        der = self.cantidad - 1
        while izq < der:
            aux = self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der] = aux
            izq += 1
            der -= 1

    def copiar(self):
        nueva = ListaPasajerosManual(self.capacidad)
        for i in range(self.cantidad):
            p = self.datos[i]
            nueva.añadir(p)
        return nueva

    def filtrar_mayores_de_edad(self):
        nueva = ListaPasajerosManual(self.capacidad)
        for i in range(self.cantidad):
            p = self.datos[i]
            if p.edad >= 18:
                nueva.añadir(p)
        return nueva

    def nombres_en_mayusculas(self):
        nombres = [None] * self.cantidad
        for i in range(self.cantidad):
            nombres[i] = self.datos[i].nombre.upper()
        return nombres

    def buscar_por_nombre(self, texto):
        resultado = ListaPasajerosManual(self.capacidad)
        for i in range(self.cantidad):
            p = self.datos[i]
            if texto.lower() in p.nombre.lower():
                resultado.añadir(p)
        return resultado

    def contar_mayores(self):
        total = 0
        for i in range(self.cantidad):
            if self.datos[i].edad >= 18:
                total += 1
        return total

    def promedio_edades(self):
        if self.cantidad == 0:
            return 0
        total = 0
        for i in range(self.cantidad):
            total += self.datos[i].edad
        return total / self.cantidad

    def ordenar_por_nombre(self):
        for vuelta in range(self.cantidad - 1):
            for i in range(self.cantidad - 1 - vuelta):
                if self.datos[i].nombre.lower() > self.datos[i + 1].nombre.lower():
                    aux = self.datos[i]
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = aux

    def obtener_pasajeros(self):
        for i in range(self.cantidad):
            yield self.datos[i]
