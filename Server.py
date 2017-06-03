import socket
import Stage
import Entity

link={} #
host = "127.0.0.1"
port = 5000
mySocket = socket.socket()
mySocket.bind((host,port))
mySocket.listen(1)
conn, addr = mySocket.accept()
print ("Connection from: " + str(addr))
field=Stage.Stage(10,10,"field.txt")
link[conn]=Entity.Player(0,0,field,"1") #find out about link, probably will be changed when moving to Django
while True:
        data = conn.recv(1024).decode()
        if not data:
                break         
        if data[0]=="m":
                field.move(int(data[1]),int(data[2]),(0,1))#movement test
        conn.send(field.printgrid().encode())
         
conn.close()

