import logging
import os 
from datetime import datetime 
'''  This logging file is necessary :
Imagine running a restaurant without keeping track of orders or feedback — it would be chaos! 
The logger ensures every significant event is recorded. '''


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok = True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(

    filename =LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,



)



    