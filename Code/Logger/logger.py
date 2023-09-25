from csv_logger import CsvLogger
import logging
from time import sleep

filename = 'logs/log.csv'
delimiter = ','
level = logging.INFO
custom_additional_levels = ['logs_a', 'logs_b', 'logs_c']
fmt = f'%(asctime)s{delimiter}%(levelname)s{delimiter}%(message)s'
datefmt = '%d/%m/%Y %H:%M:%S'
max_size = 1024  # 1 kilobyte
max_files = 4  # 4 rotating files
header = ['date', 'level', 'value_1', 'value_2']

# Creat logger with csv rotating handler
csvlogger = CsvLogger(filename=filename,
                      delimiter=delimiter,
                      level=level,
                      add_level_names=custom_additional_levels,
                      add_level_nums=None,
                      fmt=fmt,
                      datefmt=datefmt,
                      max_size=max_size,
                      max_files=max_files,
                      header=header)

