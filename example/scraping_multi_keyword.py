# -*- coding: utf-8 -*-
# file_name : scraping_multi_keyword.py

from optparse import OptionParser

def search(keywords):
    if keywords.strip() == '':
        return

    for keyword in keywords.split(','):
        # keyword 를 인코딩 한 값을 [2:-1] 로 슬라이싱 하지 않으면, b'' 정보도 같이 출력 된다.
        # - str(keyword.encode('euc-kr'))       : b'%bc%d2%c7%c1%c6%ae%bf%fe%be%ee'
        # - str(keyword.encode('euc-kr'))[2:-1] : %bc%d2%c7%c1%c6%ae%bf%fe%be%ee
        # 그리고, Python 에서 기본으로 인코딩 문자를 \x 로 출력하는데, 이를 % 로 변경해줘야 웹 서버에서 인식을 한다.
        print ('keyword : %s, encoded : %s' % (keyword, str(keyword.encode('euc-kr'))[2:-1].replace('\\x', '%')))

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
