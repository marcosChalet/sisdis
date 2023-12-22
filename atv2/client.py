from xmlrpc.client import ServerProxy


local_server = ServerProxy('http://localhost:3000/')
remote_server = ServerProxy('http://172.164.23.12:3000/')

tipo_chamada = int(input("Chamda local [1]\nChamada remota [2]\n\n-> "))

if tipo_chamada == 1:
    print("Hora atual no servidor local:", local_server.get_hora())
else:
    print("Hora atual no servidor remoto:", remote_server.get_hora())