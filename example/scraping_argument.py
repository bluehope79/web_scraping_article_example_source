# -*- coding: utf-8 -*-
# file_name : scraping_argument.py

from optparse import OptionParser

def main():
    option = OptionParser(usage='%prog', version='%prog 1.0')

    option.add_option('-k', '--keyword', dest='keyword', type='string', help='Please enter keywords to search')

    (options, args) = option.parse_args()

    if options.keyword is None:
        print ('There are no input arguments.')
        return

    print ('Input arguments : %s' % options.keyword)


if __name__ == '__main__':
    main()
