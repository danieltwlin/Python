# coding=utf-8
import sys

# Python 带参执行脚本

if __name__ == "__main__":
        print(sys.argv)      #   print argv
        print(len(sys.argv)) #   argv len

        if(len(sys.argv)>1):
                print(sys.argv[1])   #   print first argv

# sys.argv[0] 即是脚本文件路径和名称，
# sys.argv[1]开始是传入脚本的参数，参数个数可变。
