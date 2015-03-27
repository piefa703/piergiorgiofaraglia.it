#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import hashlib
import os

#########
# PATHS #
#########
BASEDIR = os.path.dirname(os.path.realpath(__file__)) 

DOMAIN = 'piergiorgiofaraglia.local'

AUTHOR = u'Piergiorgio Faraglia'
SITENAME = u'Piergiorgio Faraglia'
SITEURL = 'http://' + DOMAIN

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = u'it'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# FEED RSS
FEED_DOMAIN = 'http://feeds.' + DOMAIN
FEED_ALL_RSS = 'all.rss.xml'
CATEGORY_FEED_RSS = '%s.rss.xml'


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/xm3ron'),
    ('linkedin', 'https://it.linkedin.com/in/piergiorgiofaraglia'),
    ('facebook', 'https://www.facebook.com/p.faraglia'),
    ('rss', FEED_DOMAIN + '/' + FEED_ALL_RSS),
    #('github', 'https://github.com/xm3ron'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Chi sono', '/pages/chi-sono.html'),
    ('Servizi', '/pages/servizi.html'),
    ('Portfolio', '/pages/portfolio.html'),
    ('Blog', '/blog_index.html'),
    ('Contatti', '/pages/contatti.html'),
)

# Page
#PAGE_URL = '{slug}'
#PAGE_SAVE_AS = '{slug}.html'
#PAGE_PATHS = ['']

THEME = "/Users/xm3ron/projects/piergiorgiofaraglia.it/themes/pjport"

###########
# PLUGINS #
###########
PLUGIN_PATHS = [os.path.join(BASEDIR, 'plugins')]
PLUGINS = ['gravatar', ]

# GRAVATAR PLUGIN
AUTHOR_EMAIL = 'p.faraglia@gmail.com'

########################################
# Dev settings (Remove on production!) #
########################################
LOAD_CONTENT_CACHE = False

INDEX_SAVE_AS = 'blog_index.html'

DEFAULT_DATE_FORMAT = ('- %d -<br/>%B<br/>%Y')

STATIC_PATHS = ['images', 'bin', ]
