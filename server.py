## making this server transfer bits to the client and then using error detection codes
import socket

def main() -> any:
    HOST = "127.0.0.1"
    PORT = 1234
    ## AF_INET (IPV4)
    ## SOCK_STREAM (TCP)
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), PORT))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print(f"Connection established")
        conn.send(bytes(f" fuck this world", "utf-8"))

if __name__ == "__main__":
    main()


