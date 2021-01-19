import os
import sys
import json
import requests

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from base_wechat import BaseWechat


class Requests(BaseWechat):
    def __init__(self, logger=None, debug=True):
        super().__init__(logger, debug)

    def get(self, url, params=None, headers=None, **kwargs):
        # self.logger('http get: {}'.format(locals()))
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        } if not headers else headers

        response = requests.get(url, params=params, headers=headers, **kwargs)

        return response

    def post(self, url, data=None, headers=None, **kwargs):
        # self.logger('http post: {}'.format(locals()))
        headers = {
            "Content-Type": "application/json",
        } if not headers else headers
        data = json.dumps(data) if headers['Content-Type'] == 'application/json' else data

        response = requests.post(url, data=data, headers=headers, **kwargs)

        return response

    def delete(self, url, data=None, headers=None, **kwargs):
        # self.logger('http delete: {}'.format(locals()))
        headers = {
            "Content-Type": "application/json",
        } if not headers else headers
        data = json.dumps(data) if headers['Content-Type'] == 'application/json' else data

        response = requests.delete(url, data=data, headers=headers, **kwargs)

        return response
