import logging

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(level=logging.DEBUG, filename='myLog.log',format=FORMAT)
# logging.basicConfig(level=logging.DEBUG,format=FORMAT)  # 不要logfile，就不要設定 filename
# logging.basicConfig(level=logging.CRITICAL,format=FORMAT)   # 嚴重 Error 才輸出

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')



# logging.basicConfig(level=logging.DEBUG, filename='myLog.log', filemode='w', format=FORMAT)
# level 設成 INFO, 則 Debug 不會輸出
