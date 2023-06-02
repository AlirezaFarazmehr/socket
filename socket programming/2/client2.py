import socket

host = socket.gethostname()
port = 12021

c_socket=socket.socket()
c_socket.connect((host, port))

opp = input("What operation do you want to be performed? Send the number inside the parentheses. \n reverse(1) \n Uppercase(2) \n Lowercase(3) \n Capital(4) : \n")

while True:
    c_data = input("->")
    if c_data.strip() == "!quit" :
        c_data = "1@!quit"
        c_socket.send(c_data.encode())
        print("\n")
        c_socket.close()
        break
    c_data = opp + "@" + c_data
    c_socket.send(c_data.encode())
    s_data = c_socket.recv(1024).decode()
    print(s_data)