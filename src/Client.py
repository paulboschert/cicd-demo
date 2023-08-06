#!/usr/bin/env python3

import socket

class Client:
    def __init__(self, host=socket.gethostbyname('127.0.0.1'), port=54004):
        self.socket = socket.socket()
        self.socket.connect(('', port))

    def close(self):
        self.socket.close()

    '''
    Send two numbers to be added to Server
    Numbers are sent as strings and response 
    is the summation.
    '''
    def get_sum(self, a, b):
        message = str(a) + " " + str(b)
        self.socket.send(message.encode())

        response = self.socket.recv(1024).decode()
        return response
