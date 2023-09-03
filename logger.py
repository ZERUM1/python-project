import logging

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setAge():
        try:
            if 10 > 0:
                
                logging.info('Age set successfully.')
        except:
            logging.error('Error while setting age.')
        

logging.info('This is an informational message')
logging.warning('This is a warning message')