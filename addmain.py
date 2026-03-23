#!/usr/bin/python

from socket import *
import optparse
from threading import *
from termcolor import colored

def connscan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(0.01)
        sock.connect((tgtHost, tgtPort))
        print(colored(f"{tgtPort}/tcp is open!", 'green'))
        try:
            s = socket()
            s.connect((tgtHost, tgtPort))
            data = s.recv(1048576)
            print(f"Info for {tgtPort}, {data}")
            s.close()
        except:
            print("connection refused")
    except:
        print(colored(f"{tgtPort}/tcp is closed", 'red'))
    finally:
        sock.close()

def portscanner(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f"Unknown host {tgtHost}")
        return

    try:
        tgtName = gethostbyaddr(tgtIP)[0]
        print(f"[+] Scan results for {tgtName}")
    except:
        print(f"Scan results for {tgtIP}")

    for port in tgtPorts:
        t = Thread(target=connscan, args=(tgtHost, int(port)))
        t.start()

def main():
    help = optparse.OptionParser("Usage: -H <Target Host> -p <Target Port>")
    help.add_option("-H", dest='tgtHost', help='specify target host')
    help.add_option("-p", dest='tgtPort', help='specify target port(s) comma separated')

    (options, args) = help.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if (tgtHost is None) or (tgtPorts[0] is None):
        print(help.usage)
        exit(0)

    portscanner(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()

