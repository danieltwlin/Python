import os

# 要檢查的檔案路徑
filepath = "/etc/motd"

# 檢查檔案是否存在
if os.path.isfile(filepath):
  print("檔案存在。")
else:
  print("檔案不存在。")
os.path.isfile 對於一般檔案以及連結檔案都會傳回 True，如果想判斷檔案是否屬於連結檔，可以再加上 os.path.islink 的判斷：

# 檢查是否為連結檔
if os.path.islink(filepath):
  print("連結檔。")
else:
  print("非連結檔。")
  
# os.path.isdir 對於目錄以及連結到目錄的連結檔都會傳回 True，
# 若要判斷是否為連結檔，同樣可使用 os.path.islink。


#檢查路徑是否存在
#若只是想要查看特定的路徑是否存在，不分檔案或目錄，則可使用 os.path.exists：
# 要檢查的檔案路徑
filepath = "/etc/motd"

# 檢查路徑是否存在
if os.path.exists(filepath):
  print("路徑存在。")
else:
  print("路徑不存在。")
