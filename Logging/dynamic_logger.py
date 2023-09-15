#### 1.2 dynamic logging config
import logging
import sys

dynamic_logger = logging.getLogger()
dynamic_logger.debug('debug check')
dynamic_logger.info('info check')
dynamic_logger.setLevel(logging.DEBUG)
# setLevel은 addHandler를 해야 출력 됨
dynamic_logger.debug('debug check')
dynamic_logger.info('info check')
log_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log_handler.setFormatter(formatter)
dynamic_logger.addHandler(log_handler)

dynamic_logger.info("hello world")