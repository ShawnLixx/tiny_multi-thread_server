import socket
import threading
from operation import Operation
from request import *

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self, queenHandler):
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind((self.host, self.port))
        listen_socket.listen(1)
        print 'Serving HTTP on port %s ...' % self.port
        t = threading.Thread(target = queenHandler.run)
        t.setDaemon(True)
        t.start()
        while True:
            client_connection, client_address = listen_socket.accept()
            request = client_connection.recv(1024)
            urlString = request.split()[1]
            paras = self.urlParaDecode(urlString)
            operation = Operation(paras['operation'])
            request = Request(client_connection, operation)
            queenHandler.add(request)

    def urlParaDecode(self, url):
        paras = {}
        if url.find("?") == -1:
            return paras
        urlcp = url[url.find('?') + 1:]
        while True:
            key = urlcp[0: url.find("=") - 2]
            if urlcp.find("&") != -1:
                value = urlcp[urlcp.find("=") + 1: urlcp.find("&")]
                paras[key] = value
                urlcp = urlcp[urlcp.find("&") + 1]
            else:
                value = urlcp[urlcp.find("=") + 1:]
                paras[key] = value
                break

        return paras
