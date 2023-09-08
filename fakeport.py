import socket

def fake_service(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(1)

    print(f'Fake service is listening on port {port}')

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f'Connection from: {client_addr}')

        http_response = b'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nFake service response\n'
        client_socket.send(http_response)
        client_socket.close()

if __name__ == '__main__':
    ip = "15.0.0.1"
    #ip = "localhost"
    port_number = 8765 # Change this to your desired port
    fake_service(ip,port_number)
