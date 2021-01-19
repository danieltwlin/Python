import paramiko

ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 建立连接
ssh.connect("xx.xx.xx.xx", username="root", port=22, password="you_password")

# 使用这个连接执行命令
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ls -l")

# 获取输出
print(ssh_stdout.read())

# 关闭连接
ssh.close()


#  pip install paramiko
