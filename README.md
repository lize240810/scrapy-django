# scrapy + Django 
> scrapy 爬虫使用django模型操数据库
## 1. 创建scrapy项目
```
scrapy startproject tax-scrapy
```
## 2. 进入scrapy项目创建spider文件
```
cd tax_scrapy
scrapy genspider example example.com
```

## 3. 创建django项目
> 目录不需要退回 直接在爬虫的目录下
```
django-admin startproject django_db
```

## 4. 创建django app
```
python manage.py startapp creditchina
```

## 5. 修改django settings 文件
```py
# 添加当前环境
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR))

# 注册app
INSTALLED_APPS = [
    ...
    'creditchina',
]
```
## 6. 到scrapy的__init__.py 文件中引入 django项目的model
```
import os
import django

# # scrapy项目中使用django的model
os.environ['DJANGO_SETTINGS_MODULE'] = 'tax_scrapy.django_db.django_db.settings'
django.setup()

import pymysql
pymysql.install_as_MySQLdb()
```

## 7. 在爬虫中引入django model
```
# -*- coding: utf-8 -*-
import scrapy

from creditchina.models import NameItem


class CreditchinaSpider(scrapy.Spider):
    name = 'creditchina'
    allowed_domains = ['.gov.cn/']
    start_urls = ['http://https://www.creditchina.gov.cn//']

    def parse(self, response):
        print(NameItem)

```