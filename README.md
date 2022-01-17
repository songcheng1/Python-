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

