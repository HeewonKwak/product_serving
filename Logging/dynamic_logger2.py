#### chatGPT code
import logging

# 로거 생성
logger = logging.getLogger('my_logger')

# 로그 레벨 설정 (DEBUG 이상 모든 레벨 출력)
logger.setLevel(logging.DEBUG)

# 핸들러 생성 (예: 파일 핸들러)
# handler = logging.FileHandler('my_log.log')
# 핸들러 생성 (예: 콘솔 핸들러)
handler = logging.StreamHandler()

# 로그 포매터 설정 (예: 로그 메시지에는 로그 레벨, 시간, 메시지가 포함됨)
formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(message)s')
handler.setFormatter(formatter)
# print(help(logging.FileHandler))

# 로거에 핸들러 추가
logger.addHandler(handler)

# 로그 메시지 출력
logger.debug('이것은 Debug 레벨의 로그입니다.')