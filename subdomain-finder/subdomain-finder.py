#!/usr/bin/env python3
# subdomain-finder.py

import socket
import argparse

def find_subdomains(domain, wordlist_path):
    print(f"[~] Loading wordlist from: {wordlist_path}")
    try:
        with open(wordlist_path, "r") as f:
            subdomains = f.read().splitlines()
    except FileNotFoundError:
        print("[!] Wordlist file not found.")
        return

    print(f"[~] Starting scan on: {domain}\n")
    for sub in subdomains:
        full_domain = f"{sub.strip()}.{domain}"
        try:
            ip = socket.gethostbyname(full_domain)
            print(f"[+] Found: {full_domain} → {ip}")
        except socket.gaierror:
            pass  # sous-domaine inexistant

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain brute-force discovery tool")
    parser.add_argument("domain", help="Target domain (e.g. example.com)")
    parser.add_argument("-w", "--wordlist", default="wordlist/subdomains.txt", help="Path to subdomain wordlist")

    args = parser.parse_args()
    find_subdomains(args.domain, args.wordlist)
