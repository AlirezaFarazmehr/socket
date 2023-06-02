import socket
import threading

host = socket.gethostname()
port = 12021

def client_processing(conn , addr):
    while True:
        r_data = conn.recv(1024).decode()
        if  r_data == "!quit" or not r_data:
            print(addr, 'left the chat!')
            break
        print(addr ,'>>>' + str(r_data))
        s_data = str(r_data)[::-1]
        if s_data[-1].isupper():
            s_data = s_data.capitalize()
        conn.send(s_data.encode())
        print(s_data)






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