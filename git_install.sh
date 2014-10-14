#!/bin/bash 
# for centos 6

cd /opt
wget  http://zy-res.oss-cn-hangzhou.aliyuncs.com/git/v2.1.2.tar.gz
tar xf v2.1.2.tar.gz
cd git-2.1.2/
yum install -y autoconf gcc zlib-devel gettext  perl-ExtUtils-MakeMaker openssl-devel curl-devel expat-devel
make configure
./configure --prefix=/usr
make -j4
make install
git --version
