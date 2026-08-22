#!/usr/bin/env python3
import socket
import ipaddress
import argparse

POPULAR_PORTS = [80, 443, 4444, 21, 22, 23, 25, 53, 1433, 2000, 3000, 3306, 5000, 5432, 5555, 8080]
DEVICES_IN_SUBNET = []

# main function that starts everything
def main():
    args = args_parser()

    if args.range:
        scan_network(args.range, args.status)

    elif args.port and args.host:
        scan_ports(args.host, args.port)
    else:
        for port in POPULAR_PORTS:
            scan_ports(args.host, port)

# parser for arguments (host and port)
def args_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--range", type=str, required=False)
    parser.add_argument("-s", "--status", type=str, required=False)
    parser.add_argument("-i", "--host", type=str, required=False)
    parser.add_argument("-p", "--port", type=int, required=False)

    args = parser.parse_args()
    return args

# function for scanning ports
def scan_ports(host:str, port:int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)

        # connect_ex returns 0 (int), if connection is correct
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"\033[92m[+]\033[0m Port is open [{port}]")

        else:
            print(f"\033[91m[-]\033[0m Port is closen [{port}]")

# function for scanning devices in subnetwork
def scan_network(network_range: str, status: str) -> None:
    network = ipaddress.ip_network(network_range, strict=False) # network object

    for ip in network.hosts():
        current_ip = str(ip)

        for port in POPULAR_PORTS:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.1)

                result = sock.connect_ex((current_ip, port))
                if status == 'hard':
                    print(f"\033[93mTCP/IP -> {current_ip}:{port}\033[0m")

                if result == 0:
                    DEVICES_IN_SUBNET.append(current_ip)
                    break
    print(DEVICES_IN_SUBNET)

if __name__ == "__main__":
    main()
