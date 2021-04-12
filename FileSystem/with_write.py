# 用 with 寫入檔案
with open('/opt/test.txt', 'w') as f:
    f.write('Hello, world!')  
    
    
# 附加寫入檔尾
with open('/opt/test.txt', '') as f:
    f.write('Hello, world!')  
    
# 設定編碼 
with open(name, 'r', encoding='UTF-8') as f:
    content = f.read()
    print(content)
