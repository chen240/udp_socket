from socket import *

#1.创建套节字
sockfd=socket(AF_INET,SOCK_STREAM)


#2.发起连接 connect()
server_addr=('192.168.101.13',8887)
sockfd.connect(server_addr)
while True:
    #3.消息收发
    data=input("发送>>")
    if not data:
        break

    sockfd.send(data.encode())
    data=sockfd.recv(1024)
    print('接受到',data.decode())

#4.关闭套节字
sockfd.close()