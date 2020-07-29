
import datetime,time

# Start Time
starttime = datetime.datetime.now()

#long running
time.sleep(2)

# Get Total Time
endtime = datetime.datetime.now()
print((endtime - starttime).seconds)

# Time Format
seconds = (endtime - starttime).seconds
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print("%02d:%02d:%02d" % (h, m, s))


# datetime中的常見類
#
#（1）datetime.date 表示日期，常用的屬性有：year, month和day
#
#（2）datetime.time 表示時間，常用屬性有：hour, minute, second,
