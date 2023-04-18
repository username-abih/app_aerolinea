from datetime import datetime

#metodos de validacion para reutilizacion
def validar_str(dato):
    if not isinstance(dato, str) and dato is not None:
        raise ValueError("el valor {} debe ser un str".format(dato))


def validar_int(dato):
    if not isinstance(dato, int) and dato is not None:
        raise ValueError("el valor {} debe ser un numero entero".format(dato))


def validar_float(dato):
    if not isinstance(dato, float) and not isinstance(dato, int) and dato is not None :
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
            raise ValueError("el valor fecha no esta en formato dia-mes-año (00-00-0000) (str)")

def validar_hora_hh_mm(dato):
    if dato is not None:
        x = None
        try:
            x = datetime.strptime(dato, "%H:%M")
        except:
            raise ValueError("el valor Hora no esta en formato 24:00")

# pasajeros y subsecuentes
class Pasajero():
    '''Clase Pasajero con los atributos id, nombre y precio billete,
    con el metodo mostrar puntos

    ARGS
    -Id: numero unico e irrepetible para identificar al pasajero
    -Nombre: nombre del pasajero
    -precio billete: precio total del billete
    '''
    def __init__(self, id=None, nombre= None, precio_billete= None):
        validar_int(id)
        self.__id = id
        validar_str(nombre)
        self.__nombre = nombre
        validar_float(precio_billete)
        self.__precio_billete = precio_billete

    #funcion mostrar puntos que muestra los puntos actuales del pasajero
    def mostrar_puntos(self):
        print("puntos actuales: {}".format(self.__cantidad_puntos))

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
        return'''
        -ID:             {}
        -NOMBRE:         {}
        -PRECIO BILLETE: {}'''.format(self.__id, self.__nombre, self.__precio_billete)


class Pasajero_frecuente(Pasajero):
    '''Clase Pasajero frecuente con los atributos id, nombre, precio billete,
    y cantidad de puntos, con el metodo mostrar puntos heredado del padre

    ARGS
    -Id: numero unico e irrepetible para identificar al pasajero
    -Nombre: nombre del pasajero
    -precio billete: precio total del billete
    -cantidad puntos: cantidad de puntos recolectados por los vuelos del cliente
    '''
    def __init__(self, id=None, nombre= None, precio_billete= None,
                 cantidad_puntos=0):
        super().__init__(id, nombre, precio_billete)
        validar_float(cantidad_puntos)
        self.__cantidad_puntos = cantidad_puntos

    def mostrar_puntos(self):
        super().mostrar_puntos()

    #getter y setter
    @property
    def cantidad_puntos(self):
        return self.__cantidad_puntos
    @cantidad_puntos.setter
    def cantidad_puntos(self, nuevos_puntos):
        validar_float(nuevos_puntos)
        self.__cantidad_puntos = nuevos_puntos

    def __str__(self):
        return "Pasajero Frecuente" + super().__str__() + '''
        -PUNTOS: {}'''.format(self.__cantidad_puntos)


class Pasajero_no_frecuente(Pasajero):
    '''Clase Pasajero frecuente con los atributos id, nombre, precio billete,
    y cantidad de puntos, con el metodo mostrar puntos heredado del padre

    ARGS
    -Id: numero unico e irrepetible para identificar al pasajero
    -Nombre: nombre del pasajero
    -precio billete: precio total del billete
    -cantidad puntos: cantidad de puntos recolectados por los vuelos del cliente
    '''
    def __init__(self, id=None, nombre= None, precio_billete= None,
                 cantidad_puntos=0):
        super().__init__(id, nombre, precio_billete)
        validar_float(cantidad_puntos)
        self.__cantidad_puntos = cantidad_puntos

    # getter y setter
    @property
    def cantidad_puntos(self):
        return self.__cantidad_puntos
    @cantidad_puntos.setter
    def cantidad_puntos(self, nuevos_puntos):
            validar_float(nuevos_puntos)
            self.__cantidad_puntos = nuevos_puntos

    def __str__(self):
        return "Pasajero no frecuente" + super().__str__() + '''
        -PUNTOS: {}'''.format(self.__cantidad_puntos)


