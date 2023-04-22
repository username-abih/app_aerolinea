from datetime import datetime


# métodos de validación para reutilización


def validar_str(dato):
    if not isinstance(dato, str) and dato is not None:
        raise ValueError("el valor {} debe ser un str".format(dato))


def validar_int(dato):
    if not isinstance(dato, int) and dato is not None:
        raise ValueError("el valor {} debe ser un numero entero".format(dato))


def validar_float(dato):
    if not isinstance(dato, float) and not isinstance(dato, int) and dato is not None:
        raise ValueError("el valor {} debe ser un numero flotante".format(dato))


def validar_lista(dato):
    if not isinstance(dato, list) and dato is not None:
        raise ValueError("el valor {} debe ser una lista".format(dato))


def validar_bool(dato):
    if not isinstance(dato, bool) and dato is not None:
        raise ValueError("el valor {} debe ser un booleano".format(dato))


def validar_fecha_dd_mm_yyyy(dato):
    if dato is not None:

        try:
            datetime.strptime(dato, "%d-%m-%Y")
        except:
            raise ValueError("el valor fecha no esta en formato dia-mes-año (00-00-0000) (str)")


def validar_hora_hh_mm(dato):
    if dato is not None:
        try:
            datetime.strptime(dato, "%H:%M")
        except:
            raise ValueError("el valor Hora no esta en formato 24:00")


# pasajeros y subsecuentes
class Pasajero():
    """Clase Pasajero con los atributos id, nombre y precio billete,
    con el método mostrar precio

    ARGS
    -Id: número unico e irrepetible para identificar al pasajero
    -Nombre: nombre del pasajero
    -precio billete: precio total del billete
    """

    def __init__(self, id=None, nombre=None, precio_billete=None):
        validar_int(id)
        self.__id = id
        validar_str(nombre)
        self.__nombre = nombre
        validar_float(precio_billete)
        self.__precio_billete = precio_billete

    # función mostrar puntos que muestra los puntos actuales del pasajero
    def mostrar_precio(self):
        return print("""el precio del billete del cliente {} 
        con ID {}
        es de {} $""".format(self.__nombre, self.__id, self.__precio_billete))

    # setter y getters
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, nuevo_id):
        validar_int(nuevo_id)
        self.__id = nuevo_id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        validar_str(nuevo_nombre)
        self.__nombre = nuevo_nombre

    @property
    def precio_billete(self):
        return self.__precio_billete

    @precio_billete.setter
    def precio_billete(self, nuevo_precio_billete):
        validar_float(nuevo_precio_billete)
        self.__precio_billete = nuevo_precio_billete

    def __str__(self):
        return '''
        -ID:             {}
        -NOMBRE:         {}
        -PRECIO BILLETE: {}'''.format(self.__id, self.__nombre, self.__precio_billete)


