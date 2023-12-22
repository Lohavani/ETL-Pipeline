import logging

# This log file created can be monitored by a cron to run an email notification script that is  
# run after the ETL pipeline, to parse the log file and trigger a notification if there is any error

# This log file created can be parsed to determine the kind of error and rerun certain parts of
# the ETL pipeline if necessary

# Setting the log level for the log file and the format of log message
logging.basicConfig(filename = 'ETL_Logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log(level, exception):
    if (level == "Info"):
        logging.info(exception)
    if (level == "Error"):
        logging.error(exception)