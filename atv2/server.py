from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime

RPC_PORT = 3000
RPC_URL = 'localhost'

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/', '/hora')

with SimpleXMLRPCServer((RPC_URL, RPC_PORT), requestHandler=RequestHandler) as server:
    def get_hora():
        now = datetime.now()
        hora_atual = now.strftime("%H:%M:%S")
        return hora_atual

    server.register_function(get_hora, 'get_hora')

    print(f"\n🚀 Iniciando servidor RPC em {RPC_URL}:{RPC_PORT}")
    server.serve_forever()