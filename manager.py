import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import logg
import mock.mock_json
import requests
from data.data_source import DATAS


class API(object):
    def __init__(self):
        self.ip = ''
        self.url = ''
        self.route = ''
        self.method = ''
        self.data = ''
        self.res = ''
        self.mock = mock.mock_json.MOCKJSON()

    def main(self, api_data, header):
        self.ip = api_data['url']
        self.route = api_data['api_name']
        self.method = api_data['api_method']
        self.url = self.ip + self.route
        if self.method.upper() == "GET":
            self.data = self.mock.get_api_info(api_data["info"])
            self.resquest_case(self.data, methods='GET', header=header)
        elif self.method.upper() == "POST":
            self.data = self.mock.get_api_info(api_data["info"])
            self.resquest_case(self.data, methods='POST', header=header)
        elif self.method.upper() == "PUT":
            self.data = self.mock.get_api_info(api_data["info"])
            self.resquest_case(self.data, methods='PUT', header=header)

    def resquest_case(self, api_data, methods, header):
        for api_json in self.mock.get_case_list(api_data[1], **api_data[0]):
            print(api_json)
            self.requests_api(methods, api_json, header)

    @logg.api_log
    def requests_api(self, methods, api_json, header):
        self.api_json = api_json
        if methods.upper() == 'GET':
            self.res = requests.get(url=self.url, data=self.api_json, headers=header)
        elif methods.upper() == 'POST':
            self.res = requests.post(url=self.url, json=self.api_json, headers=header)
        elif methods.upper() == 'PUT':
            self.res = requests.put(url=self.url, json=self.api_json, headers=header)


if __name__ == '__main__':
    headers = {
        "authorization": 'Basic dGVzdHFlOmJ6c3RxZQ=='
    }
    api = API()
    data = DATAS().get_api_data()
    for i in range(len(data)):
        if i == 0:
            api.main(data[i], headers)