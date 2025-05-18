# 从 socket 模块导入所有内容，这样可以直接使用 socket 模块中的函数和类
from random import choice
from socket import *

# 创建一个 TCP 套接字对象，SOCK_STREAM 表示使用 TCP 协议
S = socket()

# 将套接字绑定到指定的地址和端口，'0.0.0.0' 表示监听所有可用的网络接口，8888 是监听的端口号
S.bind(('0.0.0.0', 8888))

# 开始监听客户端的连接请求，参数未指定，表示使用默认的最大连接数
S.listen()

# 等待客户端的连接，当有客户端连接时，返回一个新的套接字对象 s 用于与客户端通信，以及客户端的地址 addr
s, addr = S.accept()

# 打印客户端的地址，方便了解是哪个客户端连接到了服务器
print(addr)

# 打印提示信息，告知用户可以选择的操作
print("1.关机 2.重启")

# # 提示用户输入选择，并将用户输入的内容存储在变量 choice 中，这里原代码可能存在拼写错误，正确的应该是 choice
# choices = input("请输入：")

# # 将用户输入的选择编码为字节流，并通过套接字 s 发送给客户端
# s.send(choices.encode())