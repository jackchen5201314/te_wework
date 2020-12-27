import requests
import pytest
from .base import Util

token = Util().get_token()


class TestRequests:
    def test_addmember_post(self):
        addmember_json = {"userid": "zsaa",
                          "name": "张三",
                          "alias": "jackzhan",
                          "mobile": "+86 13800000066",
                          "department": [1]}
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
                          json=addmember_json)
        print(r.json())

    def test_delemember_get(self):
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=JiangXiaoMing")
        print(r.json())

    def test_updatemember_post(self):
        update_json = {"userid": "zhangs",
                       "name": "张三哥",
                       "alias": "jackzhan",
                       "mobile": "+86 13800000066",
                       "department": [1]}
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}", json=update_json)
        print(r.json())

    def test_search_get(self):
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=JiangChen")
        print(r.json())
