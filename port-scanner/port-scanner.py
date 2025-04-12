#!/usr/bin/env python3
# port-scanner.py

import socket
import argparse
from datetime import datetime

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user (You).")
        exit()
    except Exception as e:
        print(f"[!] Error on port {port}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple TCP Port Scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-p", "--ports", help="Port range, e.g. 20-100", default="1-1024")

    args = parser.parse_args()
    target = socket.gethostbyname(args.target)
    port_range = args.ports.split("-")

    print(f"\n[*] Scanning {target} from port {port_range[0]} to {port_range[1]}")
    print(f"[*] Started at {datetime.now().strftime('%H:%M:%S')}\n")

    for port in range(int(port_range[0]), int(port_range[1]) + 1):
        scan_port(target, port)

    print(f"\n[*] Scan completed at {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()
