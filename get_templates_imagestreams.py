import requests
import json

class Online_repo(object):

    def __init__(self):
        # urls for imagestreams/templates of Online Starter/Pro
        self.url_prefix = "https://api.github.com/repos/openshift/online/contents/ansible/roles/oso_template_imagestream_sync/files"
        self.url_starter_is = self.url_prefix + "/starter/imagestreams"
        self.url_starter_template = self.url_prefix + "/starter/templates"
        self.url_pro_is = self.url_prefix + "/pro/imagestreams"
        self.url_starter_template = self.url_prefix + "/pro/templates"

    def get_starter_is(self, token):
        # store the imagestream tag info
        istag_dict = {}
        # HTTP header, including the github token for developers
        headers = {
            'Authorization': 'token ' + token
        }
        # new session
        self.session = requests.session()
        response = self.session.get(self.url_starter_is, headers=headers)
        # json 'loads' to a python list
        json_is = json.loads(response.text)
        # is_item: dict type
        for is_item in json_is:
            response = self.session.get(is_item['download_url'], headers=headers)
            # return dict
            json_response = json.loads(response.text)
            istag_dict[json_response['metadata']['name']] = []
            for tag_item in json_response['spec']['tags']:
                istag_dict[json_response['metadata']['name']].append(tag_item['name'])
        print istag_dict



if __name__ == "__main__":
    token = ''
    starter_is = Online_repo()
    starter_is.get_starter_is(token)
