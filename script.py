
#! /usr/bin/env python3

import os
import requests

url = "http://35.222.148.75/feedback/"
#os.chdir('/data/feedback')
reviews = {}
for file in os.listdir('.'):
    with open(file, 'r', encoding='utf-8') as review:
        review = review.readlines()
        reviews['title'] = review[0].strip()
        reviews['name'] = review[1].strip()
        reviews['date'] = review[2].strip()
        reviews['feedback'] = review[3].strip()
        result = requests.post(url, data=reviews)
        print(result.status_code)

