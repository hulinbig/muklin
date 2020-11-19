# coding=utf-8
import requests
import json
import urllib.parse
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class RunMethod():
    def __init__(self):
        pass

    def post_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=json.dumps(data), headers=header, verify=False).json()
        else:
            res = requests.post(url=url, data=json.dumps(data), verify=False).json()
        return res

    def get_main(self, url, data=None, header=None):
        res = None
        data = urllib.parse.urlencode(data)
        url = url + '?' + data
        if header != None:
            res = requests.get(url, headers=header).json()
        else:
            res = requests.get(url).json()
        return res

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, sort_keys=True, indent=2)

