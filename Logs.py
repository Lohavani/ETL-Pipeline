import logging

#root_logger = logging.getLogger()
#root_logger.setLevel(logging.INFO)

# Setting the log level for the log file and the format of log message
logging.basicConfig(filename = 'C:\\Users\\lose3\\OneDrive - NHS\\Python codes\\ETL\\ETL_Logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log(level, exception):
    if (level == "Info"):
        logging.info(exception)
    if (level == "Error"):
        logging.error(exception)