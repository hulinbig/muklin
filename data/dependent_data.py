# coding=utf-8
import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
from util.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse #解析层级关系
import json

class DependentData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.run_method = RunMethod()
        self.data = GetData()


    #通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    #执行依赖测试,获取结果
    def run_dependent(self):
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.get_header_for_json(row_num)

        url = self.data.get_url(row_num)
        method = self.data.get_requst_method(row_num)
        # print(row_num, request_data, header, url, method)
        res = self.run_method.run_main(method, url, request_data, header[0])
        return json.loads(res)

    #根据依赖的key去获取依赖测试case的请求值且返回
    def get_data_for_key(self, row):
        depend_data = self.data.get_depend_key(row)
        #打印正则
        # print(depend_data)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        #打印通过正则而得到的结果
        # print(madle)

        return [math.value for math in madle][0]


if __name__ == '__main__':
    depend = DependentData('test_06')
    print(depend.get_data_for_key(7))
    # print(depend.run_dependent())

