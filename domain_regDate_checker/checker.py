import urllib.request
import xml.etree.ElementTree as ET
import json
from datetime import datetime

def date_diff_too_short(domain, whois_key):
    try:
        #XML

        # 요청을 보내고 응답을 받습니다
        query = "http://apis.data.go.kr/B551505/whois/domain_name?serviceKey=" + whois_key + "&query="+ domain + "&answer=xml";
        request = urllib.request.urlopen(query).read().decode("utf-8")

        # XML 파일을 파싱합니다.
        root = ET.fromstring(request)
        
        # <regDate> 태그를 찾아 날짜 텍스트를 date_text에 저장합니다.
        for date in root.iter('regDate'):
            date_text = date.text
            break

        # 오늘 날짜를 가져옵니다.
        today = datetime.today()
        
        # 날짜 텍스트를 날짜 변수로 바꿉니다.
        regDate = datetime.strptime(date_text, "%Y. %m. %d.")
        
        # 날짜 차이를 계산합니다
        difference = today - regDate  
        
        # 등록일과 오늘 날짜가 1달(30일)도 차이가 안 나면 True, 아니면 False 반환
        if difference.days < 30:
            return True
        else:
            return False
    except:
        try:
            #JSON

            # 요청을 보내고 응답을 받습니다
            query = f"http://apis.data.go.kr/B551505/whois/domain_name?serviceKey={whois_key}&query={domain}&answer=json"
            request = urllib.request.urlopen(query).read().decode("utf-8")

            # JSON 파일을 파싱합니다.
            data = json.loads(request)
            
            # date 값을 찾아 날짜 텍스트를 date_text에 저장합니다.
            date_text = data.get("whois", {}).get("regDate", "")

            # 이하동문
            today = datetime.today()
            
            regDate = datetime.strptime(date_text, "%Y. %m. %d.")
            
            difference = today - regDate  
            
            if difference.days < 30:
                return True
            else:
                return False
        except:
            # 해외에서 관리하는 도메인(.net, .com 등)은 지원하지 않음
            return None
