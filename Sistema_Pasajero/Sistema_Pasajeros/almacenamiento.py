import json
from pathlib import Path
from pasajero import Pasajero


def guardar(lista, ruta):
    datos = []
    for p in lista.obtener_pasajeros():
        datos.append({'nombre': p.nombre, 'cedula': p.cedula, 'edad': p.edad})
    Path(ruta).write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding='utf-8')
    return len(datos)


def cargar(lista, ruta):
    archivo = Path(ruta)
    if not archivo.exists():
        return 0, 0
    registros = json.loads(archivo.read_text(encoding='utf-8'))
    if not isinstance(registros, list):
        raise ValueError('El archivo no contiene una lista')
    validos = []
    cedulas = set()
    for item in registros:
        if not isinstance(item, dict):
            raise ValueError('Registro incorrecto')
        nombre = item.get('nombre', '')
        cedula = item.get('cedula', '')
        edad = item.get('edad')
        if (not isinstance(nombre, str) or not nombre.strip() or
            not isinstance(cedula, str) or len(cedula) != 10 or not cedula.isdigit() or
            type(edad) is not int or edad < 0 or edad > 120 or cedula in cedulas):
            raise ValueError('Datos incorrectos o cédulas repetidas en JSON')
        cedulas.add(cedula)
        validos.append(Pasajero(nombre.strip(), cedula, edad))
    if hasattr(lista, 'capacidad') and len(validos) > lista.capacidad - lista.longitud():
        raise ValueError('No hay espacio para cargar todos los pasajeros')
    if any(lista.buscar(p.cedula) != -1 for p in validos):
        raise ValueError('Hay cédulas que ya existen en la lista')
    for p in validos:
        lista.añadir(p)
    return len(validos), len(registros)
