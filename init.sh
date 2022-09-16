sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart
gunicorn -b 0.0.0.0:8080 hello:app
gunicorn -b 0.0.0.0:8000 ./ask/ask/wsgi:django