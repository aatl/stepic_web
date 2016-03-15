sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.gunicorn.conf   /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/django.gunicorn.conf   /etc/gunicorn.d/django.gunicorn.conf
sudo /etc/init.d/gunicorn restart
