#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


print("#"*30)
print("     Simple port scanner     ")
print("#"*30)
print("\n")

def main():
    def portscanner():
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if s.connect_ex((host,port)):
            print(f"Port {port} is closed!")
        else:
            print(f"Port {port} is open!")
            try:
                s = socket.socket()
                s.connect((host, int(port)))
                s.settimeout(5)
                data = s.recv(1048576)
                print(data)
                s.close()
            except:
                print("connection refused")
        s.close()

    host =str(input("Enter the Host: "))
    what =int(input("Scan one port(1) or scan a range(2): "))

    if what == 1:
        port =int(input("Enter the Port: "))
        portscanner()
    elif what == 2:
        portrangee = int(input("Enter the start port: "))
        portrangez = int(input("Enter the end port: "))
        for port in range(portrangee, portrangez + 1):
            portscanner()

    else:
	print("only one and tow allowed!")
        main()

main()
