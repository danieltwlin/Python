import os
import datetime


def get_time():

        x = datetime.datetime.now()
        #
        dt_now = str(x.year) +  str(x.month).zfill(2) + str(x.day).zfill(2) + str(x.hour).zfill(2) + str(x.minute).zfill(2) + str(x.second).zfill(2)
        print(dt_now)

        # 2021/04/12 13:56:47
        # dt_now = str(x.year) + '/' + str(x.month).zfill(2) + '/' + str(x.day).zfill(2) + ' ' + str(x.hour).zfill(2) + ':'  +str(x.minute).zfill(2) + ':' +str(x.second).zfill(2)

        hour =x.hour

        return hour

if __name__=="__main__":
        hour=get_time()
        print(hour)
