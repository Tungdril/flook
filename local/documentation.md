# Pi networking commands
Get public IP:
- curl ipinfo.io/ip

Start/Stop/Restart Apache 2
- sudo service apache2 start
- sudo service apache2 stop
- sudo service apache2 restart

Apache 2 status:
- sudo systemctl status apache2.service

Clone repo to Apache 2 directory:
- sudo git clone https://github.com/Tungdril/flooker.git /var/www/flook.de/public_html

Update repo from source:
- cd /var/www/flook.de/public_html
- sudo git pull origin main

Start MySQL:
- sudo mysql -u root -p
To exit:
- quit() 