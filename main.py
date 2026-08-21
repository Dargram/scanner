#!/usr/bin/env python3
import socket
import argparse

POPULAR_PORTS = {21, 22, 23, 25, 53, 80, 443, 1433, 2000, 3000, 3306, 4444, 5000, 5432, 5555, 8080}
# parser for arguments (host and port)
def args_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--host", type=str, required=True)
    parser.add_argument("-p", "--port", type=int, required=False)
    args = parser.parse_args()
    return args

# main function for scanning ports
def scan_port(host:str, port:int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1.0)

        # connect_ex returns 0 (int), if connection is correct
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"[+] Port is open [{port}]")

        else:
            print(f"[-] Port is close [{port}]")

if __name__ == "__main__":
    args = args_parser()

    if args.port:
        scan_port(args.host, args.port)
    else:
        for port in POPULAR_PORTS:
            scan_port(args.host, port)
