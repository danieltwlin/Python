from datetime import datetime

# GMT string to GMT Time

dateString = "Oct 28 23:59:59 2020 GMT"
dateFormatter = "%b %d %H:%M:%S %Y GMT"
print(datetime.strptime(dateString, dateFormatter))
