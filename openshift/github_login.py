#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import etree
try:
    import cookielib
except:
    import http.cookiejar as cookielib

"""
Login Github and save cookies
"""

class Github_login(object):

    def __init__(self):
        self.login_url = "https://github.com/login"
        self.post_url = "https://github.com/session"

        # get header from browser
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
            'Connection': 'keep-alive',
            'Host': 'github.com',
            'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
            }
        # new session
        self.session = requests.session()
        # cookie file
        self.session.cookies = cookielib.LWPCookieJar(filename='github_cookie')

    # get authenticity_token
    def get_token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        html = etree.HTML(response.text)
        authenticity_token = html.xpath('//div/input[2]/@value')
        print 'authenticity_token: ', authenticity_token
        return authenticity_token

    # post
    def post_session(self, username, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.get_token()[0],
            'login': username,
            'password': password
            }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        self.session.cookies.save()

    # check if already log in successfully
    def check_login(self):
        try:
            self.session.cookies.load(ignore_discard=True)
        except:
            print "fail to get cookie!"
        profileUrl = "https://github.com/settings/profile"
        response = self.session.get(profileUrl, headers=self.headers)
        selector = etree.HTML(response.text)
        info = selector.xpath('//div[@class="column two-thirds"]/dl/dd/input/@value')
        # Print personal info
        print(u'Your profile: %s' % info)

if __name__ == "__main__":
    mylogin = Github_login()
    mylogin.post_session('username', "password")
    mylogin.check_login()
