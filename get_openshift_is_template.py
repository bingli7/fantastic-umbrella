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
        print 'Getting the default imagestreams...'
        self.session = requests.session()
        response = self.session.get(self.default_is_api, headers=headers)
        # loads to a python dict
        json_response = json.loads(response.text)
        for is_item in json_response['items']:
            # get the is name
            is_dict[is_item['metadata']['name']] = []
            for tag_item in is_item['spec']['tags']:
                is_dict[is_item['metadata']['name']].append(tag_item['name'])
        print 'Successfully get the imagestreams.'

        return is_dict

    def get_default_template(self, token):
        # store the default templates info to a dict
        t_dict = []
        # header with bearer token
        headers = {
            'Authorization': 'Bearer ' + token
            }
        print 'Getting the default templates...'
        self.session = requests.session()
        response = self.session.get(self.default_template_api, headers=headers)
        # loads to a python dict
        json_response = json.loads(response.text)
        for t_item in json_response['items']:
            t_dict.append(t_item['metadata']['name'])
        print 'Successfully get the templates.'

        return t_dict


if __name__ == '__main__':
    # oAuth token to access Openshift API
    token = '*********************************'
    # which environment
    cluster_id = 'free-int'

    online_instance = Get_openshift_is_template(cluster_id)
    default_is = online_instance.get_default_is(token)
    default_template = online_instance.get_default_template(token)
    print default_is
    print default_template