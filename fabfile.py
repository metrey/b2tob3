# -*- coding: utf-8 -*-
from fabric.api import local


def build_docs():
    local('python setup.py build_sphinx')


def docs():
    build_docs()
    local('python setup.py upload_sphinx')


def release():
    local('python setup.py sdist upload')


def git():
    local('git add . && git commit -a')
    local('git push')