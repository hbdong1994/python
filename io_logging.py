import os
import platform
import logging

# print platform.platform()

if platform.platform().startswith('Windows'):
    log_file = os.path.join(os.getcwd(),  # os.getcwd() get the location of current script
                            'test.log'
                            )

logging.basicConfig(   # logging config
    level=logging.DEBUG,  # logging level DEBUG is all log
    format='[%(asctime)s][%(levelname)s] \t: %(message)s',
    filename=log_file,
    filemode='ab+'  # 'w' only write 'r' only read  'a' append to file
)

logging.debug('start to logging ')
logging.info('Doing something')
logging.error('this is error log')
logging.warning('this is warning log')
logging.debug('Stop')
