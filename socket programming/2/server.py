import socket
import threading

host = socket.gethostname()
port = 12021

def client_processing (conn , addr):
    while True:
        r_data = conn.recv(1024).decode()
        check = r_data.split("@")
        data =check[1]

        if not r_data:
            break
        if data == "!quit" or not data:
            print(addr , 'left the chat!')
            break
        if check[0] == "1" :
            print(addr ,'>>>' + data)
            data = str(data)[::-1]
            if data[-1].isupper():
                data = data.capitalize()
            print( "reverse is " + data)

        elif check[0] == '2' :
            print(addr , ">>>" + data)
            data = data.upper()
            print("uppercase is " + data)

        elif check[0] == "3" :
            print(addr , ">>>" + data)
            data = data.lower()
            print("lowercase is " + data)

        elif check[0] == "4" :
            print(addr , ">>>" + data)
            data = data.capitalize()
            print("capitalize is " + data)

        conn.send(data.encode())




def main():
    s_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s_socket.bind((host, port))
    print("server is ready...")
    s_socket.listen(5)
    while True:
        conn, addr = s_socket.accept()
        t = threading.Thread(target= client_processing, args=(conn ,addr))
        t.start()
if __name__ == '__main__':
    main()


s_socket.close()