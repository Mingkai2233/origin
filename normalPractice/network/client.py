import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
hostname = socket.gethostname()
port = 5555
content = "helloworld"
s.connect((hostname, port))
s.send(content.encode('utf-8'))
