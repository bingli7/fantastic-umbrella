#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

class Get_openshift_is_template(object):
    """
    Get the default imagestreams and tempaltes under openshift namespace
    """
    def __init__(self, cluster_id):
        self.api = "https://api." + cluster_id + ".openshift.com"
        self.default_is_api = self.api + '/apis/image.openshift.io/v1/namespaces/openshift/imagestreams'
        self.default_template_api =  self.api + '/apis/template.openshift.io/v1/namespaces/openshift/templates'

    def get_default_is(self, token):
        # store the default imagestreamtag info to a dict
        is_dict = {}
        # header with bearer token
        headers = {
            'Authorization': 'Bearer ' + token
            }
        self.session = requests.session()
        response = self.session.get(self.default_is_api, headers=headers)
        # loads to a python dict
        json_response = json.loads(response.text)
        for is_item in json_response['items']:
            # get the is name
            is_dict[is_item['metadata']['name']] = []
            for tag_item in is_item['spec']['tags']:
                is_dict[is_item['metadata']['name']].append(tag_item['name'])
        print is_item



    def get_default_template(self, token):
        pass

if __name__ == '__main__':
    # oAuth token to access Openshift API
    token = '**********************'

    online_instance = Get_openshift_is_template('free-int')
    online_instance.get_default_is(token)