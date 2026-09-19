# Mini Network Toolkit 🕵️‍♂️⚡

A simple, multi-functional network scanning and packet sniffing utility written in Python using `socket` and `Scapy`. Designed for educational purposes, local network discovery, and port auditing.

---

## 🚀 Features

- **TCP Port Scanner:** Check if common or specific ports are open on a target host.
- **ICMP Ping:** Test host availability using ICMP echo requests.
- **Local Network Sniffer:** Capture and monitor local traffic to discover active devices (IP & MAC addresses).
- **CLI Interface:** Easy-to-use command-line arguments via `argparse`.

---

## 🛠️ Prerequisites & Installation

Make sure you have Python 3 installed. This tool requires **Scapy**, which may require administrative/root privileges to run raw socket operations.

1. Clone the repository:
   ```bash
   git clone [https://github.com/Dargram/Dargscanner.git](https://github.com/Dargram/Dargscanner.git)
 '''
 2. Navigate to the project directory:
   ```bash
   cd Dargscanner
```
 3. Install dependencies:
   ```bash
   pip3 install scapy
```
## 💻 Usage
Run the script with sudo (Linux/macOS) or as Administrator (Windows) because Scapy requires raw socket permissions for sniffing and ICMP packets.

1. Check an ICMP Ping:
   ```bash
   python3 main.py -t 192.168.1.1 -i
 '''
 2. Scan Popular Ports on a Host:
   ```bash
   python3 main.py -t 192.168.1.1
 ```
 3. Scan a Specific Port:
   ```bash
   python3 main.py -t 192.168.1.1 -p 80
 ```
 4. Sniff Local Network Traffic:
   ```bash
   python3 main.py -s
 ```
## ⚠️ Disclaimer

This tool is created for educational and authorized security auditing purposes only. Do not use it against targets without prior explicit permission.
