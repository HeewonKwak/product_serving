#### 1. logging module 써보기
import logging

logger = logging.getLogger("example")  # root logger
logger.debug("hello debug")         # 로그 출력 X
logger.info("hello info")           # 로그 출력 X
logger.warning("hello warning")     # 로그 출력 O
logger.error("hello error")         # 로그 출력 O
logger.critical("hello critical")   # 로그 출력 O

#### 1.1 logging module config 추가하기
import logging.config

logger_config = {
    "version": 1,  # required
    "disable_existing_loggers": True,  # 다른 Logger를 overriding 합니다
    "formatters": {
        "simple": {"format": "%(asctime)s | %(levelname)s - %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        }
    },
    "loggers": {"example": {"level": "DEBUG", "handlers": ["console"]}},
}

logging.config.dictConfig(logger_config)
logger_with_config = logging.getLogger("example")
logger_with_config.debug("debug 보이죠?")
logger_with_config.info("info 보이죠?")
logger_with_config.warning("warning 보이죠?")
logger_with_config.error("error 보이죠?")
logger_with_config.critical("critical 보이죠?")