import socket

#host = '157.158.62.175' 
host = '192.168.0.18'
port = 5560

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
#obsluga hasla
while True:
    msg= s.recv(1024)
    msgencode = msg.decode("utf-8")
    print(msgencode)
    
    password = input()
    s.send(str.encode(password))
    
    if msgencode == "Password correct":
        break
    elif msgencode == "Password incorrect. Disconnecting from server":
        s.close()

while True:
        ##obsługa komend
  command = input("Enter your command: ")
  if command == 'EXIT':
    s.send(str.encode(command))
    break
  elif command == 'KILL':
    s.send(str.encode(command))
    break
  s.send(str.encode(command))
  #reply = s.recv(1024)
  #print(reply.decode('utf-8'))
s.close()