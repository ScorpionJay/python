# flask demo

- [flask](http://flask.pocoo.org)
- [uwsgi](https://uwsgi-docs.readthedocs.io)

> nginx config

```
server{
        listen  8000;
        server_name localhost;

        location / {
                include         uwsgi_params;
                uwsgi_pass      127.0.0.1:8888;
                uwsgi_param     UWGI_SCRIPT manage:app;
        }
}
```

> uwsgi config

```
[uwsgi]

socket = 127.0.0.1:8888
processes = 4
threads = 2
master = true
pythonpath = /home/jay/Documents/python/flask
wsgi-file = /home/jay/Documents/python/flask/dy.py
module = manage
callable = app
memory-report = true
daemonize = /home/jay/Documents/python/flask/server.log
```