class Pasajero_frecuente(Pasajero):
    """Clase Pasajero frecuente con los atributos id, nombre, precio billete,
    y cantidad de puntos, con el método mostrar precio heredado del padre y
    el metodo mostrar puntos

    ARGS
    -Id: número unico e irrepetible para identificar al pasajero
    -Nombre: nombre del pasajero
    -precio billete: precio total del billete
    -cantidad puntos: cantidad de puntos recolectados por los vuelos del cliente
    """

    def __init__(self, id=None, nombre=None, precio_billete=None,
                 cantidad_puntos=0):
        super().__init__(id, nombre, precio_billete)
        validar_float(cantidad_puntos)
        self.__cantidad_puntos = cantidad_puntos

    def mostrar_precio(self):
        return super().mostrar_precio()

    def mostrar_puntos(self):
        print("""los puntos del pasajero {}
        con ID {}
        son {}""".format(self.nombre, self.id, self.__cantidad_puntos))

    # getter y setter
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
    """Clase Pasajero frecuente con los atributos id, nombre, precio billete,
    y cantidad de puntos, con el método mostrar precio heredado del padre y
    el metodo mostrar puntos.

    ARGS
    -Id: número unico e irrepetible para identificar al pasajero
    -Nombre: nombre del pasajero
    -precio billete: precio total del billete
    -cantidad puntos: cantidad de puntos recolectados por los vuelos del cliente
    """

    def __init__(self, id=None, nombre=None, precio_billete=None,
                 cantidad_puntos=0):
        super().__init__(id, nombre, precio_billete)
        validar_float(cantidad_puntos)
        self.__cantidad_puntos = cantidad_puntos

    def mostrar_precio(self):
        return super().mostrar_precio()

    def mostrar_puntos(self):
        print("""los puntos del pasajero {}
        con ID {}
        son {}""".format(self.nombre, self.id, self.__cantidad_puntos))


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
    """Bulto que contiene los atributos ID y Peso.

    ARGS:
    -ID: numero unico e irrepetible para identificar al bulto
    -Peso: peso total del bulto
    """

    def __init__(self, id=None, peso=None):
        validar_int(id)
        self.__id = id
        validar_float(peso)
        self.__peso = peso

    # setter y getters
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, nuevo_id):
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
    """Clase Vuelo con los atributos número, hora de salida, hora de llegada y destino.

    ARGS:
    -número: número de serie unico e irrepetible del vuelo
    -hora de salida: hora de salida del vuelo
    -hora de llegada: hora de llegada del vuelo
    -destino: destino del vuelo
    """

    def __init__(self, numero=None, hora_salida=None, hora_llegada=None,
                 destino=None):
        validar_int(numero)
        self.__numero = numero
        validar_hora_hh_mm(hora_salida)
        self.__hora_salida = hora_salida
        validar_hora_hh_mm(hora_llegada)
        self.__hora_llegada = hora_llegada
        validar_str(destino)
        self.__destino = destino

    # getter y setters
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
    """Clase Vuelo de carga con los atributos número, hora de salida, hora de llegada, destino,
    lista de carga y peso máximo, contiene los métodos agregar carga, mostrar carga y quitar carga.

    ARGS:
    -número: número de serie unico e irrepetible del vuelo
    -hora de salida: hora de salida del vuelo
    -hora de llegada: hora de llegada del vuelo
    -destino: destino del vuelo
    -lista carga: lista con todos los bultos que llevara el vuelo
    -peso máximo: peso máximo permitido por el vuelo
    """

    def __init__(self, numero=None, hora_salida=None, hora_llegada=None,
                 destino=None, lista_carga=[], peso_maximo=None):
        super().__init__(numero, hora_salida, hora_llegada, destino)
        validar_lista(lista_carga)
        self.__lista_carga = lista_carga
        validar_float(peso_maximo)
        self.__peso_maximo = peso_maximo
        self.__peso_actual = 0
        for carga in lista_carga:
            self.__peso_actual += carga.peso

    # método para agregar carga nueva a la lista de carga
    def agregar_carga(self, nueva_carga):
        if (self.__peso_actual + nueva_carga.peso) > self.__peso_maximo:
            print('''Carga máxima excedida, no se ha añadido el bulto con ID {}
>>> La carga excede por {} KG'''.format(nueva_carga.id, self.__peso_actual + nueva_carga.peso - self.__peso_maximo))

        else:
            self.__lista_carga.append(nueva_carga)
            self.__peso_actual += nueva_carga.peso
            print("""Se ha agregado el bulto con ID {}
>>> La carga actual es de {} / {} Kg""".format(nueva_carga.id, self.__peso_actual, self.__peso_maximo))

    # método para mostrar todos los str de los objetos que contiene la lista de carga
    def mostrar_carga(self):
        for carga in self.__lista_carga:
            print(carga)

    # método para quitar carga de la lista de carga
    def quitar_carga(self, carga_quitar):
        pass
        self.__lista_carga.remove(carga_quitar)
        self.__peso_actual -= carga_quitar.peso
        print("""se ha quitado el bulto con ID {}
>>> La carga actual es de {} / {} Kg""".format(carga_quitar.id, self.__peso_actual, self.__peso_maximo))

    # getter y setters
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
        -Cantidad de artículos a cargar: {}
        -Peso máximo: {}'''.format(len(self.__lista_carga),
                                   self.__peso_maximo)


class Vuelo_comercial(Vuelo):
    """Clase Vuelo comercial con los atributos número, hora de salida, hora de llegada, destino y lista de pasajeros,
    cón los métodos agregar pasajero, mostrar lista de pasajeros y quitar pasajero

    ARGS:
    -número: número de serie unico e irrepetible del vuelo
    -hora de salida: hora de salida del vuelo
    -hora de llegada: hora de llegada del vuelo
    -destino: destino del vuelo
    -lista de pasajeros: lista de pasajeros que ira en el vuelo"""

    def __init__(self, numero=None, hora_salida=None, hora_llegada=None,
                 destino=None, lista_pasajeros=[]):
        super().__init__(numero, hora_salida, hora_llegada, destino)
        validar_lista(lista_pasajeros)
        self.__lista_pasajeros = lista_pasajeros

    # método para agregar pasajero a la lista de pasajeros
    def agregar_pasajero(self, pasajero):
        self.__lista_pasajeros.append(pasajero)
        print("""se ha añadido el pasajero {} a el vuelo {}""".format(pasajero.nombre, self.numero ))

    # método para mostrar la lista de pasajeros
    def mostrar_lista_pasajeros(self):
        for pasajero in self.__lista_pasajeros:
            print(pasajero)

    # quita un pasajero de la lista de pasajeros del vuelo
    def quitar_pasajero(self, pasajero_quitar):
        self.__lista_pasajeros.remove(pasajero_quitar)
        print("""se ha quitado el pasajero {} a el vuelo {}""".format(pasajero_quitar.id, self.numero))

    # getter y setters
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
    """Clase Vuelo internacional con los atributos número, hora de salida, hora de llegada, destino
    lista de pasajeros y escalas.
    Con el método mostrar escalas, agregar escala y quitar escala

    ARGS:
    -número: número de serie unico e irrepetible del vuelo
    -hora de salida: hora de salida del vuelo
    -hora de llegada: hora de llegada del vuelo
    -destino: destino del vuelo
    -lista de pasajeros: lista de pasajeros que ira en el vuelo
    -Escalas: lista de lugares donde aterrizara el avion y volverá a salir"""

    def __init__(self, numero=None, hora_salida=None, hora_llegada=None,
                 destino=None, lista_pasajeros=[], escalas=[]):
        super().__init__(numero, hora_salida, hora_llegada,
                         destino, lista_pasajeros)
        validar_lista(escalas)
        self.__escalas = escalas

    # muestra las escalas que realizara el vuelo
    def mostrar_escalas(self):
        print("las escalas que realizara el vuelo {} con destino {} son:".format(self.numero, self.destino))
        for escala in self.__escalas:
            print("     -{}".format(escala))

    # agregar escala al vuelo
    def agregar_escala(self, escala_nueva):
        self.__escalas.append(escala_nueva)
        print("""se ha agregado la escala {} al vuelo {}""".format(escala_nueva, self.numero))

    # quita escala al vuelo
    def quitar_escala(self, escala):
        self.__escalas.remove(escala)
        print("""se ha quitado la escala {} al vuelo {}""".format(escala, self.numero))

    # getter y setters
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
    """Clase Vuelo nacional con los atributos número, hora de salida, hora de llegada, destino
    lista de pasajeros y número minimo de pasajeros.
    Con el metodo Puede volar

    ARGS:
    -número: número de serie unico e irrepetible del vuelo
    -hora de salida: hora de salida del vuelo
    -hora de llegada: hora de llegada del vuelo
    -destino: destino del vuelo
    -lista de pasajeros: lista de pasajeros que ira en el vuelo
    -número minimo de pasajeros: número minimo de pasajeros para que costee el vuelo"""

    def __init__(self, numero=None, hora_salida=None, hora_llegada=None,
                 destino=None, lista_pasajeros=[], num_minimo_pasajeros=None):
        super().__init__(numero, hora_salida, hora_llegada,
                         destino, lista_pasajeros)
        validar_int(num_minimo_pasajeros)
        self.__num_minimo_pasajeros = num_minimo_pasajeros

    # método para corroborar que el vuelo tenga el minimo de pasajeros y sea redituable que vuele
    def puede_volar(self):
        if len(self.lista_pasajeros) >= self.__num_minimo_pasajeros:
            return True
        else:
            return False

    # getter y setter
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
    # creamos objetos
    # pasajeros
    pasajero1 = Pasajero(1001, "pasajero1", 1000)
    pasajero2 = Pasajero(1002, "pasajero2", 1000)
    pasajero3 = Pasajero(1003, "pasajero3", 1000)

    # pasajeros frecuentes
    p_frecuente1 = Pasajero_frecuente(1004, "frecuente1", 1000, 100)
    p_frecuente2 = Pasajero_frecuente(1005, "frecuente2", 1000, 200)
    p_frecuente3 = Pasajero_frecuente(1006, "frecuente3", 1000, 200)

    # pasajeros infrecuentes
    p_infrecuente1 = Pasajero_no_frecuente(1006, "pasajero_no_f1", 1000, 0)
    p_infrecuente2 = Pasajero_no_frecuente(1007, "pasajero_no_f2", 1000, 0)
    p_infrecuente3 = Pasajero_no_frecuente(1008, "pasajero_no_f3", 1000, 0)

    # bultos
    bulto1 = Bulto(1001, 50)
    bulto2 = Bulto(1002, 100)
    bulto3 = Bulto(1003, 700)

    # vuelos

    # vuelo
    vuelo = Vuelo(501, "10:50", "13:30", "Estambul")

    # vuelo de carga
    vuelo_carga = Vuelo_carga(502, "11:00", "12:39", "Hermosillo", [bulto1, bulto2], 500)

    # vuelo comercial
    vuelo_comercial = Vuelo_comercial(503, "07:00", "10:00", "Guadalajara", [pasajero1, p_frecuente1, p_infrecuente1])

    # vuelo internacional
    vuelo_internacional = Vuelo_internacional(504, "08:00", "18:00", "Madrid",
                            [pasajero1, p_frecuente1, p_infrecuente1], ["Barcelona", "Francia"])

    # vuelo nacional
    vuelo_nacional = Vuelo_nacional(505, "13:00", "16:00", "merida", [pasajero3, p_frecuente3, p_infrecuente3], 4)

    '''probamos métodos de objetos'''

    # lista de todos los objetos para pruebas
    lista_todo = [pasajero1, p_frecuente1, p_infrecuente1, bulto1, vuelo, vuelo_carga,
                  vuelo_comercial, vuelo_internacional, vuelo_nacional]
    # str
    for met_str in lista_todo:
        print(met_str)

    # pasajero, frecuente y no frecuente
    pasajero1.mostrar_precio()
    p_frecuente1.mostrar_precio()
    p_infrecuente1.mostrar_precio()

    p_frecuente1.mostrar_puntos()
    p_infrecuente1.mostrar_puntos()

    # vuelo de carga
    vuelo_carga.mostrar_carga()
    vuelo_carga.agregar_carga(bulto3)
    vuelo_carga.quitar_carga(bulto1)
    vuelo_carga.mostrar_carga()

    # Vuelo comercial
    print("_____")
    vuelo_comercial.agregar_pasajero(pasajero2)
    vuelo_comercial.mostrar_lista_pasajeros()
    print("____")
    vuelo_comercial.quitar_pasajero(pasajero1)
    vuelo_comercial.mostrar_lista_pasajeros()

    #vuelo internacional
    print("____")
    vuelo_internacional.agregar_escala("Estambul")
    vuelo_internacional.mostrar_escalas()
    vuelo_internacional.quitar_escala("Francia")
    vuelo_internacional.mostrar_escalas()

    # Vuelo Nacional
    print("____")
    print(vuelo_nacional.puede_volar())