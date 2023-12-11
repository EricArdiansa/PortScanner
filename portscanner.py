import socket
from IPy import IP

#fungsi scanning tiap port
def scan(target, jml_port):
    converted_ip =cek_ip(target)
    print("\n" + "[Menscan Target]" + str(target))
    for port in range(1, jml_port):
        scan_port(converted_ip, port)

#fungsi untuk memvalidasi apakah inputan yang dimasukkan adalah ip
def cek_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)
    

#fungsi banner untuk mengetahui layanan yang berjalan di port yang terbuka
def cek_banner(s):
    return s.recv(1024)

#fungsi scan port untuk mengecek apakah port bisa diakses atau tidak
def scan_port(alamat_ip,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((alamat_ip, port))
        try:
            banner = cek_banner(sock)
            print("[+] Port terbuka" + str(port) + ":" + str(banner.decode().strip("\n").strip("\r")))
        except:
            print("[+] Port Terbuka" + str(port))
    except:
        pass   

#fungsi utama
if __name__ == "__main__":
    target = input("[+] Masukkan target untuk diScan(Pisahkan target yang lebih dari satu menggunakan ,): ")
    jumlah_port = int(input("[+] Masukkan jumlah port yang ingin kamu scan"))
    if ',' in target:
        for ip_add in target.split(","):
            scan(ip_add.strip(" "), jumlah_port)
    else:
        scan(target, jumlah_port)