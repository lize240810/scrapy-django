import os
import django

# # scrapy项目中使用django的model
os.environ['DJANGO_SETTINGS_MODULE'] = 'tax_scrapy.django_db.django_db.settings'
django.setup()

import pymysql
pymysql.install_as_MySQLdb()