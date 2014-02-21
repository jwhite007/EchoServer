#! /usr/bin/env python

import socket

server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)

address = ('127.0.0.1', 50000)
try:
    server_socket.bind(address)
    server_socket.listen(1)

    while True:
        conn, addr = server_socket.accept()  # this blocks until a client connects
        rec_message = conn.recv(32)
        conn.shutdown(socket.SHUT_RD)
        conn.sendall(rec_message)
        conn.shutdown(socket.SHUT_WR)
        conn.close()
finally:
    server_socket.close()
