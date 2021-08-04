import logging

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(level=logging.DEBUG, filename='myLog.log',format=FORMAT)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')



# logging.basicConfig(level=logging.DEBUG, filename='myLog.log', filemode='w', format=FORMAT)
