#!/usr/bin/env python
# -*- coding: utf-8 -*-

import get_templates_imagestreams
import get_openshift_is_template

starter_env = ['free-int', 'free-stg']
pro_env = ['online-int', 'online-stg']

def check_default_is(cluster_id, github_token, openshift_token):
    get_online_repo = get_templates_imagestreams.Online_repo()
    openshift_default = get_openshift_is_template.Get_openshift_is_template(cluster_id)    
    # Get imagestreams from Openshift cluster
    openshift_is = openshift_default.get_default_is(openshift_token)

    if cluster_id in starter_env:
        # Get all the imagestream info from Github and Openshift Starter
        starter_is = get_online_repo.get_starter_is(github_token)

        print 'Checking default imagestreams on ' + cluster_id + ':\n'
        for key1,value1 in starter_is.items():
            if key1 not in openshift_is:
                print 'imagestream ' + key1 + ' does not exist in ' + self.cluster_id
                continue
            if len(starter_is[key1]) != len(openshift_is[key1]):
                print 'some tags of ' + key1 + 'not imported'
            else:
                for tag in value1:
                    if tag in openshift_is[key1]:
                        print key1 + ':' + tag + '  imported'
    # Get imagestreams from Pro
    elif cluster_id in pro_env:
        # Get all the imagestream info from Github and Openshift Pro
        pro_is = get_online_repo.get_pro_is(github_token)
        print 'Checking default imagestreams on ' + cluster_id + ':\n'
        for key1,value1 in pro_is.items():
            if key1 not in openshift_is:
                print 'imagestream ' + key1 + ' does not exist in ' + cluster_id
                continue
            if len(pro_is[key1]) != len(openshift_is[key1]):
                print 'some tags of ' + key1 + 'not imported'
            else:
                for tag in value1:
                    if tag in openshift_is[key1]:
                        print key1 + ':' + tag + '  imported'
    # Wrong cluster id
    else:
        print 'Wrong cluster id!'

def check_default_templates(cluster_id, github_token, openshift_token):
    get_online_repo = get_templates_imagestreams.Online_repo()
    openshift_default = get_openshift_is_template.Get_openshift_is_template(cluster_id)
    # Get templates from Openshift cluster
    openshift_template = openshift_default.get_default_template(openshift_token)

    if cluster_id in starter_env:
        # Get all the templates from Starter Github repo
        starter_templates = get_online_repo.get_starter_templates(github_token)

        print 'Checking default templates on ' + cluster_id + ':\n'
        for t in starter_templates:
            if t in openshift_template:
                print t + ' exists'
            else:
                print t + ' not exists!'
    elif cluster_id in pro_env:
        # Get all the templates from Pro Github repo
        pro_templates = get_online_repo.get_pro_templates(github_token)

        print 'Checking default templates on ' + cluster_id + ':\n'
        for t in pro_templates:
            if t in pro_templates:
                print t + ' exists'
            else:
                print t + ' not exists!'
    else:
        print 'Wrong cluster id!\n'

if __name__ == '__main__':
    # Github private token for developers
    github_token = '*******************'

    cluster_id = 'online-stg'
    openshift_token = '********************'
    # cluster_id = 'free-int'
    # openshift_token = '********************'

    check_default_is(cluster_id, github_token, openshift_token)
    check_default_templates(cluster_id, github_token, openshift_token)
