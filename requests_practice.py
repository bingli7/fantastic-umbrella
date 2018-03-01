#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

'''
Practice on 'requests'
'''

my_requests = requests.session()

# set my own cookie
my_requests.get("http://httpbin.org/cookies/set?bingli=redhat")

# return 'requests.models.Response'
my_response = my_requests.get("http://httpbin.org/cookies")

print "type of 'my_response':  ", type(my_response)
print my_response.text


my_requests.get("http://httpbin.org/cookies/delete?bingli")
new_response = my_requests.get("http://httpbin.org/cookies")
print "new cookies:  \n", new_response.text