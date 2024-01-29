from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class Server:
    def __init__(self):
        self.chamadas = 0
        self.mensagens = []

    def salvar(self, mensagem):
        self.chamadas += 1
        self.mensagens.append(mensagem)
        return True

    def getMensagens(self):
        self.chamadas += 1
        return self.mensagens

    def getIP(self):
        self.chamadas += 1
        return server.server_address[0]
    
    def getChamadas(self):
        self.chamadas += 1
        return self.chamadas

    def getHora(self):
        self.chamadas += 1
        now = datetime.now()
        hora = now.strftime("%Y-%m-%d %H:%M")
        return hora

with SimpleXMLRPCServer(('192.168.11.8', 2801), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    server.register_instance(Server())
    server.serve_forever()