import socket
import sys

# Create a socket
def create_socket():
    try:
        global host
        global port
        global s
        host = '192.168.43.221'
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print('Socket creation error :'+str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print('Binding the Port : ' + str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as mes:
        print('Socket Binding Error : '+str(mes)+'\n'+'Retrying...')
        bind_socket()


# Estrablish commection with a clint (socket must be listening)
def socket_accept():
    conn,address =s.accept()
    print('Conncction has been Esteblished'+'IP :'+address[0]+'Port :'+str(address[1]))
    send_command(conn)
    conn.close()

# Send commands to friend
def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()

        if len(str.encode(cmd)) > 0 :
            conn.send(str.encode(cmd))
            clint_responns = str(conn.recv(1024),'utf-8')
            print(clint_responns,end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
