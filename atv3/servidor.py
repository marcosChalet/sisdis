from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('192.168.11.8', 2801), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    mensagens = []

    def salvar(mensagem):
        mensagens.append(mensagem)
        return True

    def getMensagens():
        return mensagens

    def getIP():
        return server.server_address[0]

    def getHora():
        now = datetime.now()
        hora = now.strftime("%Y-%m-%d %H:%M")
        return hora

    server.register_function(salvar, 'salvar')
    server.register_function(getMensagens, 'getMensagens')
    server.register_function(getIP, 'getIP')
    server.register_function(getHora, 'getHora')

    server.serve_forever()