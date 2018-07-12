# -*- coding:utf-8 -*-
"""
DATE: 2018-07-12
"""
import unittest
from unittest.mock import patch
import PullDataOfWeibo


class MyTestCase(unittest.TestCase):

    @patch("os.getcwd")
    @patch("PullDataOfWeibo.fetch_data")
    def test_run(self, mock_fetch_data, mock_getcwd):
        mock_getcwd.return_value = "D:\scripts\PullDataOfWeibo"
        mock_fetch_data.return_value = '{"id":"657","content":"#\u96c5\u601d\u53e3\u8bed#\u96c5\u601d\u53e3\u8bed\u4e3a\u4ec0\u4e48\u4f60\u7684\u5206\u6570\u90a3\u4e48\u4f4e","add_time":"2018-05-15 11:15:28","img_url":["http:\/\/data.100zhaosheng.com\/uploads\/images\/weibo\/20180515\/headerimg1526354128494236.png","http:\/\/data.100zhaosheng.com\/uploads\/images\/weibo\/20180515\/headerimg1526354128150948.png","http:\/\/data.100zhaosheng.com\/uploads\/images\/weibo\/20180515\/headerimg1526354128521976.png","http:\/\/data.100zhaosheng.com\/uploads\/images\/weibo\/20180515\/contentimg1526354128861891.png","http:\/\/data.100zhaosheng.com\/uploads\/images\/weibo\/20180515\/contentimg1526354128296693.png"]}'
        PullDataOfWeibo.run()


if __name__ == "__main__":
    unittest.main()
