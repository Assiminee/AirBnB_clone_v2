#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install -y nginx

html=\
"
<html>
\n\t<head>
\n\t</head>
\n\t<body>
\n\t\tHolberton School
\n\t</body>
\n</html>
"

[ -d /data/ ] || mkdir /data/
[ -d /data/web_static/ ] || mkdir /data/web_static/
[ -d /data/web_static/releases/ ] || mkdir /data/web_static/releases/
[ -d /data/web_static/shared/ ] || mkdir /data/web_static/shared/
[ -d /data/web_static/releases/test/ ] || mkdir /data/web_static/releases/test/
[ -f /data/web_static/releases/test/index.html ] || echo -e $html | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

sudo sed /rewrite/a\\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t} /etc/nginx/sites-enabled

sudo nginx -s reload
