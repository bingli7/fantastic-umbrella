#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

class Openshift_operation(object):
    """
    CRUD operation on Openshift objects
    """
    def __init__(self, cluster_id, token):
        self.cluster_id = cluster_id
        self.token = token
        self.api_url = "https://api." + self.cluster_id + ".openshift.com"
        # All the endpoint url
        self.project_api_url = self.api_url + '/apis/project.openshift.io/v1/projects'

    def new_project(self, project_name):
        post_data = {
            "kind": "Project",
            "apiVersion": "v1",
            "metadata": {
                "name": project_name
                },
            "spec": {
                "finalizers": [
                    "openshift.io/origin",
                    "kubernetes"
                    ]
                }
            }
        headers = {
            'Authorization': 'Bearer ' + token
            }
        newsession = requests.session()
        response = newsession.post(self.project_api_url, headers=headers, data=post_data)
        print response.status_code
        print response.text

if __name__ == '__main__':

    cluster_id = 'online-stg'
    token = '**************************'

    os_object = Openshift_operation(cluster_id, token)
    os_object.new_project('djfskdksls')