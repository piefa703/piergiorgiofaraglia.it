#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

#########
# PATHS #
#########
BASEDIR = os.path.dirname(os.path.realpath(__file__)) 

AUTHOR = u'Piergiorgio Faraglia'
SITENAME = u'Piergiorgio Faraglia'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = u'it'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 2

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Menu
#DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Chi sono', '/pages/chi-sono.html'),
    ('Blog', '/blog_index.html'),
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

SOCIAL = (
    ('twitter', 'https://twitter.com/xm3ron'),
    ('github', 'https://github.com/xm3ron'),
    # facebook, flickr
)
