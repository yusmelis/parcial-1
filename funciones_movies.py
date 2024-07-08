# -----------------------------Funciones de Menu----------------------------


def pedir_confirmacion(mensaje: str) -> bool:
    """le consulta al usuario si desea continuar

    Args:
        mensaje (str): _description_

    Returns:
        bool: True si la respuesta es afirmativa /false caso contratio
    """
    rta = input(mensaje).lower
    return rta == 's'


def limpiar_pantalla():
    """borra informacion antigua en la consola para presentar nueva
    """
    import os
    os.system("cls")


def pausar():
    """_el programa es pausado hasta presionar una tecla
    """
    import os
    os.system("pause")


def menu() -> int:
    """muestra un menu de opciones a elegir

    Returns:
        int: devuelve la opcion elegida o un error
    """

    limpiar_pantalla()
    print(f"{'Menu de Opciones':^50s}")

    print("1- Cargar Archivo .CSV")
    print("2- Imprimir lista de Peliculas")
    print("3- Asignar rating")
    print("4- asigna genero")
    print("5- filtrar por genero")
    print("6 -ordernar por genero y rating")
    print("7 -imprimir mejor rating")

    try:
        opcion = (pedir_numero(1, 9, 3))
        return opcion
    except ValueError as e:
        print(e)
        exit()


def pedir_numero(l_inf: int, l_sup: int, veces: int) -> int:
    """pide un numero entero por consola validando que este dentro de un limite con una cantidad de oportunidades especificadas

    Args:
        l_inf (int):limite inferior del rango
        l_sup (int): limites superior del rango
        veces (int): cantidad de oportunidades para ingresar numero valido

    Raises:
        ValueError: si exceden las oprtunidades sin ingresar una cifra valida

    Returns:
        numero ingresado si es validado correctamente
    """

    while veces > 0:

        numero = (input(f"ingrese un numero entre {l_inf} y {l_sup} :  "))
        if not numero.isdigit() or int(numero) < l_inf or int(numero) > l_sup:
            print("ingreso errado")
            veces -= 1

        else:
            return int(numero)
    raise ValueError("demasiados intento fallido se cerrara el programa")
# -----------------------------Carga de Archivo csv----------------------------


def get_path_actual(nombre_archivo):
    """realiza una union entre el nombre del archivo proporcionado  y la ruta del script de trabajo actual

    Args:
        nombre_archivo (str):  nombre del archivo

    Returns:
        _type_: la direccion de acceso al archivo
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

# ------------------------Imprmir lista---------------------------------------


def mostrar_movies(lista_movies: list):
    """muestra por  consola todos loselementos de la lista con sus respectivos atributos

    Args:
        lista_movie (list): lista de elementos a mostrar
    """
    TAM = len(lista_movies)
    print("     ***Listado de movies*****   ")
    print("Id          Titulo                 Genero                  Rating")
    print("----------------------------------------------")
    for i in range(TAM):
        mostrar_movie(lista_movies[i])


def mostrar_movie(movie: dict):
    """muestra por consola los atributos de movie

    Args:
        movie (dict): diccionario  de una movie
    """

    print(f"{movie['id']} {movie['titulo']:>30}   {
          movie['genero']:12}             {movie['rating']:.1f}")


def mapear_movies(mapeadora, desde, hasta, lista: list) -> list:
    """  mapea una lista de movies para crear en una nueva  lista con elementos que muestraen informacion especifica determinada por la funcion mapeadora
    Args:
        lista (list):lista de diccionarios con la informacion de los movies
        mapeadora (function):  Función que toma un diccionario  como argumento y devuelve un nuevo objeto con informacion indicada del empleado
    Returns:
        list: lista mapeada
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append(mapeadora(el, desde, hasta))
    return lista_retorno


def rating_movie(movie: dict, desde, hasta):
    """carga con un numero flotantante de 1 decimal el rating de un diccionario de forma aleatoria"

    Args:
        movie (dict): _dicionario a ser cargado el rating
        desde (_type_):numero inicial del rango dentro dl cual se desea cargar
        hasta (bool):numero final dentro del rango del cual se desea cagar

    Returns:
        el diccionario mapeado con el titulo y rating
    """
    from random import randint
    numero = randint(int(desde*10), int(hasta*10))
    numero_flotante = float(numero/10)
    movie["rating"] = numero_flotante
    return {"titulo": movie["titulo"], "rating": movie["rating"]}


def mostrar_movie_rating(movie: dict):
    """muestra por consola el rating de cada pelicula

    Args:
        movie (dict): diccionario  de una movie
    """

    print(f"{movie['titulo']:>30}        {movie['rating']:.1f}")


def mostrar_movies_rating(lista_movies: list):
    """muestra por  consola todos los elementos de las movies con su rating

    Args:
        lista_movie (list): lista de elementos a mostrar
    """
    TAM = len(lista_movies)
    print("     ***Listado de movies*****   ")
    print("Titulo                       Rating")
    print("----------------------------------------------")
    for i in range(TAM):
        mostrar_movie_rating(lista_movies[i])


