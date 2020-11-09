import os
from crontab import CronTab

# Create CronTab
if(1):
        # Create User CronTab
        cron = CronTab(user=True)

        # Create job
        #job = cron.new(command='/opt/lampp/bin/php /home/adas2/www/adas_pdf/index.php adas back index', user='root')
        job = cron.new(command='/opt/lampp/bin/php /home/adas2/www/adas_pdf/index.php adas back index', user='root')

        # Set period: run job  per 1 minute
        job.every(1).minute()

        # Remove log
        #job2 = cron.new(command='rm -r /home/adas2/tmp/logs', user='root')

        # @Monthly
        #job2.setall('0 0 1 1-12 *')

        # Write crontab document
        cron.write()
