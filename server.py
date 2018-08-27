import socket #socket模块

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建TCP Socket


def handler(client_sock, addr):
    try:
        print('new client from %s:%s' % addr)
        msg = client_sock.recv(100) #把接收的数据实例化
        client_sock.send(msg)
        print('received data[%s] from %s:%s' % ((msg,) + addr))
    finally:
        client_sock.close()
        print('client[%s:%s] socket closed' % addr)

if __name__ == '__main__':

    # 设置 socket reuse address 后,可以立即使用 TIME_WAIT 状态的 socket
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('192.168.1.104',9999)) #将socket绑定到地址
    sock.listen(5) #开始监听TCP传入连接

    while 1:
        client_sock, addr = sock.accept()
        handler(client_sock, addr)