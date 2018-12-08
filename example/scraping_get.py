# -*- coding: utf-8 -*-
# file_name : scraping_get.py

import requests
from bs4 import BeautifulSoup
from optparse import OptionParser

SEARCH_URL = "http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=&bidNm=%s&searchDtType=1&fromBidDt=2018/10/27&toBidDt=2018/11/26&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1"

def scraping(keyword):
    response = requests.get(SEARCH_URL % keyword)
    soup = BeautifulSoup(response.text, 'html5lib')

    titles = soup.select("#resultForm > div.results > table > tbody > tr > td > div > a")

    for i, title in enumerate(titles):
        # 위의 구분자로 정확한 값을 추출할 수가 없다.
        # 프로그램을 실행시켜보면, 다음과 같이 두 쌍의 데이터가 출력이 된다.
        # - <a href="http://www.g2b.go.kr:8081/ep/invitation/publish/bidInfoDtl.do?bidno=20181133004&amp;bidseq=00&amp;releaseYn=Y&amp;taskClCd=5 ">20181133004-00</a>
        # - <a href="http://www.g2b.go.kr:8081/ep/invitation/publish/bidInfoDtl.do?bidno=20181133004&amp;bidseq=00&amp;releaseYn=Y&amp;taskClCd=5 ">지진해일 경보시스템 소프트웨어 기능개선 용역</a>
        # 첫번째 데이터는 날짜에 대한 값으로 이와 같은 형태가 반복되니, 약간의 로직을 추가하여, 짝수 번째 데이터만 출력되게 한다.
        if i % 2 == 0:
            continue

        print ('title : %s\n - link : %s' % (title.text, title.get('href').strip()))

def search(keywords):
    if keywords.strip() == '':
        return

    for keyword in keywords.split(','):
        # keyword 를 인코딩 한 값을 [2:-1] 로 슬라이싱 하지 않으면, b'' 정보도 같이 출력 된다.
        # - str(keyword.encode('euc-kr'))       : b'%bc%d2%c7%c1%c6%ae%bf%fe%be%ee'
        # - str(keyword.encode('euc-kr'))[2:-1] : %bc%d2%c7%c1%c6%ae%bf%fe%be%ee
        # 그리고, Python 에서 기본으로 인코딩 문자를 \x 로 출력하는데, 이를 % 로 변경해줘야 웹 서버에서 인식을 한다.
        encoded_keyword = str(keyword.encode('euc-kr'))[2:-1].replace('\\x', '%')
        scraping(encoded_keyword)

def main():
    option = OptionParser(usage='%prog', version='%prog 1.0')

    option.add_option('-k', '--keywords', dest='keywords', type='string', help='Please enter keywords to search')

    (options, args) = option.parse_args()

    if options.keywords is None:
        print ('There are no input arguments.')
        return

    search(options.keywords)


if __name__ == '__main__':
    main()
