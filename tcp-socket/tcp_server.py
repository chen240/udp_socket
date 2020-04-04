from socket import *
'''
该方案每次只能连接一个客户端,如果需要连接多个客户端，就需要用到并发的知识
'''

#1．创建套节字对象
sockfd=socket(AF_INET,SOCK_STREAM)

#2.绑定地址，地址可以本地，也可以是ip地址
sockfd.bind(('192.168.101.13',8887))

#３．设置监听
sockfd.listen(5)
while True:
    #这个地方设置循环可以连接多个客户端,某个客户端推出后还可以继续等待连接
        #4.等待接受连接,得到客户端的套节字对象和地址
    print("Waiting connecting...")
    connfd,addr=sockfd.accept()
    # print(connfd)
    print("Connect from",addr)


    while True:
    #这个地方设置循环可以使得一个客户端连续发送消息
        #5.收发消息
        data=connfd.recv(1024).decode()
        if not data:
            break
        print('recv',data)
        n=connfd.send(b'Recieve your message')
        print("发送了%d个字节"%n)



        #６．关闭套节字
    connfd.close()
sockfd.close()