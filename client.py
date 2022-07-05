## getting the bits from the server and then resolving all the errors in the bit 
import socket 

def main() -> None:
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 1234  # The port used by the server
    full_msg = ""
    buffer = 10

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((socket.gethostname(), PORT))
        while True:
            full_msg = ''
            new_msg = True
            while True:
                data = s.recv(16)
                if new_msg:
                    print(f"new msg length: {data[:buffer]}")
                    msglen = int(data[:buffer])
                    new_msg = False

                full_msg += data.decode("utf-8")

                if len(full_msg)-buffer == msglen:
                    print("full msg recv")
                    print(full_msg[buffer:])
                    new_msg = True
                    full_msg = ''

    print(f"Received {FULL_MSG!r}")
if __name__ == "__main__":
    main()