# bulto
class Bulto():
    '''Bulto que contiene los atributos ID y Peso.

    ARGS:
    -ID: numero unico e irrepetible para identificar al bulto
    -Peso: peso total del bulto
    '''
    def __init__(self, id= None, peso= None):
        validar_int(id)
        self.__id = id
        validar_float(peso)
        self.__peso = peso

    #setter y getters
    @property
    def id (self):
        return self.__id
    @id.setter
    def id (self, nuevo_id):
        validar_int(nuevo_id)
        self.__id = nuevo_id

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, nuevo_peso):
        validar_float(nuevo_peso)
        self.__peso = nuevo_peso

    def __str__(self):
        return '''Bulto
        -ID: {}
        -PESO {} KG'''.format(self.__id, float(self.__peso))


# vuelo y subsecuentes
class Vuelo():
    '''clase Vuelo con los atributos numero, hora de salida, hora de llegada y destino.

    ARGS:
    -numero: numero de serie unico e irrepetible del vuelo
    -hora de salida: hora de salida del vuelo
    -hora de llegada: hora de llegada del vuelo
    -destino: destino del vuelo
    '''
    def __init__(self, numero= None, hora_salida= None, hora_llegada=None,
                 destino= None):
        validar_int(numero)
        self.__numero = numero
        validar_hora_hh_mm(hora_salida)
        self.__hora_salida = hora_salida
        validar_hora_hh_mm(hora_llegada)
        self.__hora_llegada = hora_llegada
        validar_str(destino)
        self.__destino = destino

    #getter y setters
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, nuevo_numero):
        validar_int(nuevo_numero)
        self.__numero = nuevo_numero

    @property
    def hora_salida(self):
        return self.__hora_salida
    @hora_salida.setter
    def hora_salida(self, nueva_hora_salida):
        validar_float(nueva_hora_salida)
        self.__hora_salida = nueva_hora_salida

    @property
    def hora_llegada(self):
        return self.__hora_llegada
    @hora_llegada.setter
    def hora_llegada(self, nueva_hora_llegada):
        validar_float(nueva_hora_llegada)
        self.__hora_llegada = nueva_hora_llegada

    @property
    def destino(self):
        return self.__destino
    @destino.setter
    def destino(self, nuevo_destino):
        validar_str(nuevo_destino)
        self.__destino = nuevo_destino

    def __str__(self):
        return ''' con numero: {}
        -Destino: {}
        -Hora de salida:    {}
        -Hora de llegada:   {}'''.format(self.__numero, self.__destino,
                   self.__hora_salida, self.__hora_llegada)


class Vuelo_carga(Vuelo):
    '''clase Vuelo de carga con los atributos numero, hora de salida, hora de llegada, destino,
    lista de carga y peso maximo, contiene los metodos agregar carga y mostrar carga.

    ARGS:
    -numero: numero de serie unico e irrepetible del vuelo
    -hora de salida: hora de salida del vuelo
    -hora de llegada: hora de llegada del vuelo
    -destino: destino del vuelo
    -lista carga: lista con todos los bultos que llevara el vuelo
    -peso maximo: peso maximo permitido por el vuelo
    '''
    def __init__(self, numero= None, hora_salida= None, hora_llegada=None,
                 destino= None, lista_carga= [], peso_maximo= None):
        super().__init__(numero, hora_salida, hora_llegada, destino)
        validar_lista(lista_carga)
        self.__lista_carga = lista_carga
        validar_float(peso_maximo)
        self.__peso_maximo = peso_maximo

    #metodo para agregar carga nueva a la lista de carga
    def agregar_carga(self, nueva_carga):
        self.__lista_carga.append(nueva_carga)

    #metodo para mostrar todos los str de los objetos que contiene la lista de carga
    def mostrar_carga(self):
        for i in self.__lista_carga:
            print(i)

    #getter y setters
    @property
    def lista_carga(self):
        return self.__lista_carga
    @lista_carga.setter
    def lista_carga(self, nueva_lista_carga):
        validar_lista(nueva_lista_carga)
        self.__lista_carga = nueva_lista_carga

    @property
    def peso_maximo(self):
        return self.__peso_maximo
    @peso_maximo.setter
    def peso_maximo(self, nuevo_peso_maximo):
        validar_float(nuevo_peso_maximo)
        self.__peso_maximo = nuevo_peso_maximo

    def __str__(self):
        return "vuelo de Carga" + super().__str__() + '''
        -Cantidad de articulos a cargar: {}
        -Peso maximo: {}'''.format(len(self.__lista_carga),
                                   self.__peso_maximo)

