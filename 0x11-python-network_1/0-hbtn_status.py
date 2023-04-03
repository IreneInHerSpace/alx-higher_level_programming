#!/usr/bin/python3

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
        html = response.read()
<<<<<<< HEAD


=======
        
        
>>>>>>> d00a07ebf80c8e1384480bef7428bc72e88420a6
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf-8')))
