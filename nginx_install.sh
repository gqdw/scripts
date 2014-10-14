cd /opt
wget http://t-down.oss-cn-hangzhou.aliyuncs.com/nginx-1.6.0.tar.gz
tar xf nginx-1.6.0.tar.gz
cd nginx-1.6.0
yum install -y  pcre-devel zlib-devel
./configure --prefix=/alidata/nginx
make -j4
make install

