import socket

HOST = 'localhost'
PORT = 5000

# Cria o socket do servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

print(f"Servidor escutando em {HOST}:{PORT}...")

conn, addr = servidor.accept()
print(f"Conexão estabelecida com {addr}")

while True:
    dados = conn.recv(1024)
    if not dados:
        break
    mensagem = dados.decode()
    print("Cliente:", mensagem)
    resposta = "Recebido: " + mensagem
    conn.sendall(resposta.encode())

conn.close()
servidor.close()
