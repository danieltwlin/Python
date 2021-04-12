mport os,sys
import datetime

# write log to file
def log_file(file,log):

        # Get Time Now
        x = datetime.datetime.now()  
        # 2021/04/12 13:56:47
        dt_now = str(x.year) + '/' + str(x.month).zfill(2) + '/' + str(x.day).zfill(2) + ' ' + str(x.hour).zfill(2) + ':'  +str(x.minute).zfill(2) + ':' +str(x.second).zfill(2)

        # log Time, Msg
        with open(file, 'a') as f:
                #f.write('Hello, world!')
                f.write(dt_now + '\n')
                f.write(log + '\n\n')


if __name__=='__main__':

        file = 'logfile.log'
        log = 'test1'
        log_file(file,log)
