# coding=utf-8
import json

class OperationJson():
    def __init__(self, filename=None):
        if filename:
            self.filename = filename
        else:
            self.filename = "../dataconfig/get_process.json"
        self.data = self.get_json_data()

    #读取json文件
    def get_json_data(self):
        with open(self.filename, encoding='utf-8') as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self, id):
        return self.data[id]

if __name__ == '__main__':
    op = OperationJson()
    print(op.get_data('Content-Type'))