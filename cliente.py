import socket

HOST = 'localhost'  # Endereço do servidor (127.0.0.1)
PORT = 5000         # Porta que o servidor está escutando

# Cria o socket do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((HOST, PORT))
    print(f"Conectado ao servidor em {HOST}:{PORT}")
    
    while True:
        mensagem = input("Você: ")
        if mensagem.lower() == 'sair':
            break
        cliente.sendall(mensagem.encode())
        resposta = cliente.recv(1024).decode()
        print("Servidor:", resposta)

except ConnectionRefusedError:
    print("Erro: Não foi possível se conectar ao servidor.")
finally:
    cliente.close()
