#!/usr/bin/env python
# coding: utf-8

import os
import sys

# ��ϵͳ�ı�������ΪUTF8
reload(sys)
sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")#mysite�滻Ϊ�Լ�����Ŀ��

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()