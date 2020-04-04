#必须要有客户端，没有telnet小工具
from socket import *
import sys

if len(sys.argv)<3:
    print('''argv is error!
             run as
             python3 udp_client.py 127.0.0.1 8888''')
    raise

#从命令行输入ip和端口
HOST=sys.argv[1]
PORT=int(sys.argv[2])
ADDR=(HOST,PORT)

#创建套节字
sockfd=socket(AF_INET,SOCK_DGRAM)

#消息的收发
while True:
    data=input("消息:")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    data,addr=sockfd.recvfrom(1024)
    print("从服务端到:",data.decode())

sockfd.close()