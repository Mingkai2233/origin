import socket

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)
hostName = socket.gethostname()
port = 5555
s.bind((hostName, port))
s.listen(5)
print("begin listening")
while True:
    clientSocket, addr = s.accept()
    print("address:", str(addr))
    print(clientSocket.recv(1000))



