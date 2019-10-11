import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "google.com"
def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False
for x in range(0,4444):
    if pscan(x):
        print("Port", x, "Open")
    else:
        print("Port", x, "Close")