# coding=utf-8

from mock import mock
#模拟mock，封装方法完成
def mock_test(mock_method, request_data, url, response_data):
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url, request_data)
    return res
