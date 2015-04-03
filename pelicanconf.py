#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

#########
# PATHS #
#########
BASEDIR = os.path.dirname(os.path.realpath(__file__))
PATH = 'content'

DOMAIN = 'technotes.piergiorgiofaraglia.it'
SITEURL = 'http://' + DOMAIN

AUTHOR = u'Piergiorgio Faraglia'
SITENAME = u'Technotes'

TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = u'en'

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
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Piergiorgio Faraglia', 'http://piergiorgiofaraglia.it'),
)

THEME = "/Users/xm3ron/projects/pelican-themes/pjport"

###########
# PLUGINS #
###########
PLUGIN_PATHS = [os.path.join(BASEDIR, 'plugins')]
PLUGINS = ['gravatar', 'sitemap', ]

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

DEFAULT_DATE_FORMAT = ('- %d -<br/>%B<br/>%Y')

STATIC_PATHS = ['extra/CNAME', 'extra/robots.txt', ]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/robots.txt': {'path': 'robots.txt'}, }

#
# pjport theme settings
#


# about me
ABOUT_ME = "I''m Piergiorgio Faraglia a computer engineer focused on software engineering and that is my tech blog. <br/>On this blog you can find my technology notes and you can navigate my projects and works"

# contacts
CONTACT_EMAIL = 'pj80.forums@gmail.com'
CONTACT_PHONE = '+39 328 72 77 333'
CONTACT_CITY = 'Rome'

# GOOGLE ANALYTICS (set to  None if don't want it)
GOOGLE_ANALYTICS = 'UA-30758042-2'
