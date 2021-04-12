import os,sys
import datetime


def log_file(file,log,time_flag = False):

        # Get Time Now
        x = datetime.datetime.now()
        #2021/04/12 15:26:23
        dt_now = str(x.year) + '/' + str(x.month).zfill(2) + '/' + str(x.day).zfill(2) + ' ' + str(x.hour).zfill(2) + ':'  +str(x.minute).zfill(2) + ':' +str(x.second).zfill(2)

        # log Time, Msg
        with open(file, 'a') as f:

                if(time_flag):
                        f.write(dt_now + '\n')

                f.write(log + '\n\n')


if __name__=='__main__':

        file = 'testlog.log'
        log = 'test1'
        log_file(file,log,'True')