class Vuelo_comercial(Vuelo):
    '''clase Vuelo comercial con los atributos numeero, hora de salida, hora de llegada, destino y lista de pasajeros.

    ARGS:
    -numero: numero de serie unico e irrepetible del vuelo
    -hora de salida: hora de salida del vuelo
    -hora de llegada: hora de llegada del vuelo
    -destino: destino del vuelo
    -lista de pasajeros: lista de pasajeros que ira en el vuelo'''

    def __init__(self, numero=None, hora_salida=None, hora_llegada=None,
                 destino=None, lista_pasajeros= []):
        super().__init__(numero, hora_salida, hora_llegada, destino)
        validar_lista(lista_pasajeros)
        self.__lista_pasajeros = lista_pasajeros

    #metodo para agregar pasajero a la lista de pasajeros
    def agregar_pasajero(self, pasajero):
        self.__lista_pasajeros.append(pasajero)

    #metodo para mostrar la lista de pasajeros
    def mostrar_lista_pasajeros(self):
        for i in self.__lista_pasajeros:
            print(i)

    #getter y setters
    @property
    def lista_pasajeros(self):
        return self.__lista_pasajeros
    @lista_pasajeros.setter
    def lista_pasajeros(self, nueva_lista_pasajeros):
        validar_lista(nueva_lista_pasajeros)
        self.__lista_pasajeros = nueva_lista_pasajeros

    def __str__(self):
        return super().__str__() + '''
        -Cantidad de Pasajeros: {}'''.format(len(self.__lista_pasajeros))


class Vuelo_internacional(Vuelo_comercial):
    '''clase Vuelo internacional con los atributos numeero, hora de salida, hora de llegada, destino,
     lista de pasajeros y escalas.

    ARGS:
    -numero: numero de serie unico e irrepetible del vuelo
    -hora de salida: hora de salida del vuelo
    -hora de llegada: hora de llegada del vuelo
    -destino: destino del vuelo
    -lista de pasajeros: lista de pasajeros que ira en el vuelo
    -Escalas: lista de lugares donde aterrizara el avion y volvera a salir'''

    def __init__(self, numero=None, hora_salida=None, hora_llegada=None,
                 destino=None, lista_pasajeros=[], escalas= []):
        super().__init__(numero, hora_salida, hora_llegada,
                         destino, lista_pasajeros)
        validar_lista(escalas)
        self.__escalas = escalas

    #muestra las escalas que realizara el vuelo
    def mostrar_escalas(self):
        print("las escalas que realizara el vuelo {} con destino {} son:".format(self.__numero, self.__destino))
        for i in self.__escalas:
            print("     -".format(i))

    #getter y setters
    @property
    def escalas(self):
        return self.__escalas
    @escalas.setter
    def escalas(self, nuevas_escalas):
        validar_lista(nuevas_escalas)
        self.__escalas = nuevas_escalas

    def __str__(self):
        return "Vuelo Comercial Internacional" + super().__str__() + '''
        -Cantidad de escalas {}'''.format(len(self.__escalas))

