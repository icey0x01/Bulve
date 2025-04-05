from socket import AF_INET, SOCK_STREAM, socket

HOST = "127.0.0.1"
# Portai iki 1024 reikalauja aukstesniu privilegiju reiktu runnint su sudo, jeigu norim runnint ant port 22. Portas turi sutapt su serverio portu
PORT = 6969
BUFF_SIZE = 23
with socket(AF_INET, SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # prisijungiam prie hosto
    s.sendall(b"Zdarof molis")  # nusiunciam teksta
    data = s.recv(
        BUFF_SIZE
    )  # Docs'ai raso - Receive data from the socket. The return value is a bytes object representing the data received. https://docs.python.org/3/library/socket.html#socket.socket.recv
    print(data)
    s.sendall(b"pasol naxui")
    data = s.recv(BUFF_SIZE)
    print(data)
