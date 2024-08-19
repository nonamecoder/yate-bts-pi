./autogen.sh
./configure --prefix=/usr/local
make -j4
make install-noapi
ldconfig
