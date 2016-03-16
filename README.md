Atifier
--------

Generate RSS/Atom feed from changes in or in a specific region of a web page.

Installation
-------------

There are two dependencies for the project:
* django v1.9+
* node.js v4.4.0+

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
$ python manage.py createsuperuser
$ python manage.py runserver
```

For the scraper:

```
# Now for the scraper separately
$ cd atifier/scraper
$ touch debug.js
# Add the LOAD_IMAGES, USER_AGENT,VIEWPORT_SIZE attributes in the debug.js
# Example:
# module.exports = {
#   USER_AGENT = "...",
#   LOAD_IMAGES = true,
#   VIEWPORT_SIZE = {
#       width: 1366,
#       height: 768
#   }
# }
$ npm install
```

Add a cron entry in `/etc/cron.d/crontab`:

```
* * * * * ubuntu cd /home/ubuntu/atifier/server && source /home/ubuntu/at_env/bin/activate && python manage.py poll_urls
```

Login the django admin at `http://localhost:8000/admin/` and create the
pages you want to track along with the DOM selectors (sent to
`document.querySelector`) and an interval in minutes the page has to be
scraped (valid value between 0 and 59).
