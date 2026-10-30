import tempfile
from pathlib import Path
from pasajero import Pasajero
from lista_manual import ListaPasajerosManual
from lista_python import ListaPasajerosPython
from almacenamiento import guardar, cargar


def verificar(tipo):
    lista = tipo() if tipo == ListaPasajerosPython else tipo(10)
    assert lista.añadir(Pasajero('Luis', '0987654321', 35))
    assert lista.añadir(Pasajero('Ana', '0912345678', 28))
    assert lista.añadir(Pasajero('Beto', '0934567890', 16))
    assert not lista.añadir(Pasajero('Ana repetida', '0912345678', 30))
    assert lista.longitud() == 3
    assert lista.contar_mayores() == 2
    assert lista.promedio_edades() == (35 + 28 + 16) / 3
    assert lista.buscar_por_nombre('a').longitud() == 1
    lista.ordenar_por_nombre()
    assert [p.nombre for p in lista.obtener_pasajeros()] == ['Ana', 'Beto', 'Luis']
    lista.ordenar_asc()
    assert lista.buscar_binaria('0987654321') == 2
    copia = lista.copiar()
    copia.reversar()
    assert [p.cedula for p in lista.obtener_pasajeros()] != [p.cedula for p in copia.obtener_pasajeros()]
    with tempfile.TemporaryDirectory() as t:
        archivo = Path(t) / 'datos.json'
        assert guardar(lista, archivo) == 3
        nueva = tipo() if tipo == ListaPasajerosPython else tipo(10)
        assert cargar(nueva, archivo)[0] == 3
        assert nueva.longitud() == 3
        try:
            cargar(nueva, archivo)
            raise AssertionError('Debió rechazar duplicados')
        except ValueError:
            pass
    assert lista.eliminar_por_valor('0934567890')
    assert lista.longitud() == 2
    print(tipo.__name__, 'OK')


verificar(ListaPasajerosManual)
verificar(ListaPasajerosPython)
