import socket

MSGLEN = 1024

def myreceive():
    chunks = ""
    bytes_recd = 0
    while bytes_recd < MSGLEN:
        chunk = conn.recv(MSGLEN - bytes_recd).decode()
        if chunk == '':
            raise RuntimeError("socket connection broken")
        chunks = chunks + chunk
        bytes_recd = bytes_recd + len(chunk)
    return chunks

strmsg = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 2222))
s.listen(5)

while True:
    (conn, address) = s.accept()

    while True:
        msg =  myreceive()

        print(msg.strip())

        if "CLOSE" == msg.upper().strip():
            break

    print("Connection closed! Next please..\n\n ")
