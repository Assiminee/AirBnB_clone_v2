#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install -y nginx

html=\
"<html>
\t<head>
\t</head>
\t<body>
\t\tHolberton School
\t</body>
</html>
"

[ -d /data/ ] || sudo mkdir /data/
[ -d /data/web_static/ ] || sudo mkdir /data/web_static/
[ -d /data/web_static/releases/ ] || sudo mkdir /data/web_static/releases/
[ -d /data/web_static/shared/ ] || sudo mkdir /data/web_static/shared/
[ -d /data/web_static/releases/test/ ] || sudo mkdir /data/web_static/releases/test/
[ -f /data/web_static/releases/test/index.html ] || echo -e "$html" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

sudo sed -i '/rewrite/a\\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}' /etc/nginx/sites-enabled/default

sudo service nginx restart
