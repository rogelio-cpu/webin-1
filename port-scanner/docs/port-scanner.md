# 📘 Tools Documentation

port-scanner.py — TCP Port Scanner

🔍 Description

Un outil simple écrit en Python pour scanner des ports TCP ouverts sur une cible donnée.

🛠️ Utilisation

python3 port-scanner.py -t 192.168.1.1 -p 20-100

📦 Paramètres

-t, --target : adresse IP ou domaine à scanner (ex: 192.168.1.1)

-p, --ports : plage de ports à scanner (ex: 1-1024)

🧠 Fonctionnement

Analyse des ports un par un dans la plage spécifiée

Tentative de connexion TCP avec socket.connect_ex()

Affichage des ports ouverts

✅ Exemple de résultat

[+] Port 22 is open
[+] Port 80 is open

⚠️ Avertissement

N'utilisez cet outil que sur des machines que vous possédez ou pour lesquelles vous avez une autorisation explicite. L'analyse de ports non autorisée est illégale.