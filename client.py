import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   ## for using tcp protocol
host = "172.20.10.4"
port = 1234
s.connect((host,port))
print("Connected succesfully:")
while True:
    # Receive message coming from the server 
    message_rcv = s.recv(1024)
    # Decode message in string from binary
    message_rcv = message_rcv.decode()
    print("message from server:", message_rcv)
    #this will send message to server
    message = input(str("Client"))
    message = message.encode()
    s.send(message)
