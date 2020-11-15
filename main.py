import os
import colorama
import time
import socket
import hashlib

import socket_connector

connected = False

#ip = "127.0.0.1" # Default IP (Local)
ip = "10.2.126.2" # Default IP (Server UCAB)
port = 19876 # Defaul Port

Client_ip = socket.gethostbyname(socket.gethostname())
UDP_port = 9876 #UDP Port

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
UDPsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

realmessage = ""
encoded_message = ""


def print_header():
    print("""
    Universidad Católica Andrés Bello
    Ingeniería Informática
    Sistemas Distribuidos - Práctica 3
    José Andrés Rodríguez Pérez - CI: 27.663.836""")



def server_settings():
    print(f"""
    La configuración actual de conexión al servidor es:
    - Dirección IP Servidor: {ip}
    - Puerto Servidor: {port}
    - Dirección IP Cliente: {Client_ip}
    - Puerto UDP Cliente: {UDP_port} """)



def change_server_settings():
    global ip, port, UDP_port

    print("""
    Configuración nueva de conexión al servidor:
    - Dirección IP Servidor""", end = ": ")
    ip = input()
    print("""
    - Puerto Servidor""", end = ": ")
    port = int(input())
    print("""
    - Puerto UDP Cliente""", end = ": ")
    UDP_port = int(input())

    print(colorama.Fore.GREEN + """
    ¡Configuracion guardada!""")
    print(colorama.Style.RESET_ALL)
    time.sleep(5)

    os.system("cls")
    print_menu1()




def start():
    global ip, port, sock, Client_ip, connected
    global UDP_port, realmessage, encoded_message

    print_header()
    print("""
    ------------- MENU -------------
    Seleccione una opción del menu:
    1. Configurar conexión del servidor
    2. Conectarse al servidor
    3. Obtener tamaño del mensaje
    4- Solicitar mensaje en puerto UDP
    5. Validar contenido del mensaje
    6. Desconectarse del servidor
    0. Salir

    Opcion""", end = ": ")
    response = int(input())

    if response == 1:
        os.system("cls")
        print_header()
        print_menu1()
    elif response == 2:
        os.system("cls")
        print_header()
        sock = print_menu_autenticacion()
        os.system("cls")
        start()
    elif response == 3:
        if connected == True:
            socket_connector.get_msglen(sock, ip, port)
            os.system("cls")
            start()
        else:
            print(colorama.Fore.RED + """
            ¡No se ha conectado al servidor con un usuario!""")
            print(colorama.Style.RESET_ALL)
            time.sleep(5)
            os.system("cls")
            start() 
    elif response == 4:
        if connected == True:
            encoded_message = socket_connector.opensocket_UDP(Client_ip, UDP_port, sock)
            os.system("cls")
            start()
        else:
            print(colorama.Fore.RED + """
            ¡No se ha conectado al servidor con un usuario!""")
            print(colorama.Style.RESET_ALL)
            time.sleep(5)
            os.system("cls")
            start()
    elif response == 5:
        if connected == True:
            message = encoded_message.encode()
            messageMD5 = hashlib.md5(message).hexdigest()
            socket_connector.validate_checksum(sock, ip, port, messageMD5)
            os.system("cls")
            os.system("cls")
            start()
        else:
            print(colorama.Fore.RED + """
            ¡No se ha conectado al servidor con un usuario!""")
            print(colorama.Style.RESET_ALL)
            time.sleep(5)
            os.system("cls")
            start()
    elif response == 6:
        if connected == True:
            socket_connector.terminate_TCPsocket(sock)
            os.system("cls")
            start()
        else:
            print(colorama.Fore.RED + """
            ¡No se ha conectado al servidor con un usuario!""")
            print(colorama.Style.RESET_ALL)
            time.sleep(5)
            os.system("cls")
            start()
    else:
        print("""
        ¡Gracias por participar!""")



def print_menu1():

    print("""
    ------- 1. CONFIGURACION DEL SERVIDOR ------- """)
    server_settings()
    print("""
    Seleccione una opción del menu:
    1. Configurar paramatros de conexión
    0. Regresar

    Opcion""", end = ": ")

    response = int(input())
    if response == 0:
        os.system("cls")
        start()
    elif response == 1:
        change_server_settings()



def print_menu_autenticacion():
    global ip, port, connected

    print("""
    ------- 2. CONECTARSE AL SERVIDOR ------- """)
    server_settings()
    print("""
    **INICIAR SESIÓN**
    Introduzca su nombre de usuario para acceder al servidor
    (Introduzca 0 para regresar)

    USERNAME""", end = ": ")
    response = input()

    sock, connected = socket_connector.connect_server(connected, ip, port, response)
    return sock

start()