#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

#########
# PATHS #
#########
BASEDIR = os.path.dirname(os.path.realpath(__file__))
PATH = 'content'

DOMAIN = 'piergiorgiofaraglia.it'
SITEURL = 'http://' + DOMAIN
THEME_BASEURL = 'http://' + DOMAIN

AUTHOR = u'Piergiorgio Faraglia'
SITENAME = u'Piergiorgio Faraglia'

TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = u'it'
JINJA_EXTENSIONS = ['jinja2.ext.i18n', ]
I18N_GETTEXT_NEWSTYLE = True
I18N_TEMPLATES_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = 'all.rss.xml'
CATEGORY_FEED_RSS = '%s.rss.xml'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/xm3ron'),
    ('linkedin', 'https://it.linkedin.com/in/piergiorgiofaraglia'),
    ('facebook', 'https://www.facebook.com/p.faraglia'),
    ('rss', SITEURL + '/' +FEED_ALL_RSS),
)

DEFAULT_PAGINATION = 10

# Menu
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = ()

THEME = "/Users/xm3ron/projects/pelican-themes/pjport"

###########
# PLUGINS #
###########
PLUGIN_PATHS = [os.path.join(BASEDIR, 'plugins')]
PLUGINS = ['gravatar', 'sitemap', 'i18n_subsites', ]

#
# GRAVATAR PLUGIN
#
AUTHOR_EMAIL = 'p.faraglia@gmail.com'

#
# SITEMAP PLUGIN
#
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

#
# I18N SUBSITES PLUGIN
#
# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'en': {
        'SITENAME': 'Piergiorgio Faraglia',
    }
}

DEFAULT_DATE_FORMAT = ('- %d -<br/>%B<br/>%Y')

STATIC_PATHS = ['extra/CNAME', 'extra/robots.txt', 'bin', 'images', ]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/robots.txt': {'path': 'robots.txt'}, }

# contacts
CONTACT_EMAIL = 'pj80.forums@gmail.com'
CONTACT_PHONE = '+39 328 72 77 333'
CONTACT_CITY = 'Rome'

# GOOGLE ANALYTICS (set to  None if don't want it)
GOOGLE_ANALYTICS = 'UA-30758042-1'

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
INDEX_SAVE_AS = 'techblog/index.html'

PAGE_ORDER_BY = 'navbar-order'

BLOG_RELURL = 'techblog'
BLOG_NAME = 'TechBlog'
