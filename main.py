import socket

print("#"*20)
print("Banner grabber")
print("#"*20)

def banner(ip, port):
    try:
        s = socket.socket()
        s.connect((ip, int(port)))
        s.settimeout(5)
        data = s.recv(1048576)
        print(data)
        s.close()
    except:
        print("connection refused")

def main():
    ip = input("Please enter the IP: ")
    port = input("Please enter the Port: ")
    banner(ip, port)

main() 
