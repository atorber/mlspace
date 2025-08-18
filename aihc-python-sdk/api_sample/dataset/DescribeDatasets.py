'''
基础客户端示例
'''

# !/usr/bin/env python
# coding=utf-8

import sys

from baidubce.exception import BceHttpClientError, BceServerError
# from baidubce.services.aihc.aihc_model import JobConfig
from baidubce.services.aihc.aihc_client import AihcClient

import json
import logging

from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials

from baidubce.exception import BceHttpClientError, BceServerError


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


def to_dict(obj):
    """
    将对象转换为字典格式。
    
    递归地将Python对象（包括自定义对象、字典、列表）转换为纯字典格式，
    便于JSON序列化和调试输出。
    
    Args:
        obj: 要转换的对象，可以是字典、列表、自定义对象或基本类型
        
    Returns:
        dict/list/基本类型: 转换后的字典、列表或基本类型值
        
    Examples:
        >>> obj = SomeClass()
        >>> obj.name = "test"
        >>> result = to_dict(obj)
        >>> print(result)
        {'name': 'test'}
    """
    if isinstance(obj, dict):
        return {k: to_dict(v) for k, v in obj.items()}
    elif hasattr(obj, '__dict__'):
        return {k: to_dict(v) for k, v in obj.__dict__.items()}
    elif isinstance(obj, list):
        return [to_dict(i) for i in obj]
    else:
        return obj


def main():
    """
    主函数，演示AIHC服务的各种操作。
    
    本函数展示了AihcClient的完整使用流程，包括：
    1. 创建AIHC客户端实例
    2. 查询任务列表和详情
    3. 查询各种资源列表（数据集、模型、服务、开发机）
    4. 完整的错误处理机制
    
    注意：
    - 部分功能（如创建、更新、删除任务）被注释掉，避免误操作
    - 所有API调用都包含完整的异常处理
    - 响应数据会被转换为JSON格式输出
    
    Raises:
        BceHttpClientError: 当API调用失败时抛出
        BceServerError: 当服务器返回错误时抛出
    """

    dataset_id = None
    version_id = None

    # create a aihc client
    aihc_client = AihcClient(config)

    # 查询数据集列表
    try:
        __logger.info('--------------------DescribeDatasets start--------------------')
        response = aihc_client.dataset.DescribeDatasets()
        print(json.dumps(to_dict(response), ensure_ascii=False))
        __logger.info('DescribeDatasets: %s', response.__dict__.keys())
        dataset_id = response.datasets[0].id
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, str(e.last_error)))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # 查询数据集详情
    try:
        __logger.info('--------------------DescribeDataset start--------------------')
        response = aihc_client.dataset.DescribeDataset(datasetId=dataset_id)
        print(json.dumps(to_dict(response), ensure_ascii=False))
        __logger.info('DescribeDataset: %s', response.__dict__.keys())
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, str(e.last_error)))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # 获取数据集版本列表
    try:
        __logger.info('--------------------DescribeDatasetVersions start--------------------')
        response = aihc_client.dataset.DescribeDatasetVersions(datasetId=dataset_id)
        print(json.dumps(to_dict(response), ensure_ascii=False))
        __logger.info('DescribeDatasetVersions: %s', response.__dict__.keys())
        version_id = response.versions[0].id
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, str(e.last_error)))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # 获取数据集版本详情
    try:
        __logger.info('--------------------DescribeDatasetVersion start--------------------')
        response = aihc_client.dataset.DescribeDatasetVersion(datasetId=dataset_id, versionId=version_id)
        print(json.dumps(to_dict(response), ensure_ascii=False))
        __logger.info('DescribeDatasetVersion: %s', response.__dict__.keys())
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, str(e.last_error)))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # 修改数据集
    try:
        __logger.info('--------------------ModifyDataset start--------------------')
        response = aihc_client.dataset.ModifyDataset(datasetId=dataset_id, name='test_dataset_2xxx')
        print(json.dumps(to_dict(response), ensure_ascii=False))
        __logger.info('ModifyDataset: %s', response.__dict__.keys())
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, str(e.last_error)))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # 删除数据集
    try:
        __logger.info('--------------------DeleteDataset start--------------------')
        response = aihc_client.dataset.DeleteDataset(datasetId=dataset_id)
        print(json.dumps(to_dict(response), ensure_ascii=False))
        __logger.info('DeleteDataset: %s', response.__dict__.keys())
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, str(e.last_error)))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

if __name__ == '__main__':
    main()