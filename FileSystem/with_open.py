with open('/path/to/file', 'r') as f:
    print(f.read())

    
# with 的寫法，相當於下面的寫法，with語句來自動幫我們調用close()方法：

# 由於文件讀寫時都有可能產生IOError，一旦出錯，後面的f.close()就不會調用。所以，為了保證無論是否出錯都能正確地關閉文件，我們可以使用try ... finally來實現：
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()    
