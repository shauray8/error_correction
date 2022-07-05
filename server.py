## making this server transfer bits to the client and then using error detection codes
import socket
import time
import select

def recive_message(s:any) -> any:
    try:
        message_header = s.recv(buffer)
        if not len(message_header):
            return False
        message_length = int(message_header.decode("utf-8"))
        return {"header":message_header, "data":s.recv(message_length)}

    except:
        return False

def main() -> None:
    IP = "127.0.0.1"
    PORT = 1234
    ## AF_INET (IPV4)
    ## SOCK_STREAM (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket,SO_REUSEADDR, 1)
    s.bind((IP, PORT))
    s.listen(5)
    socket_list = [s]
    client = {}
    # msg = "fuck this world"
    buffer = 10

    while True:
        read_sockets, _,exception_sockets = select.select(sockets_list, [], sockets_list)
        for notified in read_sockets:
            if notified == s:
                client_socket, client_address = s.accept
                user = recive_message(s)
                if user is False:
                    sockets_list.append(client_socket)
                    clients[client_socket] = user
                    print(f"Connection established --> {client_Address[0]} : {client_Address[1]}, username:{user['data'].decode('utf-8')}")

                else:
                    message = receive_message(notified)
                    if message is false:
                        print(connection closed)
                        sockets.list.remove(notified)
                        del clients[notified]
                        continue
                    
                    user = clients[notified]
                    print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

                    for client_socket in clients:
                        if client_socket != notified_socket:
                            client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

            for notified_socket in exception_sockets:
                sockets_list.remove(notified_socket)
                del clients[notified_socket]

        while True:
            time.sleep(2)
            msg = f"{time.monotonic()}"
            msg = f"{len(msg):<{buffer}}" + msg
            conn.send(bytes(msg, "utf-8"))

if __name__ == "__main__":
    main()


