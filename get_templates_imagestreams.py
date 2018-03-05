import requests
import json

class Online_repo(object):

    def __init__(self):
        # urls for imagestreams/templates of Online Starter/Pro
        self.url_prefix = "https://api.github.com/repos/openshift/online/contents/ansible/roles/oso_template_imagestream_sync/files"
        self.url_starter_is = self.url_prefix + "/starter/imagestreams"
        self.url_starter_template = self.url_prefix + "/starter/templates"
        self.url_pro_is = self.url_prefix + "/pro/imagestreams"
        self.url_pro_template = self.url_prefix + "/pro/templates"


    def get_starter_is(self, token):

        """
        Get all the imagestream tags from Online Starter's Github Repository
        """

        # dict to store all the imagestream tag info
        istag_dict = {}
        # HTTP header, including the personal github token
        headers = {
            'Authorization': 'token ' + token
        }
        print "Get the imagesteam tags from Online Starter repository: \n"

        self.session = requests.session()
        # Get from the Github API
        response = self.session.get(self.url_starter_is, headers=headers)
        # json 'loads' to a python list. Every element is for one imagestream
        json_is = json.loads(response.text)

        for is_item in json_is:
            # Get the real is file from the download link
            response = self.session.get(is_item['download_url'], headers=headers)
            json_response = json.loads(response.text)
            # key:imagestream name; value:list of tags
            istag_dict[json_response['metadata']['name']] = []
            # tag_item is tag list
            for tag_item in json_response['spec']['tags']:
                istag_dict[json_response['metadata']['name']].append(tag_item['name'])

        print "Successfully get Starter's imagestreamtags:\n"
        print istag_dict

    def get_starter_templates(self, token):

        """
        Get all the templates from Online Starter's Github Repository
        """

        # list to store all the templates info
        templates_list = []
        # HTTP header, including the personal github token
        headers = {
            'Authorization': 'token ' + token
        }
        print "Get the templates from Online Starter repository: \n"

        self.session = requests.session()
        # Get from the Github API
        response = self.session.get(self.url_starter_template, headers=headers)
        # json 'loads' to a python list. Every element is for one template
        json_templates = json.loads(response.text)

        for t_item in json_templates:
            # Get the real template file from the download url
            response = self.session.get(t_item['download_url'], headers=headers)
            json_response = json.loads(response.text)
            templates_list.append(json_response['metadata']['name'])

        print templates_list


if __name__ == "__main__":
    # Personal access tokens for Github
    token = '********************'
    starter_is = Online_repo()
    # Get imagestreams of Online Starter
    starter_is.get_starter_templates(token)
