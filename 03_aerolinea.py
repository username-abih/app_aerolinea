from datetime import datetime

#metodos de validacion para reutilizacion

def validar_str(dato):
    if not isinstance(dato, str) and dato is not None:
        raise ValueError("el valor {} debe ser un str".format(dato))


def validar_int(dato):
    if not isinstance(dato, int) and dato is not None:
        raise ValueError("el valor {} debe ser un nuemero entero".format(dato))


def validar_float(dato):
    if not isinstance(dato, float) and dato is not None:
        raise ValueError("el valor {} debe ser un numero flotante".format(dato))


def validar_lista(dato):
    if not isinstance(dato, list) and dato is not None:
        raise ValueError("el valor {} debe ser una lista".format(dato))


def validar_bool(dato):
    if not isinstance(dato, bool) and dato is not None:
        raise ValueError("el valor {} debe ser un booleano".format(dato))


def validar_fecha_dd_mm_yyyy(dato):
    if dato is not None:
        x = None
        try:
            x = datetime.strptime(dato, "%d-%m-%Y")
        except:
            raise ValueError("el valor fecha_inicio no esta en formato dia-mes-año (00-00-0000) (str)")


# pasajeros y sub secuentes
class Pasajero():
    '''

    '''
    def __init__(self, id=None, nombre= None, precio_billete= None):
        validar_int(id)
        self.__id = id
        validar_str(nombre)
        self.__nombre = nombre
        validar_float(precio_billete)
        self.__precio_billete = precio_billete

    def mostrar_puntos(self):
        pass

    #setter y getters
    @property
    def id (self):
        return self.__id
    @id.setter
    def id(self, nuevo_id):
        validar_int(nuevo_id)
        self.__id = nuevo_id

    @property
    def nombre (self):
        return self.__nombre
    @nombre.setter
    def nombre (self, nuevo_nombre):
        validar_str(nuevo_nombre)
        self.__nombre = nuevo_nombre

    @property
    def precio_billete (self):
        return self.__precio_billete
    @precio_billete.setter
    def precio_billete (self, nuevo_precio_billete):
        validar_float(nuevo_precio_billete)
        self.__precio_billete = nuevo_precio_billete

    def __str__(self):
        return'''PASAJERO
        -ID:             {}
        -NOMBRE:         {}
        -PRECIO BILLETE: {}
        '''


class Pasajero_Frecuente(Pasajero):
    '''

    '''
    def __init__(self, id=None, nombre= None, precio_billete= None,
                 cantidad_puntos=None):
        super().__init__(id, nombre, precio_billete)
        validar_float(cantidad_puntos)
        self.__cantidad_puntos = cantidad_puntos

    def


class Pasajero_no_frecuente(Pasajero):
    pass

# bulto
class Bulto():
    pass

# vuelo y subsecuentes
class Vuelo():
    pass

class Vuelo_carga(Vuelo):
    pass

class Vuelo_comercial(Vuelo):
    pass

class Vuelo_internacional(Vuelo_comercial):
    pass

class Vuelo_nacional(Vuelo_comercial):
    pass


if __name__ == "__main__":
    pass