# coding=utf-8
import os, sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependentData
from util.send_email import SendEmail
from util.get_login_token import GetLoginToken
import json


class TunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.common_util = CommonUtil()
        self.send_mail = SendEmail()
        self.get_token = GetLoginToken()
        #更新登陆token
        self.get_token.update_token()

    #程序执行主入口
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            print(i)
            url = self.data.get_url(i)
            method = self.data.get_requst_method(i)
            is_run = self.data.is_run(i)
            data = self.data.get_data_for_json(i)
            header = self.data.get_header_for_json(i)
            expect = self.data.get_expcet_data(i)
            depend_case = self.data.is_depend(i)
            # print(header[0])
            # print(type(header[0]))
            if is_run:
                #method, url, data=None, header=None
                # print(res)
                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    #获取的依赖响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    print(depend_response_data)
                    #获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    print(depend_key)
                    print(data) #替换前json源数据
                    data[depend_key] = depend_response_data
                    print(data)#替换后的数据

                res = self.run_method.run_main(method, url, data, header[0]) #h获取数据可以做一个判断
                # print(res)

                if self.common_util.is_contain(expect, res):
                    self.data.write_result(i, 'pass')
                    pass_count.append(i)
                else:
                    self.data.write_result(i, res)
                    fail_count.append(i)
            else:
                print('此条case跳过')
        #发送邮件开关
        # self.send_mail.send_main(pass_count, fail_count)
        # print(len(pass_count))
        # print(len(fail_count))

if __name__ == '__main__':
    run = TunTest()
    print(run.go_on_run())


