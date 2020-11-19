# coding=utf-8
import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

import xlrd
from xlutils.copy import copy
from data.data_config import *
class OperationExcel():
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/test_case.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()
    #获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables
    #获取行数
    def get_lines(self):
        tables = self.data
        return tables.nrows
    #获取单元格内容
    def rget_cell_value(self, row, col):
        values = self.data.cell_value(row, col)
        return values

    #往excel里面写入数据
    def write_value(self, row, col, value):
        """
        :param row:行
        :param col:列
        :param value:值
        :return:
        """
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    #根据对应的case_id 找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_values(row_num)
        return row_data

    #根据对应的case_id找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        clos_data = self.get_cols_data()
        for col_data in clos_data:
            if col_data == case_id:
                return num
            num = num + 1

    #根据行号 找到该行的内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    #获取某一列的内容
    def get_cols_data(self):
        tables = self.data
        col_value = tables.col_values(get_id())
        return col_value




if __name__ =='__main__':
    operationg = OperationExcel()
    print(operationg.get_cols_data())
