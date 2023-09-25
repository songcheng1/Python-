# Centos 安装python3

# 编译python源码时，需要一些依赖包，一次安装完毕

```
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel

yum install gcc gcc-c++ openssl-devel libffi-devel tk-devel

```
# 安装wget

```
yum install wget
```

# 下载python源码包

``` wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz ```

# 解压安装&编译

```
# 解压压缩包
tar -zxvf Python-3.8.5.tgz  

# 进入文件夹
cd Python-3.8.5

# 配置安装位置
./configure prefix=/usr/local/python3

# 安装
make && make install
```
# 添加软连接

```
#添加python3的软链接 
ln -s /usr/local/python3/bin/python3.8 /usr/bin/python3 

#添加 pip3 的软链接 
ln -s /usr/local/python3/bin/pip3.8 /usr/bin/pip3

或者

#添加python3的软链接 
ln -s /usr/local/python3/bin/python3.8 /usr/bin/python

#添加 pip3 的软链接 
ln -s /usr/local/python3/bin/pip3.8 /usr/bin/pip

```

# 配置环境变量
```vi /etc/profile```

最后一行添加:

```
export PYTHON_HOME=/usr/local/python3

export PATH=$PYTHON_HOME/bin:$PATH
```

# 保存退出后 执行 source /etc/profile 执行环境变量文件后生效


# pycharm 激活码--有效期2023.7

