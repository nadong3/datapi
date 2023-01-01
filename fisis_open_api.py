# 금융통계정보시스템 데이터 가져오기 연습
# url : http://fisis.fss.or.kr/openapi/statisticsInfoSearch.
# 인증KEY : 4fcb334d9dc5745fc188b748b3a12ae3

import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup

# API로 데이터 불러오기 변수 선언
인증키   = '4fcb334d9dc5745fc188b748b3a12ae3'

통계정보API_URL = 'http://fisis.fss.or.kr/openapi/statisticsInfoSearch.'
금융회사API_URL = 'http://fisis.fss.or.kr/openapi/companySearch.'

응답방식 = 'json'
언어    = 'kr'

인증키   = '4fcb334d9dc5745fc188b748b3a12ae3'

params ={ 'serviceKey' : 'oq/77deE3mUMPiXUdTCAd3bnjO/IAnnJWivxggRowD1aUCpPcpfq1BHtVuBlSU2t7LKzx6h2mWX50H9kaBf9QA=='
        , 'numOfRows' : '2'
        , 'pageNo' : '1'
        , 'resultType' : 'json'
        , 'title' : '저축_일반현황_임직원현황'
        , 'basYm' : '202112' }

response = requests.get(url, params=params)

#bs파싱 = BeautifulSoup(response.text, "html.parser")

#print(bs파싱)

json_res1 = json.loads(response.text)
json_res2 = json_res1['response']
json_res3 = json_res2['body']
json_res4 = json_res3['tableList']
json_res5 = json_res4[0]
json_res6 = json_res5['items']
json_res7 = json_res6['item']
pprint(json_res7)
pprint(type(json_res7))
pprint(len(json_res7))


#저축은행임직원현황List
저축은행임직원현황List = []

for item in json_res7:
    기준년월       = item["basYm"]
    법인등록번호    = item["crno"]
    금융회사코드    = item["fncoCd"]
    금융회사명      = item["fncoNm"]
    임직원수       = item["xcsmCnt"]
    임직원구분코드   = item["xcsmDcd"]
    임직원구분코드명 = item["xcsmDcdNm"]
    저축은행임직원현황List.append([기준년월, 법인등록번호, 금융회사코드, 금융회사명, 임직원수, 임직원구분코드, 임직원구분코드명])

print(*저축은행임직원현황List)

# 테스트 출력
#pprint(response)

#bs파싱 = BeautifulSoup(response.text, "html.parser")
#pprint(bs파싱.prettify())

#print(bs파싱.find('item').get_text())

#print(bs파싱.find_all("items"))

#저축은행임직원현황List = []
#for item in bs파싱.find_all("item"):
#    기준년월       = item.find("basYm").text
#    법인등록번호    = item.find("crno").text
#    금융회사코드    = item.find("fncoCd").text
#    금융회사명      = item.find("fncoNm").text
#    임직원수       = item.find("xcsmCnt").text
#    임직원구분코드   = item.find("xcsmDcd").text
#    임직원구분코드명 = item.find("xcsmDcdNm").text
#    저축은행임직원현황List.append([기준년월, 법인등록번호, 금융회사코드, 금융회사명, 임직원수, 임직원구분코드, 임직원구분코드명])

#print(*저축은행임직원현황List)
#city_df = pd.DataFrame(cityList, columns= ["cityCode", "cityName"])
#city_df.head()






#인증
#with requests.Session() as sess:
#    sess.post(f"https://sgisapi.kostat.go.kr/OpenAPI3/auth/authentication.json")
#인증주소 = "https://sgisapi.kostat.go.kr/OpenAPI3/auth/authentication.json"
#인증결과 = requests.get(인증주소)
#print(인증결과.status_code)
#print(인증결과)

#urls = 'https://sgisapi.kostat.go.kr/OpenAPI3/stats/population.json'

#headers = {
# 'aa'   
#}

#print("aa")
#pprint "aa"