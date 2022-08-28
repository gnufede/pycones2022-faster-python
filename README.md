
## Research (WIP)

Run some benchmarks for python code and web applications.

The goal is to compare cpython 3.9 (baseline) to 
- cpython 3.11-rc
- pypy 3.9
- nuitka

and more

### Script

``` sh
$ cd research/script
$ docker-compose up
```

### Realworld

Based on [Flask realworld example app]( https://github.com/gothinkster/flask-realworld-example-app)

#### Preparation

``` sh
$ cd research/realworld
$ mkdir postgres_data
$ docker-compose run cpython39 /script.sh
```

Containers may get stuck running, do a `docker-compose stop` in that case.
Wrk may fail early if the backend is not ready, just rerun `up` the command.

``` sh
$ cd research/realworld
$ web=pypy39 docker-compose up wrk
```
