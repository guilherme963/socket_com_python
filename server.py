#???
try:
    import socket
    import threading
except Exception as e:
    print('Alguma coisa não está instalada, ele disse que foi o {}'.format(e))



PORT = 5080
SERVER = socket.gethostbyname(socket.gethostname())
addr = (SERVER, PORT)
HEADER = 256 # Tamanho do Header do protocolo



servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Tipo da meia
servidor.bind((SERVER, PORT))

def interagir(conectividade, addr):
    print("{} Se conectou".format(addr))
    while True:
        bit_len = conectividade.recv(HEADER).decode('utf-8')
        if bit_len:
            mensagem = conectividade.recv(int(bit_len)).decode('utf-8')
            print(addr[0], ":", mensagem)
            if mensagem == "!desconectado":break

def iniciar():
    verdade = True
    print("Iniciando Servidor...\n" ,SERVER, socket.gethostname(), PORT)
    servidor.listen()
    print('Aguardando conectividade....')
    while verdade:
        conectividade, addr = servidor.accept()
        thread = threading.Thread(target = interagir, args = (conectividade, addr))
        thread.start()
        print("conectividades ativas: ", threading.activeCount() - 1)



iniciar()