class Vuelo_nacional(Vuelo_comercial):
    '''clase Vuelo nacional con los atributos numeero, hora de salida, hora de llegada, destino,
     lista de pasajeros y numero minimo de pasajeros

    ARGS:
    -numero: numero de serie unico e irrepetible del vuelo
    -hora de salida: hora de salida del vuelo
    -hora de llegada: hora de llegada del vuelo
    -destino: destino del vuelo
    -lista de pasajeros: lista de pasajeros que ira en el vuelo
    -Numero minimo de pasajeros: numero minimo de pasajeros para que costee el vuelo'''

    def __init__(self, numero=None, hora_salida=None, hora_llegada=None,
                 destino=None, lista_pasajeros=[], num_minimo_pasajeros= None):
        super().__init__(numero, hora_salida, hora_llegada,
                         destino, lista_pasajeros)
        validar_int(num_minimo_pasajeros)
        self.__num_minimo_pasajeros = num_minimo_pasajeros

    def puede_volar(self):
        if len(self.__lista_pasajeros) >= self.__num_minimo_pasajeros:
            return True
        else:
            return False

    #getter y setter
    @property
    def num_minimo_pasajeros(self):
        return self.__num_minimo_pasajeros
    @num_minimo_pasajeros.setter
    def num_minimo_pasajeros(self, nuevo_min_pasajeros):
        validar_int(nuevo_min_pasajeros)
        self.__num_minimo_pasajeros = nuevo_min_pasajeros

    def __str__(self):
        return "Vuelo Comercial Nacional" + super().__str__() + '''
        -Numero minimo de pasajeros: {}'''.format(self.__num_minimo_pasajeros)

if __name__ == "__main__":
    #creamos objetos
    #pasajeros
    pasajero1 = Pasajero(1001,"pasajero1",1000)
    pasajero2 = Pasajero(1002,"pasajero2",1000)
    pasajero3 = Pasajero(1003,"pasajero3",1000)

    #pasajeros frecuentes
    p_frecuente1 = Pasajero_frecuente(1004,"frecuente1",1000,100)
    p_frecuente2 = Pasajero_frecuente(1005,"frecuente2",1000,200)
    p_frecuente3 = Pasajero_frecuente(1006,"frecuente3",1000,200)

    #pasajeros infrecuentes
    p_infrecuente1 = Pasajero_no_frecuente(1006, "pasajero_no_f1", 1000, 0)
    p_infrecuente2 = Pasajero_no_frecuente(1007, "pasajero_no_f2", 1000, 0)
    p_infrecuente3 = Pasajero_no_frecuente(1008, "pasajero_no_f3", 1000, 0)


    #bultos
    bulto1 = Bulto(1001, 50)
    bulto2 = Bulto(1002, 100)
    bulto3 = Bulto(1003, 700)

    #vuelos

    #vuelo
    vuelo = Vuelo(501, "10:50", "13:30", "estambul")

    #vuelo de carga
    vuelo_carga = Vuelo_carga(502, "11:00", "12:39", "Hermosillo", [bulto1, bulto2], 500)

    #vuelo comercial
    vuelo_comercial = Vuelo_comercial(503, "07:00", "10:00", "Guadalajara", [pasajero1, p_frecuente1, p_infrecuente1])

    #vuelo internacional
    vuelo_internacional = Vuelo_internacional(504, "08:00", "18:00", "madrid", [pasajero2, p_frecuente2, p_infrecuente2])

    #vuelo nacional
    vuelo_nacional = Vuelo_nacional(505, "13:00", "16:00", "merida", [pasajero3, p_frecuente3, p_infrecuente3], 4)

    '''probamos metodos de objetos'''

    #lista de todos los objetos para pruebas
    lista_todo = [pasajero1, p_frecuente1,p_infrecuente1, bulto1, vuelo, vuelo_carga,
                  vuelo_comercial, vuelo_internacional, vuelo_nacional]
    #str    '''bien'''
    for i in lista_todo:
        print(i)




