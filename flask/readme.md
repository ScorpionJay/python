# flask demo

use flask uwsgi nginx to deploy a web application

## nginx config

```
server{
        listen  8000;
        server_name your domain;

        location / {
                include         uwsgi_params;
                uwsgi_pass      127.0.0.1:9090;
                uwsgi_param     UWGI_SCRIPT manage:app;
        }
}
```

## uwsgi install

[WSGI quickstart](https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html)

```
pip install uwsgi
```

## uwsgi config

```
[uwsgi]

socket = 127.0.0.1:9090
processes = 4
threads = 2
master = true
wsgi-file = /home/jay/Documents/python/flask/dy.py
module = manage
callable = app
memory-report = true
daemonize = /home/jay/Documents/python/flask/server.log
```

## start uwsgi

```
uwsgi uwsgi-config.ini

uwsgi --socket :9090 --plugin python  --wsgi-file foobar.py
```

## ref

- [flask](http://flask.pocoo.org)
- [uwsgi](https://uwsgi-docs.readthedocs.io)
