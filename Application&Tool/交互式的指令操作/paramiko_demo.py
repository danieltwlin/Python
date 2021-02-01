import paramiko
 
# 实例化SSHClient
ssh = paramiko.SSHClient()

# 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接SSH服务端，以用户名和密码进行认证
ssh.connect(hostname='192.168.1.105', port=22, username='root', password='123456')

# 打开一个Channel并执行命令
stdin, stdout, stderr = ssh.exec_command('df -h ')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值

# 打印执行结果
print(stdout.read().decode('utf-8'))    

# print(stdout.read().decode('utf-8', 'ignore'))

# 关闭SSHClient
ssh.close()
