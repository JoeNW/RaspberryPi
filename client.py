#client
import socket
import sys
if __name__ == '__main__': #如果模块被直接运行，则代码块被运行，如果模块被导入，则代码块不被运行
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#创建TCP Socket

    data_to_sent = 'hello tcp socket'
    try:
        sock.connect(('192.168.1.104',9999))

        sent = sock.send(data_to_sent.encode())
        print(sock.recv(1024))
    finally:
        sock.close()
        print('socket closed')