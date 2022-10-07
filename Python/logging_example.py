import logging


logging.basicConfig(filename='app.log',format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p',  level=logging.DEBUG)
logging.info('Gross Commission < 0.1% with 0 commission')
logging.warning('Data does not match with CRM system file')
logging.error('Service Type not match,Please info DE team know.')


"""
a = 5
b = 0
try:
  c = a / b
except Exception as e:
  logging.exception("Exception occurred")
"""



# Logger 
# reference : https://docs.python.org/3/library/logging.html 

# Lib - Logger 
# https://docs.python.org/3/library/logging.html