WDV7B5UM4J-eyJsaWNlbnNlSWQiOiJXRFY3QjVVTTRKIiwibGljZW5zZWVOYW1lIjoia2lkZHkgaW5zZWFtcyIsImFzc2lnbmVlTmFtZSI6IiIsImFzc2lnbmVlRW1haWwiOiIiLCJsaWNlbnNlUmVzdHJpY3Rpb24iOiIiLCJjaGVja0NvbmN1cnJlbnRVc2UiOmZhbHNlLCJwcm9kdWN0cyI6W3siY29kZSI6IlBTSSIsImZhbGxiYWNrRGF0ZSI6IjIwMjUtMDgtMDEiLCJwYWlkVXBUbyI6IjIwMjUtMDgtMDEiLCJleHRlbmRlZCI6dHJ1ZX0seyJjb2RlIjoiUFBDIiwiZmFsbGJhY2tEYXRlIjoiMjAyNS0wOC0wMSIsInBhaWRVcFRvIjoiMjAyNS0wOC0wMSIsImV4dGVuZGVkIjp0cnVlfSx7ImNvZGUiOiJQQ1dNUCIsImZhbGxiYWNrRGF0ZSI6IjIwMjUtMDgtMDEiLCJwYWlkVXBUbyI6IjIwMjUtMDgtMDEiLCJleHRlbmRlZCI6dHJ1ZX0seyJjb2RlIjoiUEMiLCJmYWxsYmFja0RhdGUiOiIyMDI1LTA4LTAxIiwicGFpZFVwVG8iOiIyMDI1LTA4LTAxIiwiZXh0ZW5kZWQiOmZhbHNlfSx7ImNvZGUiOiJQV1MiLCJmYWxsYmFja0RhdGUiOiIyMDI1LTA4LTAxIiwicGFpZFVwVG8iOiIyMDI1LTA4LTAxIiwiZXh0ZW5kZWQiOnRydWV9XSwibWV0YWRhdGEiOiIwMTIwMjIwODAxUFNBTjAwMDAwNSIsImhhc2giOiJUUklBTDoyNjMyMTUzOTMiLCJncmFjZVBlcmlvZERheXMiOjcsImF1dG9Qcm9sb25nYXRlZCI6ZmFsc2UsImlzQXV0b1Byb2xvbmdhdGVkIjpmYWxzZX0=-S44u4zyBrYbltQAZezyCkBYsVU9HRftkKneJSWd2SsZMxgJiA1JfkhEl2yc4zrXBBqCCn2PKpaw8noyremrYtur0Iz93xp1geS6VSI4t5w5jgHR1CEUcL9Ia4BIl3CIMkxR3WXPrSGAt9jVitTmmCGGO9swTN4Hxey4iNNsEhkp8LDG949kRhN1ly00RH+p+rUP+FdVxwZ7e06rIV1c/8MGoJi4Z+7oyi+WnfIP+QIwxoNa60dzshI9Ep9d0p6bIR6eBKbNkfooWmp87mpOyN5QPupwF4q1KgS+LbFTeY/zZK6yP7tj+T2rbE3WI8MhnIviArGLs9DjZm20MwZTWvg==-MIIETDCCAjSgAwIBAgIBDTANBgkqhkiG9w0BAQsFADAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBMB4XDTIwMTAxOTA5MDU1M1oXDTIyMTAyMTA5MDU1M1owHzEdMBsGA1UEAwwUcHJvZDJ5LWZyb20tMjAyMDEwMTkwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCUlaUFc1wf+CfY9wzFWEL2euKQ5nswqb57V8QZG7d7RoR6rwYUIXseTOAFq210oMEe++LCjzKDuqwDfsyhgDNTgZBPAaC4vUU2oy+XR+Fq8nBixWIsH668HeOnRK6RRhsr0rJzRB95aZ3EAPzBuQ2qPaNGm17pAX0Rd6MPRgjp75IWwI9eA6aMEdPQEVN7uyOtM5zSsjoj79Lbu1fjShOnQZuJcsV8tqnayeFkNzv2LTOlofU/Tbx502Ro073gGjoeRzNvrynAP03pL486P3KCAyiNPhDs2z8/COMrxRlZW5mfzo0xsK0dQGNH3UoG/9RVwHG4eS8LFpMTR9oetHZBAgMBAAGjgZkwgZYwCQYDVR0TBAIwADAdBgNVHQ4EFgQUJNoRIpb1hUHAk0foMSNM9MCEAv8wSAYDVR0jBEEwP4AUo562SGdCEjZBvW3gubSgUouX8bOhHKQaMBgxFjAUBgNVBAMMDUpldFByb2ZpbGUgQ0GCCQDSbLGDsoN54TATBgNVHSUEDDAKBggrBgEFBQcDATALBgNVHQ8EBAMCBaAwDQYJKoZIhvcNAQELBQADggIBABqRoNGxAQct9dQUFK8xqhiZaYPd30TlmCmSAaGJ0eBpvkVeqA2jGYhAQRqFiAlFC63JKvWvRZO1iRuWCEfUMkdqQ9VQPXziE/BlsOIgrL6RlJfuFcEZ8TK3syIfIGQZNCxYhLLUuet2HE6LJYPQ5c0jH4kDooRpcVZ4rBxNwddpctUO2te9UU5/FjhioZQsPvd92qOTsV+8Cyl2fvNhNKD1Uu9ff5AkVIQn4JU23ozdB/R5oUlebwaTE6WZNBs+TA/qPj+5/we9NH71WRB0hqUoLI2AKKyiPw++FtN4Su1vsdDlrAzDj9ILjpjJKA1ImuVcG329/WTYIKysZ1CWK3zATg9BeCUPAV1pQy8ToXOq+RSYen6winZ2OO93eyHv2Iw5kbn1dqfBw1BuTE29V2FJKicJSu8iEOpfoafwJISXmz1wnnWL3V/0NxTulfWsXugOoLfv0ZIBP1xH9kmf22jjQ2JiHhQZP7ZDsreRrOeIQ/c4yR8IQvMLfC0WKQqrHu5ZzXTH4NO3CwGWSlTY74kE91zXB5mwWAx1jig+UXYc2w4RkVhy0//lOmVya/PEepuuTTI4+UJwC7qbVlh5zfhj8oTNUXgN0AOc+Q0/WFPl1aw5VV/VrO8FCoB15lFVlpKaQ1Yh+DVU8ke+rt9Th0BCHXe0uZOEmH0nOnH/0onD

# 定期清除日志信息（每周一的0点,清除上上周日志信息）

  0 0 * * 1  find /tmp/log/  -name "*.log" -mtime +6 -exec rm {} \\; 

# linux 执行curl
FILE_PATH=`curl -k -s -F "_api_key=81d68433aefc538985ceb" -F "buildKey=xxxx.apk" https://xxx.xxx.xxx/xxx/app/xxxx`

result=$(python -c "import json; k_json=json.loads('$FILE_PATH');print (k_json['data']['buildQRCodeURL'])")
echo $result
  
  



# Centos miniconda 快捷安装配置python3

1. https://docs.conda.io/projects/miniconda/en/latest/

2. source .bashrc

3.conda create --name python3 python=3.11

4. conda activate python3

