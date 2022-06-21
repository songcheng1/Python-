# coding:utf-8
# 参考
# 算法一

import hashlib


def md5hex(word): 
    if isinstance(word, unicode): 
        word = word.encode("utf-8") 
    elif not isinstance(word, str): 
        word = str(word) 
    m = hashlib.md5() 
    m.update(word)
    return m.hexdigest()


# 参数名
paramas_name=[
    'android_id',
    'channel',
    'deviceId',
    'device_fingerprint',
    'imei',
    'lang',
    'password',
    'phone',
    'platform',
    'sid',
    'start',
    't',
    'type',
    'versionName',
    'zone'
    ]


#按参数名顺序传入参数值列表，无参数名留空值
def get_sign(paramas_value):
    key=''
    for index,item in enumerate(paramas_value):
        if item!='':
            key=key+paramas_name[index]+'%3D'+item
    deviceId=paramas_value[2]
    v1_2 = bytearray(key, 'utf-8')
    v5_1 = ''
    v3_2 = 0
    v2 = 0
    v4_1=bytearray(deviceId, 'utf-8')

    while v2<len(v1_2):
        v5_1 = v5_1 + str(v1_2[v2] ^ v4_1[v3_2 ])
        v3_2 = (v3_2 + 1) % len(v4_1)
        v2 = v2 + 1

    sign=md5hex(md5hex(v5_1)+deviceId)
    return sign


# 算法二
import urllib
import urllib.parse
import hashlib


def sign_with_query_items(data):
    udid = data['deviceId']
    # 将请求参数按key排序
    data = {k: data[k] for k in sorted(data.keys())}
    # 拼接成字符串
    data_str = ''
    for k, v in data.items():
        data_str += '{}={}'.format(k, v)
    data_str = urllib.parse.quote(data_str, 'utf-8')
    # 将url encode之后的字符串的每个字符与对应的udid字符进行异或原形
    xor_str = ''
    udid_length = len(udid)
    for i in range(len(data_str)):
        data_char = data_str[i]
        udid_index = int(i % udid_length)
        udid_char = udid[udid_index]
        rst = ord(udid_char) ^ ord(data_char)
        xor_str += str(rst)

    # 对异或后的字符串MD5
    md5 = hashlib.md5()
    md5.update(xor_str.encode())
    md5_str = md5.hexdigest()

    # 将MD5后的字符串和udid拼接起来，再次MD5
    md5_str += udid
    md5 = hashlib.md5()
    md5.update(md5_str.encode())
    md5_str = md5.hexdigest()
    return md5_str
if __name__ == '__main__':
      params = {
        "deviceId": "",
        "device_fingerprint": "",
        "device_fingerprint1": "",
        "fid": "",
        "lang": "",
        "page": "",
        "page_pos": "",
        "page_size": "",
        "platform": "",
        "sid": "",
        "sort": "",
        "source": "",
        "t": ""
      }
      print(sign_with_query_items(params))

# 算法三

import hashlib

x_sign = "X"
# api = "/fe_api/burdock/v2/user/keyInfo/${userId}"
api = "/fe_api/burdock/v2/user/keyInfo/6011212c000000000101e7f4"
m = hashlib.md5()
m.update((api + "WSUDD").encode())
sign = x_sign + m.hexdigest()
print(sign)
    
