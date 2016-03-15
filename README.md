Atifier
--------

Generate RSS/Atom feed from changes in or in a specific region of a web page.

Installation
-------------

Run the following steps to install the server:

```
$ virtualenv at_env
$ source ~/at_env/bin/activate
$ git clone https://github.com/theju/atifier.git
$ cd atifier/server/
$ pip install -r requirements.txt
$ touch server/local.py
# Add the database settings and install the db driver
$ python manage.py migrate
$ python manage.py runserver
```

For the scraper:

```
# Now for the scraper separately
$ cd atifier/scraper
$ npm install
```

Add a cron entry in `/etc/cron.d/crontab`:

```
* * * * * ubuntu cd /home/ubuntu/atifier/server && source /home/ubuntu/at_env/bin/activate && python manage.py poll_urls
```
