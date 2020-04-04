from socket import *

#1.创建数据报套节字
sockfd=socket(AF_INET,SOCK_DGRAM)

#2.绑定服务端地址
server_addr=('0.0.0.0',8889)
sockfd.bind(server_addr)

#3.消息收发
while True:
    data,addr=sockfd.recvfrom(1024)
    print("Receive from %s:%s"%(addr,data.decode()))
    sockfd.sendto('收到你的消息'.encode(),addr)

sockfd.close()