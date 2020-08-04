from datetime import datetime

# GMT string to GMT Time

dateString = "Oct 28 23:59:59 2020 GMT"
dateFormatter = "%b %d %H:%M:%S %Y GMT"
print(datetime.strptime(dateString, dateFormatter))


# GMT Time to GMT String

x = datetime.now()       #現在時間
print(x.strftime("%Y-%m-%d %H:%M:%S"))
# x = datetime(2018, 6, 1)    # 設定 datetime 物件的時間
