#### 한글 로그 파일 만들기
import logging

# 로그 설정
logging.basicConfig(
    filename='my_log.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    encoding='utf-8'  # 로그 파일 인코딩 설정
)

# 로그 예시
logging.info('한글 로그 메시지')