def genero_movie(movie: dict,  lista_posibles_valores, desde, hasta):
    """carga con informacion del genero el diccionario 

    Args:
        movie (dict): diccionario de la movie
        lista_posibles_valores (_type_):lista con  data de informacion a cargar
                desde (int):numero inicial del indice de la lista de los posible s valores a cargar
        hasta (int):numero final del indice de la lista de los posible s valores a cargar


    Returns:
        _diccionario con informacion del genero de cada pelicula
    """

    from random import randint
    movie["genero"] = lista_posibles_valores[randint(desde, hasta)]
    return {"titulo": movie["titulo"], "genero": movie["genero"]}


def mapear_movies_genero(mapeadora, lista: list, lista_posibles_valores, desde, hasta) -> list:
    """  mapea una lista de movies para crear en una nueva  lista con elementos que muestraen informacion especifica determinada por la funcion mapeadora
    Args:
        lista (list):lista de diccionarios con la informacion de los movies
        mapeadora (function):  Función que toma un diccionario  como argumento y devuelve un nuevo objeto con informacion indicada del empleado
        desde (int):numero inicial del indice de la lista de los posible s valores a cargar
        hasta (int):numero final del indice de la lista de los posible s valores a cargar

    Returns:
        list: lista mapeada
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append(
            mapeadora(el, lista_posibles_valores, desde, hasta))
    return lista_retorno


def mostrar_movie_genero(movie: dict):
    """muestra por consola el rating de cada pelicula

    Args:
        movie (dict): diccionario  de una movie
    """

    print(f"{movie['titulo']:>30}        {movie['genero']:12} ")


def mostrar_movies_generos(lista_movies: list):
    """muestra por  consola todos los elementos de las movies con su rating

    Args:
        lista_movie (list): lista de elementos a mostrar
    """
    TAM = len(lista_movies)
    print("     ***Listado de movies*****   ")
    print("Titulo                       genero")
    print("----------------------------------------------")
    for i in range(TAM):
        mostrar_movie_genero(lista_movies[i])


def filter_movie(filtradora, lista: list, criterio_filtro_genero) -> list:
    """
    filtra una lista de empleados para extraer solo aquellos que pertenecen a los que defina la funcion filtradora
    Args:
        lista (list):lista de diccionarios con la informacion de los empleados
        filtradora (function):  Función que toma un diccionario  como argumento y devuelve un valor booleano segun si cumple o no con un criterio
    """

    lista_filtrada = []
    for elemento in lista:
        # funcion filtradora que me diga si la condicion se cumple o no para que agregue hago una f
        if filtradora(elemento, criterio_filtro_genero):
            lista_filtrada. append(elemento)
    return lista_filtrada


def filtrar_genero(movie: dict, criterio_filtro_genero) -> bool:
    """evalua si un diccionario cumple con tener por genero el indicado en elcriterio

    Args:
        movie (dict)diccionario con la informacion pertinente a la movie

    Returns:
        bool: verdader si es el mismo genero del criterio / false de lo contrario
    """
    return movie["genero"] == criterio_filtro_genero


def swap_lista(lista: list, i: int, j: int) -> None:
    """intercambia dos elementos de una lista

    Args:
        lista (list): lista con elementos a intercambiar
        i (int): indice del primer elemento
        j (int): indice del segundo elemento a intercambiar
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def ordenar_alumnos_criterio(movies: list, criterio_1: str, criterio_2: str, ascendete) -> None:
    """   ordena en forma ascedente o descendente y por dos criterio

    Args:
        movies (list):lista de alumno
        criterio_1 (_type_):primer criterio de ordenamiento preferiblemente de agrupamiento
        criterio_2 (_type_): segundo criterior de orden
        ascendete (_type_): True en forma creciente/ false de lo contrario
    """
    TAM = len(movies)
    for i in range(TAM-1):
        for j in range(i+1, TAM):
            if movies[i][criterio_1] == movies[j][criterio_1]:
                if movies[i][criterio_2] > movies[j][criterio_2]:
                    swap_lista(movies, i, j)
            elif movies[i][criterio_1] > movies[j][criterio_1]:
                swap_lista(movies, i, j)


def mejor_rating(movies):

    flag_maximo = True
    mejor_rating = 0
    for i in range(len(movies)):
        if flag_maximo:
            mejor_rating = movies[i]["rating"]
            flag_maximo == False
        else:
            if mejor_rating < movies[i]["rating"]:
                mejor_rating = movies[i]["rating"]

            else:
                continue

    return mejor_rating


def buscar_float_in_lista(lista: list, target: int) -> int:
    """ busca un numero entero en la lista deolviendo el indice de la posicion



    Args:
        lista (list): la lista donde se bucara el entero
        target (int):el numero entero que se desea encontrar

    Raises:
        ValueError: si no es encontrado el valor suministrado

    Returns:
        int: el indice del entero donde se encuentra en la lista
    """

    for i in range(len(lista)):
        if lista[i]["rating"] == target:
            return i
    raise ValueError(f"{target} no esta en la lista")

    from random import randint
    numero = randint(int(desde*10), int(hasta*10))
    numero_flotante = float(numero/10)
    movie["rating"] = numero_flotante
    return {"titulo": movie["titulo"], "rating": movie["rating"]}
