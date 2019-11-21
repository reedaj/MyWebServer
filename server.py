#python Server

from socket import *
import traceback
import os
#from playsound import playsound

serverPort = 10891
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(32)

#HTTP Messages
okMessage = "HTTP/1.0 200 OK\n\n"
fileNotFound = "HTTP/1.0 404 Not Found\n\n404 File Not Found"
internalServerError = "HTTP/1.0 500 Internal Server Error\n\nServerside Error: "

print("Ready to go!")
while True:
    connectionSocket, addr = serverSocket.accept()
    request = connectionSocket.recv(1024).decode()
    #Need to figure out how to tell the difference between when I need to read as binary/raw, and when to decode.
    try:
        print("REquet Recved")
        print(request)
        #logFile = open("connectionLog.txt", "a")
        #logFile.write(str(addr) + " \n")
        #logFile.close()
        #playsound("notify.wav")
        #Open up the filename from the client
        filename = request.split()[1]
        #If html file. Read normally. If any other extension, read as binary.
        #print(filename.split(".")[1])
        if filename != "/" and filename[0] == "/":
            extension = filename.split(".")
            if( extension[1] == "html" or extension[1] == "htm" or extension[1] == "HTML" ):
                file = open(filename[1:], "r")
                #read the file if it exists
                fileData = file.read()
                #add the OK message in front of the file data
                message = okMessage + fileData
                #Send the file and close the connection
                connectionSocket.sendall(message.encode())
            else:
                file = open(filename[1:], "rb")
                #read the file if it exists
                fileData = file.read()
                #add the OK message in front of the file data
                message = okMessage.encode() + fileData
                #Send the file and close the connection
                connectionSocket.sendall(message)
        else:
            #Default return index.html
            file=open("index.html", "r")
            message = okMessage + file.read()
            connectionSocket.sendall(message.encode())
            connectionSocket.close()
        
        connectionSocket.close()

    except IOError:
        #If the file doesn't exist, send a 404 message
        connectionSocket.sendall(fileNotFound.encode())
        connectionSocket.close()
    except KeyboardInterrupt:
        connectionSocket.close()
        serverSocket.close()
    except Exception as e:
        connectionSocket.close()
