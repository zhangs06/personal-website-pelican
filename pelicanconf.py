#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ujaval Gandhi'
SITENAME = u"Spatial Thoughts"
SITEURL = ''
THEME = "/home/ujaval/projects/pelican-themes/pelican-bootstrap3"

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('QGIS', '/qgis'),
    ('OpenDataKit', '/opendatakit'),
    ('Websites', '/websites'),
    ('Blog', '/blog'),
)

PLUGINS = [
    'pelican_youtube',
]

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'


DISQUS_SITENAME = 'spatialthoughts'

ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{category}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{category}/{slug}/index.html'

CATEGORY_SAVE_AS = 'blog/{slug}/index.html'
CATEGORY_URL = 'blog/{slug}/'

ARCHIVES_SAVE_AS = 'blog/archives/index.html'
#FEED_ATOM = 'blog/feeds/'
#FEED_RSS = 'blog/feeds/'

TAG_SAVE_AS = False
TAG_URL = False
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

INDEX_SAVE_AS = 'blog/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GOOGLE_ANALYTICS_UNIVERSAL = 'UA-690672-12'
# Blogroll
LINKS = (('QGIS Tutorials and Tips', 'http://qgistutorials.com/'),
         ('GIS in India', 'http://www.gisinindia.com/'),
         ('GPS in India', 'http://www.gpsinindia.com/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/spatialthoughts'),
     ('github', 'https://github.com/spatialthoughts'),
     ('Google+', 'https://google.com/+UjavalGandhi'))

DEFAULT_PAGINATION = False


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
SITEMAP = {
        'format': 'xml',
        'changefreqs': {
            'articles': 'monthly',
            'indexes': 'daily',
            'pages': 'monthly'
            }
        }
