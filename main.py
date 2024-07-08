
from funciones_movies import *

# -------------------------------------------------------------------------------------------------------


seguir = "s"
flag_cargar_archivo = False
flag_cargar_rating = False
flag_cargar_genero = False

movies = []
while seguir == "s":

    match menu():
        case 1:
            if flag_cargar_archivo == False:
                nombre_archivo = input(
                    "ingrese el nombre del archivo de peliculas que desea procesar: ")

                try:
                    with open(get_path_actual(nombre_archivo), "r", encoding="utf-8")as archivo:

                        movies = []
                        # strip corta al inicio y final / split divide la cadena en elementos
                        encabezado = archivo.readline().strip("\n").split(",")

                        for linea in archivo.readlines():
                            movie = {}
                            linea = linea.strip("\n").split(",")
                            # packing desempaquetado de lista tiene que tener igual numero de varibles
                            id, titulo, genero, rating = linea
                            movie["id"] = int(id)
                            movie["titulo"] = titulo
                            movie["genero"] = genero
                            movie["rating"] = float(rating)
                            print(id,  titulo, genero, rating)
                            movies.append(movie)
                    print("archivo cargado sastifactoriamente")

                    flag_cargar_archivo = True

                except FileNotFoundError:
                    print("el archivo no fue encontrado")

            else:
                print("el archivo ya fue cargado anteriormente intente otra opcion")
        case 2:
            if flag_cargar_archivo:
                mostrar_movies(movies)
            else:
                print("primero deberas cargar el archivo")
        case 3:
            if flag_cargar_archivo:
                lista_mapeada = mapear_movies(rating_movie, 1, 10, movies)
                mostrar_movies_rating(lista_mapeada)
                flag_cargar_rating = True
            else:
                print("primero deberas cargar el archivo")
        case 4:
            if flag_cargar_archivo:
                genero_data = ["drama", "comedia", "accion", "terror"]
                lista_mapeada = mapear_movies_genero(
                    genero_movie, movies, genero_data, 0, 3)
                mostrar_movies_generos(lista_mapeada)
                flag_cargar_genero = True
            else:
                print("primero deberas cargar el archivo")

        case 5:
            if flag_cargar_rating and flag_cargar_genero:
                genero_deseado = input(
                    "ingrese el genero deseaso(drama, comedia, accion o terror)")
                lista_filtrada = filter_movie(
                    filtrar_genero, movies, genero_deseado)
                mostrar_movies(lista_filtrada)

                with open(get_path_actual("comedias.csv"), "w", encoding="utf-8") as archivo:
                    encabezado = ",".join(
                        list(lista_filtrada[0].keys())) + "\n"
                    archivo.write(encabezado)
                    for element in lista_filtrada:
                        values = list(element.values())
                        l = []
                        for value in values:
                            if isinstance(value, int):
                                l.append(str(value))
                            elif isinstance(value, float):
                                l.append(str(value))
                            else:
                                l.append(value)

                        linea = ",".join(l) + "\n"
                        archivo.write(linea)
            else:
                print("primero deberas asignar rating y genero")
        case 6:

            if flag_cargar_rating and flag_cargar_genero:
                ordenar_alumnos_criterio(movies, "genero", "rating", False)
                mostrar_movies(movies)

        case 7:
            rating_maximo = mejor_rating(movies)
            indice = buscar_float_in_lista(movies, rating_maximo)
            mostrar_movie_rating(movie[indice])
        case 8:
            with open(get_path_actual("movies.json"), "w", encoding="utf-8") as archivo:
                json.dump(movies, archivo, indent=4)

        case "9":
            if pedir_confirmacion("desea continuar: s/n") == False:
                seguir = "n"
            continue
    pausar()

print("Fin del programa")

pausar()
