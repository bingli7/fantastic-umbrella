#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

"""
Practice on 'requests'
"""

def test_cookies():
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

def test_operation():
	r = requests.put("http://httpbin.org/put")
	print "put: ", r.text
	r = requests.delete("http://httpbin.org/delete")
	print "delete: ", r.text
	r = requests.head("http://httpbin.org/get")
	print "get: ", r.text
	r = requests.post("http://httpbin.org/post")
	print "post: ", r.text

def test_get_post():
	payload = {
		'key1': 'value1',
		'key2': 'value2'
		}
	# use params
	r = requests.get("http://httpbin.org/get", params=payload)
	print r.text	
	# post
	r2 = requests.post("http://httpbin.org/post?bingli=redhat")
	print r2.text
	print dir(r2)
	# get
	r3 = requests.get("http://httpbin.org/get?key3=value3&key4=value4")
	print r3.text
	# status code
	r4 = requests.get('http://httpbin.org/get')
	print r.status_code == requests.codes.ok

def test_json():
	url = "https://raw.githubusercontent.com/openshift/origin/master/examples/hello-openshift/hello-pod.json"
	r = requests.get(url)

	# type 'dict'
	print type(r.json())
	print r.json()
	# type 'unicode'
	print type(r.text)
	print r.text

if __name__ == "__main__":
	test_json()