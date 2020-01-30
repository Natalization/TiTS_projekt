import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) #ustawienie sposobu numeracji pinów na numery na płytce

GPIO.setup(29, GPIO.OUT) #ustawienie wyjsc
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)

host = ''
port = 5560
password = "hand" #hasło do serwera, można zmieniać co każde odpalenie serwera

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host,port))
    except socket.error as msg:
        print(msg)
    print("Socket bind complete.")
    return s

def setupConnection(): #ewentualnie to przeniesc do petli glownej
    s.listen(1) #allows one connection at the time
    conn, address = s.accept()
    print("Connected to: " +address[0] + ":" + str(address[1]))
    return conn

def Verification(conn): 
    conn.send(bytes("Welcome. Press Enter...", "utf-8"))
    for x in range(3):        
        conn.send(bytes("Password: ", "utf-8"))
        passw = conn.recv(1024) #receive data
        passw = passw.decode('utf-8')
        if passw == password:
            conn.send(bytes("Password correct", "utf-8"))
            dataTransfer(conn)
            #break
        elif x == 0 and passw != password:
            conn.send(bytes("Password incorrect. Attempts remaining: 2", "utf-8"))
            #continue
        elif x == 1 and passw != password:
            conn.send(bytes("Password incorrect. Attempts remaining: 1", "utf-8"))
            #continue
        elif x == 2 and passw != password:
            conn.send(bytes("Password incorrect. Disconnecting from server", "utf-8"))
            conn.close()
            setupConnection()


def HANDCLOSE():
    GPIO.output(29, GPIO.HIGH)
    GPIO.output(31, GPIO.LOW)
    GPIO.output(33, GPIO.HIGH)
    GPIO.output(35, GPIO.LOW)
    reply = "Hand is closing"
    return reply
    
def HANDOPEN():
    GPIO.output(29, GPIO.LOW)
    GPIO.output(31, GPIO.HIGH)
    GPIO.output(33, GPIO.LOW)
    GPIO.output(35, GPIO.HIGH)
    reply = "Hand is opening"
    return reply
    

def dataTransfer(conn):
    while True:
        data = conn.recv(1024) #receive data
        data = data.decode('utf-8')
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]
         
        if command == 'HANDOPEN':
            reply = HANDOPEN()
        elif command == 'HANDCLOSE':
            reply = HANDCLOSE()
        elif command == 'EXIT':
            print("Our client has left us :(")
            break
        elif command == 'KILL':
            print("Our server is closing")
            GPIO.cleanup() #ważne, żeby powrócić do ustawień początkowych aby przypadkiem nie zepsuć rpi
            s.close()
            break
        else:
            reply = 'Unknown command'
        conn.sendall(str.encode(reply))
        print("Data has been sent!")        
    conn.close()

s = setupServer()

while True:
    try:
        conn = setupConnection()
        Verification(conn)
    except:
        break