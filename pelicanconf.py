#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Youri Mouton & Calum Macrae'
SITENAME = u'Save OS X!'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('The Unix Forum', 'unixhub.net'),
          ('Our pkgin repo', 'saveosx.org/packages'),)

# Social widget
SOCIAL = (('Youri\'s twitter', 'https://twitter.com/YouriMouton'),
          ('Youri\'s github', 'https://github.com/yrmt'),
          ('Youri\'s last.fm', 'http://www.last.fm/user/Beastie_'),
	      ('Calums\'s github', 'https://github.com/phyrne'),
          ('The Unix Forum', 'http://unixhub.net'),
          ('Our pkgin repo', 'http://saveosx/org/packages'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "pelican-bootstrap3"
TWITTER_USERNAME = "YouriMouton"
GOOGLE_ANALYTICS = "UA-44722172-1"
