##CLient side (Clientela)
import socket


mazzutti = True
HEADER = 256
FORMATO = "utf-8"

while mazzutti:
    mazzutti = False
    try:
        PORT = int(input("Porta: "))
        SERVER = str(input("Endereço do servidor: "))
    except Exception as e:
        print("Algo deu errado\n {}".format(e))
        mazzutti = True

###########################################################

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((SERVER, PORT))
except:
    print('Sua conexão foi refusada amigão\n Vê se vc digitou certo')
    quit()

def enviar_bytes(coneteudo) :
    mensagem = coneteudo.encode(FORMATO)
    enviar_tamanho = str(len(mensagem)).encode(FORMATO)
    enviar_tamanho  += b' ' * (HEADER - len(enviar_tamanho))

    cliente.send(enviar_tamanho)
    cliente.send(mensagem)

def chat():
    print('Conversa On \n CTRL + C para desconectar')
    try:
        while True: enviar_bytes(str(input()))
    except:
        print('O sevidor parece estar off\n Camarão que dorme a onda leva')
        print('Boa noite bruno')
        enviar_bytes("!desconectado")


chat()
