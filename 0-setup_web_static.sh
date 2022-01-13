#!/usr/bin/python3
# Bash script that sets up web servers


sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_stati/{releases/test,shared}

echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee -a /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
cont="\\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i 45i $cont" /etc/nginx/sites-available/default
sudo service nginx reload
sudo service nginx start
