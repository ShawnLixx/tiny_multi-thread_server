from request import *
import threading
class QueenHandler:
    def __init__(self, requestQueen, responseQueen, max_size):
        self.requestQueen = requestQueen
        self.responseQueen = responseQueen
        self.MAX_SIZE = max_size
    def add(self, request):
        if self.requestQueen.add(request):
            print "Get request %s" % request.operation.string
        else:
            print "Server full"
            response_HTTP = """HTTP/1.1 200 OK

            Server Error"""
            request.connection.sendall(response_HTTP)
            request.connection.close()
                
    def run(self):
        i = 0
        self.lock = threading.RLock()
        while i < self.MAX_SIZE:
            t = threading.Thread(target = self.executeThread, args = (i, ))
            t.setDaemon(True)
            t.start()
            i = i + 1

    def executeThread(self, id):
        while True:
            if self.requestQueen.length() == 0:
                continue
            elif self.lock.acquire():
                if self.requestQueen.length() == 0:
                    continue
                request = self.requestQueen.pop()
                self.lock.release()

            if request.operation.operation == '+':
                request.setAnswer(request.operation.a + request.operation.b)
            elif request.operation.operation == '-':
                request.setAnswer(requset.operation.a - requset.operation.b)
            elif request.operation.operation == '*':
                request.setAnswer(request.operation.a * request.operation.b)
            self.responseQueen.add(request)
            print "Thread " + str(id) + " response " + str(request.getAnswer())
            response_HTTP = """HTTP/1.1 200 OK

            """ + str(request.getAnswer())
            request.connection.sendall(response_HTTP)
            request.connection.close()
