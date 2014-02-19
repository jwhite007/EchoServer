#! /usr/bin/env python

import socket
import sys


def echo_me(message):
    # message = sys.argv[1]

    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)

    client_socket.connect(('127.0.0.1', 50000))
    client_socket.sendall(message)
    client_socket.shutdown(socket.SHUT_WR)

    buffersize = 32
    serv_message = ''
    done = False

    while not done:
        serv_message_part = client_socket.recv(buffersize)
        if len(serv_message_part) < buffersize:
            done = True
            client_socket.close()
        serv_message += serv_message_part

    return "ECHO: " + serv_message

if __name__ == '__main__':
    """Documentaion and tests"""
    print(echo_me(sys.argv[1]))
