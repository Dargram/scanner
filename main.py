#!/usr/bin/env python3
import socket
import argparse
from scapy.all import IP, ICMP, Ether, sniff, sr1

POPULAR_PORTS = [80, 443, 4444, 21, 22, 23, 25, 53, 1433, 2000, 3000, 3306, 5000, 5432, 5555, 8080]
DEVICES_IN_NETWORK = []
SEEN_DEVICES = set()

# main function that starts everything
def main():
    args = args_parser()

    if args.icmp and args.host:
        icmp_request(args.host)

    elif args.sniff:
        sniff(prn=packet_handler, store=0)

    elif args.port and args.host:
        scan_ports(args.host, args.port)
    else:
        for port in POPULAR_PORTS:
            scan_ports(args.host, port)


# parser for arguments (host and port)
def args_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--host", type=str, required=False, help="Enter hostname")
    parser.add_argument("-p", "--port", type=int, required=False, help="Enter port")
    parser.add_argument("-i", "--icmp", action="store_true", help="Use ICMP ping")
    parser.add_argument("-s", "--sniff", action="store_true", help="Do you want to sniff traffic?")

    args = parser.parse_args()
    return args


# function for scanning ports
def scan_ports(host:str, port:int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        tcp_socket.settimeout(0.5)

        # connect_ex returns 0 (int), if connection is correct
        result = tcp_socket.connect_ex((host, port))
        if result == 0:
            print(f"\033[92m[+]\033[0m Port is open [{port}]")

        else:
            print(f"\033[91m[-]\033[0m Port is closen [{port}]")


# function for sending ICMP-requests
def icmp_request(host: str) -> None:
    packet = IP(dst=host) / ICMP()
    response = sr1(packet, timeout=1, verbose=False)

    if response is not None and response.haslayer(ICMP):
        if response.getlayer(ICMP).type == 0:
            print(f"\033[92m[+]\033[0m ICMP -> {host}")
            return

    print(f"\033[91m[-]\033[0m ICMP -> {host}")


# function for checking traffic in local network
def packet_handler(packet):
    if packet.haslayer(Ether) and packet.haslayer(IP):
        src_ip = packet[IP].src
        src_mac = packet[Ether].src

        if src_ip.startswith("192.168.0."):
            device_info = f"IP: {src_ip} | MAC: {src_mac}"

            if device_info not in SEEN_DEVICES:
                SEEN_DEVICES.add(device_info)
                print(f"[LOCAL] Знайдено пристрій -> {device_info}")


if __name__ == "__main__":
    main()
