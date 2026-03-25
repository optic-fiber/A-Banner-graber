#!/usr/bin/python

from socket import *
import optparse
from threading import *
from termcolor import colored

def connscan(tgtHost, tgtPort, tgtBanner):
    sock = None
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(0.1)
        sock.connect((tgtHost, tgtPort))
        print(colored(f"{tgtPort}/tcp is open!", 'green'))
        if tgtBanner:
            try:
                s = socket(AF_INET, SOCK_STREAM)
                s.settimeout(0.5)
                s.connect((tgtHost, tgtPort))
                data = s.recv(1024)
                if data:
                    print(f" Banner: {data.decode(errors='ignore').strip()}")
                s.close()

            except:
                pass

    except:
	pass
    finally:
	if sock:
            sock.close()

def portscanner(tgtHost, tgtPorts, tgtBanner):
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
        t = Thread(target=connscan, args=(tgtHost, int(port), tgtBanner))
        t.start()
    exit()

def main():
    help = optparse.OptionParser("Usage: -H <Target Host> -p (optionl)<Target Port or multiple ports with a , > -b <Gives you the banner> ")
    help.add_option("-H", dest='tgtHost', help='specify target host')
    help.add_option("-p", dest='tgtPort', help='specify target port(s) comma separated')
    help.add_option("-b", action="store_true", dest="banner", help="enable banner grabbing")

    (options, args) = help.parse_args()

    tgtHost = options.tgtHost

    tgtBanner = 1 if options.banner else 0

    if options.tgtPort is None:
        print("Scanning all ports...")
        tgtPorts = range(1, 65536)
    else:
	tgtPorts = [int(p) for p in options.tgtPort.split(',')]

    if (tgtHost is None):
        print(help.usage)
        exit()

    try:
        portscanner(tgtHost, tgtPorts, tgtBanner)
    except KeyboardInterrupt:
        print(colored("[!] Scann aborded", 'red'))
        exit()

if __name__ == '__main__':
    main()




