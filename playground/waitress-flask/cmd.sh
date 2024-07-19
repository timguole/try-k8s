#!/bin/bash

exec waitress-serve --listen=*:80 wsgi:app
