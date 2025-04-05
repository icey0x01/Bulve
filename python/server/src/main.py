from socket import socket, AF_INET, SOCK_STREAM


# [X] Port Binding: Bind to TCP port 22 (or custom port) and start listening.

# [X] SYN Reception: Accept incoming SYN packets from clients.

# [X] SYN-ACK Response: Send SYN-ACK with server’s initial sequence number.

# [X] ACK Handling: Wait for client’s final ACK to establish the connection.


HOST = "127.0.0.1"
# Portai iki 1024 reikalauja aukstesniu privilegiju reiktu runnint su sudo, jeigu norim runnint ant port 22
PORT = 6969
# Dydzio blokas
BUFF_SIZE = 12
"""
AF_INET - Adresu seima (Address Family), kad galetu komunikuoti su IPV4 (0.0.0.0) adresais
SOCK_STREAM - Nustato, kad tai butu TCP protokolas

╔═══════════╦══════════════════════════════════════════════════════╗
║           ║                      Socket Type                     ║
║ Address   ╟────────────┬─────────────┬──────────┬────────────────╢
║ Family    ║ SOCK_DGRAM │ SOCK_STREAM │ SOCK_RDM │ SOCK_SEQPACKET ║ 
╠═══════════╬════════════╪═════════════╪══════════╪════════════════╣
║ IPX/SPX   ║ SPX        │ IPX         │ ?        │ ?              ║
║ NetBIOS   ║ NetBIOS    │ n/a         │ ?        │ ?              ║
║ IPv4      ║ UDP        │ TCP         │ ?        │ SCTP           ║
║ AppleTalk ║ DDP        │ ADSP        │ ?        │ ?              ║
║ IPv6      ║ UDP        │ TCP         │ ?        │ SCTP           ║
║ IrDA      ║ IrLMP      │ IrTTP       │ ?        │ ?              ║
║ Bluetooth ║ ?          │ RFCOMM      │ ?        │ ?              ║
╚═══════════╩════════════╧═════════════╧══════════╧════════════════╝

Galimi patobulinimai:
 - Kad servakas neluztu ir suhandlintu jeigu nera duomenu siunciamu is kliento
 - Multi IPv4 ir IPv6 supportas
 - Butu siaip visai prikolas pasidaryt nuo 0 TCP protokolo handshake, bet sitas dabar eina tai reikia pabaigt;

Su sita komanda galim islupt kompo TCP prisijungimus (daugiau info man netstat)
netstat -an | grep tcp


Pamastymai:
reiktu paskaityti sita - https://stupidpythonideas.blogspot.com/2013/05/sockets-are-byte-streams-not-message.html
"""
TEST_LIST = ["TEST", "DUO"]
my_list = [bytes(item, "utf-8") for item in TEST_LIST]
with socket(family=AF_INET, type=SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Bind naudojamas tam, kad priskirtu tinklo sasaja
    s.listen(2)  # Listen duoda leidima klausytis prisijungimu 2-iem vartotojam
    conn, addr = s.accept()  # kimarina ir laukia iki kada ateis duomenys
    with conn:
        while True:
            data = conn.recv(BUFF_SIZE)  # Paemam buf BUFF_SIZE byte'u dydzio bloka
            if not data:  # jei nera nieko iseinam is loop'o servakas issijungia
                break
            if data == b"pasol naxui":
                conn.sendall(b"tu pasol naxui")
            else:
                conn.sendall(b"tu normalus?")
            print(data)
