from logging.handlers import SocketHandler
import socket
from tkinter.tix import Tree

#Definiciones:
socket1 = socket.socket() 
socket2 = socket.socket()
#REAL
direccion1 = '172.21.33.221'
direccion2 = '172.21.33.222'

puerto = 5500

try:
    socket1.connect((direccion1, puerto))
    socket2.connect((direccion2, puerto)) 
except:
    while True:
        if (socket1.connect((direccion1, puerto)) != True and socket2.connect((direccion2, puerto)) != True):
            break
        print("trying to connect")
        
robot1_ready = False
robot2_ready = False

while(robot1_ready == False and robot2_ready == False):
    data1 = socket1.recv(4096)
    data2 = socket2.recv(4096)

    if len(data1)>0:
        robot1_ready = True
        res1=str(data1)
        print(res1[2:len(res1)-1])
        robot1_ready = True

    if len(data2)>0:
        robot2_ready = True
        res2=str(data2)
        print(res2[2:len(res2)-1])
        robot2_ready = True

mensaje = "juntos"
socket1.send(mensaje.encode())
socket2.send(mensaje.encode())

robot1_ready = False
robot2_ready = False


while(robot1_ready == False and robot2_ready == False):
    data1 = socket1.recv(4096)
    data2 = socket2.recv(4096)

    if len(data1)>0:
        robot1_ready = True
        res1=str(data1)
        print(res1[2:len(res1)-1])

        if(res1 == "end"):
            robot1_ready = True
        else:
            mensaje = "melocoton"
            socket2.send(mensaje.encode())

    elif len(data2)>0:
        robot2_ready = True
        res2=str(data2)
        print(res2[2:len(res2)-1])

        if(res2 == "end"):
            robot2_ready = True
        else:
            mensaje = "papagallo"
            socket1.send(mensaje.encode())

socket1.close()
socket2.close()

    #if(robot1_ready == True and robot2_ready == True):

    #    robot1_ready = False
    #    robot2_ready = False

    #    mensaje = "papagallo"
    #    socket1.send(mensaje.encode())

    #    mensaje = "melocoton"
    #    socket2.send(mensaje.encode())

