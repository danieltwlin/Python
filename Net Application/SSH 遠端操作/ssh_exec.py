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

'''
   SSHClient.exec_command 在单独的“exec”通道中执行每个命令。各个命令在各自的环境中运行。
   因此，如果执行cd命令，则对后续命令完全没有影响。它们将再次从用户的主目录开始。
   如果要实现交互式shell session ，请使用 SSHClient.invoke_shell 。
'''
