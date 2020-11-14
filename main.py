response = -1

def print_header():
    print("""
    Universidad Católica Andrés Bello
    Ingeniería Informática
    Sistemas Distribuidos - Práctica 3
    José Andrés Rodríguez Pérez - CI: 27.663.836""")

def print_menu():
    print("""
    ------------- MENU -------------
    Seleccione una opción del menu:
    1. Configuración del servidor
    2. Conectarse al servidor
    0. Salir

    Opcion""", end = ":")

while response != 0:
    print_header()
    print_menu()
    response = int(input())
