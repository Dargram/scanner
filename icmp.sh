#!/bin/bash
source .env/bin/activate
export PYTHONDONTWRITEBYTECODE=1
clear

BLUE="\033[94m"
ORANGE="\033[93m"
RESET="\033[0m"
echo -e "----- Started main.py -----"

echo -e "\n${BLUE}ICMP-request -> 192.168.0.1${RESET}"
python3 main.py --icmp --host 192.168.0.1

echo -e "\n${ORANGE}ICMP-request -> one.one.one.one (Cloudflare DNS-server)${RESET}"
python3 main.py --icmp --host one.one.one.one

echo -e "\n${BLUE}ICMP-request -> youtube.com${RESET}"
python3 main.py --icmp --host youtube.com

echo -e "\n${ORANGE}ICMP-request -> kep.nung.edu.ua${RESET}"
python3 main.py --icmp --host kep.nung.edu.ua

echo -e "\n${BLUE}ICMP-request -> spotify.com${RESET}"
python3 main.py --icmp --host spotify.com

echo -e "\n${ORANGE}ICMP-request -> 57.131.40.69 (Education Platform)${RESET}"
python3 main.py --icmp --host 57.131.40.69

echo -e "\n----- ICMP ended -----"
