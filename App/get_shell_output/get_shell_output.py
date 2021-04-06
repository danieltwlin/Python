import os

# execute command, and return the output
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


ret  = execCmd('kubectl get pods | grep rnresq')

print( ret）

lst1 = ret.split()

print(lst1)
print(lst1[0])
