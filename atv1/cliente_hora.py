import socket
import threading

def receber_mensagensUDP(sock):
    while True:
        data, addr = sock.recvfrom(2048)
        mensagem = data.decode()
        if mensagem!='0':
            #Imprimindo a mensagem recebida
            print(mensagem)
        else:
            sock.close()

def receber_mensagensTCP(sock):
    while (True):
        data = sock.recv(2048)
        # data = sock.recvfrom(2048)
        mensagem = data.decode()
        if mensagem!='0':
            #Imprimindo a mensagem recebida
            print(data.decode())
        else:
            sock.close()
            break

sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addressTCP = ('localhost', 20001)

sockUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addressUDP = ('localhost', 20002)


tipoConexao = int(input("Digite:\n1 - para TCP\n2 - para UDP\n-> "))
if tipoConexao == 1:
    print ("Conectando %s porta %s" % server_addressTCP)

    sockTCP.connect(server_addressTCP)
    recepcao = threading.Thread(target=receber_mensagensTCP,args=(sockTCP,))
    recepcao.start()
    while (True):    
        message = input("Receber a Hora: ")
        sockTCP.sendall(message.encode('utf-8'))
        if message=='0':
            break

    recepcao.join()
else:
    print ("Conectando %s porta %s" % server_addressUDP)

    recepcao = threading.Thread(target=receber_mensagensUDP,args=(sockUDP,))
    recepcao.start()

    while True:
        message = input("Receber a Hora: ")
        sockUDP.sendto(message.encode('utf-8'), server_addressUDP)
        if message=='0':
            break

    recepcao.join()