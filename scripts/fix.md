./manage.py makemigrations
./manage.py migrate
sudo chown yy.www-data db.sqlite3
sudo chown yy.www-data .
./manage.py createsuperuser
sudo chmod 0664 db.sqlite3
sudo service apache2 restart
