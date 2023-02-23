"""
En este programa crearemos un Menú, y el usuario creara una cuenta y podrá elimarla y pedir
segun lo que necesite

"""
print("Bienvenido a nuestro restaurante Super Food Store ¿En qué podemos servirle? \n")

menuprincipal = int(input("Menú principal: \n 1 Crear registro: \n 2 Leer registro: \n 3 Actualizar registro: \n 4 Eliminar registro: \n 5 Salir del programa: \n"))

while menuprincipal != 5:

    if menuprincipal == 1:
        print("Ingresa tu registro: ")
    elif menuprincipal == 2:
        print("Leyendo registro: ")
    elif menuprincipal == 3:
        print("Actualiza tu registro: ")
    elif menuprincipal == 4:
        print("Eliminar registro: ")
    else:
        print("La opción ingresada no existe, por favor intenta de nuevo.")
    menuprincipal = int(input("Menú principal: \n 1 Crear registro: \n 2 Leer registro: \n 3 Actualizar registro: \n 4 Eliminar registro: \n 5 Salir del programa: \n"))