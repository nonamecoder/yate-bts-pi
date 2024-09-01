#!/bin/bash

if [ -d "/usr/local/share/yate/nipc_web" ]; then
    sudo apt update
    sudo apt install -y apache2 php
    sudo chmod -R a+rw /usr/local/etc/yate/
    sudo ln -s /usr/local/share/yate/nipc_web/ /var/www/html/nipc
    sudo service apache2 restart
    echo "Apache2 and PHP have been installed successfully, and the NiPC web application has been set up."
else
    echo "YateBTS is not installed. Please install YateBTS first."
fi
