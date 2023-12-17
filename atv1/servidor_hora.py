import socket
import threading
from datetime import datetime

def conexao_clienteUDP(client,address):
    mensagem = client.decode()
    '''
    PROTOCOLO
    '''
    if (mensagem!='0'):
        print(mensagem, address)
        current_dateTime = datetime.now().time()
        current_dateTime = str(current_dateTime)
        sockUDP.sendto(current_dateTime.encode(), address)
    else:
        sockUDP.sendto('0'.encode(), address)

def conexao_clienteTCP(client,address):
    
    while (True):    
        data = client.recv(2048)
        '''
        PROTOCOLO
        '''
        mensagem = data.decode()
        if (mensagem!='0'):
            current_dateTime = datetime.now().time()
            current_dateTime = str(current_dateTime)
            client.sendall(current_dateTime.encode())
        else:
            client.sendall('0'.encode())
            break
    #Fechando o socket
    client.close()

sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockTCP.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverTCP_address = ('localhost', 20001)
sockTCP.bind(serverTCP_address)

sockUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverUDP_address = ('localhost', 20002)
sockUDP.bind(serverUDP_address)

tipoConexao = int(input("Digite:\n1 - para TCP\n2 - para UDP\n-> "))
if tipoConexao == 1:
    print("\n🚀 Iniciando servidor em %s:%s\n" % serverTCP_address)
    sockTCP.listen(1)

    while True:
        client, address = sockTCP.accept()
        conexao = threading.Thread(target=conexao_clienteTCP,args=(client,address,))
        conexao.start()

        clientUDP, addressUDP = sockTCP.accept()
        conexaoUDP = threading.Thread(target=conexao_clienteUDP,args=(clientUDP,addressUDP,))
        conexaoUDP.start()
else:
    print("\n🚀 Iniciando servidor em %s:%s\n" % serverUDP_address)
    while True:
        client, address = sockUDP.recvfrom(2048)
        conexao_clienteUDP(client, address)
