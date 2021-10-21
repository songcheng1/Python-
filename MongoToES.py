from pymongo import MongoClient
import requests
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

# 示例
# 删除：requests.delete(f'{es_url}{db}')
# 插入：requests.put(f'{es_url}{db}')
# 插入：requests.post(f'{es_url}{db}/{table}')

es_url = 'http://host:9200/'
mongo_url = 'mongo_host:27017'
# DB = 'quotation_collection_test'
DB = 'quotation_collection'
COLLECTION = 'quotationSheet'

def insert(data):
    _id = data.pop('_id')
    data.pop('url', '')
    if data['quotation'] == float('inf'):
        data['quotation'] = 999999999999
    return requests.put(url=f'{es_url}{DB}/{COLLECTION}/{_id}', json=data)

if __name__ == '__main__':
    client = MongoClient(mongo_url)
    db_mongo = client[DB]
    mongoRecordRes = db_mongo[COLLECTION].find()

    # 起30个线程同时进行数据同步
    with ThreadPoolExecutor(30) as executor:
        # 返回一个迭代器：Returns an iterator equivalent to map(fn, iter).
        for result in executor.map(insert, mongoRecordRes):
            print(result.status_code, result.text)
