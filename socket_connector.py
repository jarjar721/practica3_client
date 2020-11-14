import socket
import sys
import colorama
import time
import os
import base64

def connect_server(ip, port, username):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (ip, port)
    print("""
    Conectando a {} - Puerto {}""".format(*server_address))
    sock.connect(server_address)

    # Enviando mensaje al servidor
    message = 'helloiam ' + username
    sock.send(bytes(message, 'utf-8'))

    # Esperando la respuesta
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)

        print('received {!r}'.format(data))
        print(colorama.Fore.GREEN + """
        ¡Conexion exitosa!""")
        print(colorama.Style.RESET_ALL)
        break
    
    time.sleep(5)
    return sock



def opensocket_UDP(Client_ip, UDP_port, TCP_socket):
    # Create a UDP socket
    UDPsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Connect the socket to the port where the server is listening
    client_address = (Client_ip, UDP_port)
    print("""
    Abriendo socket UDP a {} en el puerto {}""".format(*client_address))
    UDPsock.bind(client_address)

    # Enviando mensaje al servidor
    message = 'givememsg ' + str(UDP_port)
    TCP_socket.send(bytes(message, 'utf-8'))

    #Esperando la respuesta
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = UDPsock.recv(1024)
        amount_received += len(data)

        realmessage = base64.decodebytes(data).decode('utf_8')
        print('Received ' + realmessage)
        break
    
    time.sleep(5)
    UDPsock.close()
    return realmessage



def get_msglen(sock, ip, port):

    # Enviando mensaje al servidor
    message = 'msglen'
    sock.send(bytes(message, 'utf-8'))

    # Esperando la respuesta
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)

        print('received {!r}'.format(data))
        break
    
    time.sleep(5)
    return



def validate_checksum(sock, ip, port, messageMD5):

    # Enviando mensaje al servidor
    message = 'chkmsg ' + str(messageMD5)
    sock.send(bytes(message, 'utf-8'))

    # Esperando la respuesta
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)

        print('received {!r}'.format(data))
        break
    
    time.sleep(5)
    return



def terminate_TCPsocket(sock):

    # Enviando mensaje al servidor
    message = 'bye'
    sock.send(bytes(message, 'utf-8'))

    # Esperando la respuesta
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)

        print('Received {!r}'.format(data))
        break
    
    time.sleep(5)
    sock.close()
    return



def get_msgUDP(sock, ip, port):

    # Enviando mensaje al servidor
    message = 'msglen'
    sock.send(bytes(message, 'utf-8'))

    # Esperando la respuesta
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)

        print('received {!r}'.format(data))
        break
    
    time.sleep(5)
    return