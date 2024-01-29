import xmlrpc.client
import json

servidor = xmlrpc.client.ServerProxy('http://192.168.11.8:2801')

mensagem = input('Digite uma mensagem\n-> ')
servidor.salvar(mensagem)

dados = {
  'ip': servidor.getIP(),
  'hora': servidor.getHora(),
  'chamadas': servidor.getChamadas(),
  'mensagens': servidor.getMensagens(),
}
dados_json = json.dumps(dados, indent=2)

print(dados_json)