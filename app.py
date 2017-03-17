from server import Server
from queenHandler import QueenHandler
from request import Queen

requestQueen = Queen()
responseQueen = Queen()
queenHandler = QueenHandler(requestQueen, responseQueen, 10)
server = Server("", 8888)
server.run(queenHandler)
