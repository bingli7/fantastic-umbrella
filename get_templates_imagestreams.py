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
        # HTTP header
        self.headers = {
            'Authorization': 'token ' + token
        }
        # new session
        self.session = requests.session()
        response = self.session.get(self.url_starter_is, headers=self.headers)
        # json 'loads' to a python list
        json_is = json.loads(response.text)
        for is_item in json_is:
            response = self.session.get(is_item['download_url'], headers=self.headers)
            json_response = json.loads(response.text)
            print type('json_response')
            print json_response['metadata']['name']
            is_dict = {
                    json_response['metadata']['name']: []
                }
#            for tag_item in json_response['spec']['tags']:




if __name__ == "__main__":
    token = '63e01599454421ada46186a8a9415288b5d993e5'
    starter_is = Online_repo()
    starter_is.get_starter_is(token)