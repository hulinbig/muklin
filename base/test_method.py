# coding=utf-8
import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
import unittest
from base.HTMLTestReport import HTMLTestRunner
from base.demo01 import Method
from base.mock_demo import mock_test
import time
import os
class TestMethod(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print('类执行之前的方法')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('类执行之后的方法')
    #
    def setUp(self):
        self.test = Method()
        # print('test is setup')
    #
    # def tearDown(self):
    #     print('test is teardown')


    def test_01(self):
        url = "https://api.fachans.com/apiweb/case/prolist"
        request_data = {"page_num": 1, "page_size": 10}
        response_data = {"page_num": 1}
        # self.test.post = mock.Mock(return_value=data)
        # result = self.test.post(url, data)
        result = mock_test(self.test.post, request_data, url, response_data)
        print(result)
        #if 语句判断法
        # if result['count'] == 927:
        #     print('test is pass')
        # else:
        #     print('test is fur')
        # print(result)
        self.assertEqual(result['page_num'], 1, msg='test is not pass')
        # self.assertEqual(result['count'], 927, msg='test is not pass')
        # print('this is first case')

    # @unittest.skip('test_02')
    def test_02(self):
        url = "https://api.fachans.com/apiweb/case/prolist"
        data = {}
        result = self.test.post(url, data)
        # print(result)
        self.assertEqual(result['count'], 927, msg='test is not pass')
        # print('this is second case')

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    filename = "../report/"+"testresult"+now+".html"
    print(filename)
    # unittest.main()
    fp = open(filename, 'wb')
    print(fp)
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    runner = HTMLTestRunner(stream=fp, title='this is report', description='用例执行情况：')
    runner.run(suite)
    fp.close()


    # unittest.TextTestRunner().run(suite)  跑所有的case
