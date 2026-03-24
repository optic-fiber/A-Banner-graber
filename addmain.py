#!/usr/bin/python

from socket import *
import optparse
from threading import *
from termcolor import colored

def connscan(tgtHost, tgtPort):
    sock = None
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(0.1)
        sock.connect((tgtHost, tgtPort))
        print(colored(f"{tgtPort}/tcp is open!", 'green'))
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(0.5)
            s.connect((tgtHost, tgtPort))
            data = s.recv(1024)
            if data:
                print(f" Banner: {data.decode(errors='ignore').strip()}")
            s.close()
        except:
            print("connection refused")
    except:
	pass
    finally:
	if sock:
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
    exit()

def main():
    help = optparse.OptionParser("Usage: -H <Target Host> -p <Target Port>")
    help.add_option("-H", dest='tgtHost', help='specify target host')
    help.add_option("-p", dest='tgtPort', help='specify target port(s) comma separated')

    (options, args) = help.parse_args()

    tgtHost = options.tgtHost

    if options.tgtPort is None:
        print("Scanning all ports...")
        tgtPorts = range(1, 65536)
    else:
	tgtPorts = [int(p) for p in options.tgtPort.split(',')]

    if (tgtHost is None):
        print(help.usage)
        exit()

    portscanner(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()

