## getting the bits from the server and then resolving all the errors in the bit 
import socket 

def main() -> any:
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 1234  # The port used by the server
    FULL_MSG = ""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((socket.gethostname(), PORT))
        #s.sendall(b"Hello, world")
        while True:
            data = s.recv(8)
            if len(data) <= 0:
                break
            FULL_MSG += data.decode("utf-8")

    print(f"Received {FULL_MSG}")
if __name__ == "__main__":
    main()
