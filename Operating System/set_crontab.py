import os
from crontab import CronTab
import datetime

def log_time():

        x = datetime.datetime.now()
        #..
        dt_now = str(x.year) +  str(x.month).zfill(2) + str(x.day).zfill(2) + str(x.hour).zfill(2) + str(x.minute).zfill(2) + str(x.second).zfill(2)
        print(dt_now)

        # ...........
        f = open("/opt/py/output.txt", "a")

        #......
        f.write(dt_now)
        f.write("\n")

        f.close()


log_time()


# Create CronTab
if(1):
        # Create User CronTab
        cron = CronTab(user=True)

        # Create job
        #job = cron.new(command='/opt/lampp/bin/php /home/adas2/www/adas_pdf/index.php adas back index', user='root')
        #job = cron.new(command='python log_time.py', user='root')


        # Set period: run job  per 1 minute
        job.every(1).minute()

        # Remove log
        #job2 = cron.new(command='rm -r /home/adas2/tmp/logs', user='root')

        # @Monthly
        #job2.setall('0 0 1 1-12 *')

        # Write crontab document
        cron.write()

