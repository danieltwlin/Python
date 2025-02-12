import logging

# console msg
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything

# log file
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')




