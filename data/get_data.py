# coding=utf-8
import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from util.operation_excel import OperationExcel
from data.data_config import *
from util.operation_json import OperationJson
class GetData():
    def __init__(self):
        self.oper_excel = OperationExcel()

    #获取case数
    def get_case_lines(self):
        return self.oper_excel.get_lines()

    #获取是否执行case
    def is_run(self, row):
        flag = None
        col = get_run()
        run_model = self.oper_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #case是否携带header[优化]
    def is_header(self, row):
        col = get_header()
        header = self.oper_excel.get_cell_value(row, col)
        # if header == 'yes':
        #     return get_header_value()
        # else:
        #     return None
        return header

    #通过关键字获取header

    def get_header_for_json(self, row):
        opera_json = OperationJson()
        header = opera_json.get_data(self.is_header(row))
        return header


    #case请求方式

    def get_requst_method(self, row):
        col = get_request_way()
        request_method = self.oper_excel.get_cell_value(row, col)
        return request_method

    #case url
    def get_url(self, row):
        col = get_url()
        url = self.oper_excel.get_cell_value(row, col)
        return url

    #case body
    def get_request_data(self, row):
        col = get_data()
        data = self.oper_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    #通过关键字获取body
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    #获取预期结果
    def get_expcet_data(self, row):
        col = get_expect()
        expect = self.oper_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    def write_result(self, row, value):
        col = get_result()
        self.oper_excel.write_value(row, col, value)


    #获取依赖数据的key
    def get_depend_key(self, row):
        col = get_data_depend()
        depend_key = self.oper_excel.get_cell_value(row, col)
        if depend_key == '':
            return None
        else:
            return depend_key

    #判断是否有case依赖
    def is_depend(self, row):
        col = get_case_depend()
        depend_case_id = self.oper_excel.get_cell_value(row, col)
        if depend_case_id == '':
            return None
        else:
            return depend_case_id

    #获取数据依赖字段
    def get_depend_field(self, row):
        col = get_field_depend()
        data = self.oper_excel.get_cell_value(row, col)
        if data == '':
            return None
        else:
            return data


if __name__ == '__main__':
    getdata = GetData()
    lines = getdata.get_case_lines()
    # url = getdata.get_url(getdata.get_case_lines())
    # print(url)
    # print(getdata.get_case_lines())
    for i in range(1, lines):
        print(getdata.get_url(i))
        print(getdata.get_request_data(i))