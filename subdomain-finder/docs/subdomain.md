# subdomain-finder.py — Subdomain Discovery

🔍 Description

Ce script fait une découverte de sous-domaines par brute-force DNS. Il tente de résoudre chaque sous-domaine contenu dans une wordlist pour détecter ceux qui existent réellement.

🛠️ Utilisation

python3 subdomain-finder.py example.com -w wordlists/subdomains.txt

📦 Paramètres

domain : le domaine cible (ex: example.com)

-w, --wordlist : chemin vers le fichier contenant les sous-domaines

🧠 Fonctionnement

Lecture de la wordlist

Construction des noms complets (ex: admin.example.com)

Résolution DNS avec socket.gethostbyname()

Affichage des hôtes valides

⚠️ Avertissement

Utilisation à des fins éducatives et avec autorisation uniquement. Ne jamais scanner un domaine sans accord préalable.

