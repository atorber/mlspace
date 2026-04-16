'''
基础客户端示例
'''

# !/usr/bin/env python
# coding=utf-8

import sys

from baidubce.exception import BceHttpClientError, BceServerError
from baidubce.services.aihc.aihc_client import AihcClient
from baidubce.http import http_methods

import json
import logging

from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials

HOST = 'aihc host'
AK = 'your-access-key-id'
SK = 'your-secret-access-key'

logger = logging.getLogger('baidubce.http.aihc_http_client')
fh = logging.FileHandler('sample.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)

config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', force=True)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("baidubce").setLevel(logging.INFO)
__logger = logging.getLogger(__name__)
__logger.setLevel(logging.INFO)

aihc_client = AihcClient(config)

def main():
    '''
    基础客户端示例
    '''
    try:
        response = aihc_client.base_client._send_request(http_methods.GET, b'/', params={'action': 'DescribeDatasets'})
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('BceServerError: %s', e.last_error.message)
        else:
            __logger.error('BceHttpClientError: %s', e.last_error.message)

if __name__ == '__main__':
    main()