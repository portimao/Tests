import socket

MSGLEN = 1024

def mysend(msg):

    bytes_sent=0


        sent = s.send(msg[bytes_sent:])

        if sent == 0 :
            print("Error when sending message")
            exit()

        bytes_sent =  bytes_sent + sent


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 2222))

while True :
    msg=input("String to send: ")

    msg = msg + " "*(MSGLEN-len(msg))

    mysend(msg.encode())

    if "CLOSE" == msg.upper().strip():
        break

print("Buy-buy")
