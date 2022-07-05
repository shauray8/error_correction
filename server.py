## making this server transfer bits to the client and then using error detection codes
import socket
import time

def main() -> None:
    HOST = "127.0.0.1"
    PORT = 1234
    ## AF_INET (IPV4)
    ## SOCK_STREAM (TCP)
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), PORT))
    s.listen(5)
    msg = "fuck this world"
    buffer = 10

    while True:
        conn, addr = s.accept()
        print(f"Connection established")

        while True:
            time.sleep(2)
            msg = f"{time.monotonic()}"
            msg = f"{len(msg):<{buffer}}" + msg
            conn.send(bytes(msg, "utf-8"))

if __name__ == "__main__":
    main()


