import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start the Program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))