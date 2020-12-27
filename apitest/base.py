import pytest
import requests


class Util():
    def get_token(self):
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww0a755c411005b357&corpsecret=-tzXl87I-yRulX0ikZQGqnJ4Th2qfBgpRa_1H3FcmG0")
        print(r.json()['access_token'])
        return r.json()['access_token']
