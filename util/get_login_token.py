# coding=utf-8
import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class GetLoginToken:
    def __init__(self):
        self.data = self.get_login_token()

    #如果登录失效 跟新token和client_login
    def login(self):
        url = "https://api.fachans.com/login/password/verify"
        header = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
        body = {"username": "18582450815", "password": "hulin01234", "grant_type": "password", "client_source": "1", "client_id": "ppO60vjdP5SsxIuNp96S44Avu2lQBzm6tkRLAITQvZs=", "client_secret": "weOM5Gg9eO7IHbXj5avfSDHzwb28TDphYja83VLBakY2gRQB57Csqj2WkCBNa12N"}
        #这里必须加verify=False，关闭证书验证
        result = requests.post(url=url, data=json.dumps(body), headers=header, verify=False).json()
        return result
    def get_login_token(self):
        login_token = self.login()['access_token']
        login_client_logo = self.login()['client_logo']
        login_token = "Bearer " + login_token
        mes = [login_token, login_client_logo]
        return mes
        # print(login_token)
        # print(login_client_logo)

    def get_token(self):
        token = self.data[0]
        return token

    def get_clent_logo(self):
        clent_logo = self.data[1]
        return clent_logo

    def update_token(self):
        with open("../dataconfig/get_process.json", 'r', encoding='utf-8') as load_f:
            old_header = json.load(load_f)
        old_header['header'][0]['Authorization'] = self.get_token()
        old_header['header'][0]['Client-Logo'] = self.get_clent_logo()

        # print(old_header)
        with open("../dataconfig/get_process.json", "w", encoding='utf-8') as dump_f:
            json.dump(old_header, dump_f)



if __name__ == "__main__":
    get_token = GetLoginToken()
    get_token.update_token()



