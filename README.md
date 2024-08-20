작업 디렉토리 내에 git clone하기


코드에 경로 추가하기

import sys

sys.path.append('git clone해서 받은 디렉토리의 경로 입력')


import하기

from domain_regDate_checker.checker import date_diff_too_short


등록일을 찾고 싶은 도메인과 API 등록 키를 입력

result = date_diff_too_short(domain, whois_key)


등록일로부터 30일이 안 지났으면 True, 지났으면 False를 반환함







# text.py


import sys

sys.path.append('C:/Users/user/Desktop/Project/domain_regDate_checker')


from domain_regDate_checker.checker import date_diff_too_short


domain = 'kisa.or.kr'

whois_key = '본인 등록 키 입력'


result = date_diff_too_short(domain, whois_key)

print(result)
