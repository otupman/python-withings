# -*- coding: utf-8 -*-

"""
Python library for the Withings API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Withings Body metrics Services API
<http://www.withings.com/en/api/wbsapiv2>

Uses Oauth 1.0 to authentify. You need to obtain a consumer key
and consumer secret from Withings by creating an application
here: <https://oauth.withings.com/partner/add>

Usage:

auth = WithingsAuth(CONSUMER_KEY, CONSUMER_SECRET)
authorize_url = auth.get_authorize_url()
print "Go to %s allow the app and copy your oauth_verifier" % authorize_url
oauth_verifier = raw_input('Please enter your oauth_verifier: ')
creds = auth.get_credentials(oauth_verifier)

client = WithingsApi(creds)
measures = client.get_measures(limit=1)
print "Your last measured weight: %skg" % measures[0].weight

"""

from withings.core import WithingsCredentials, WithingsAuth, WithingsApi
from withings.core import WithingsMeasureGroup, WithingsMeasures
from withings.core import WithingsActivityGroup, WithingsSleepSummaryGroup

__title__ = 'withings'
__version__ = '0.4.0'
__author__ = 'Maxime Bouroumeau-Fuseau'
__license__ = 'MIT'
__copyright__ = 'Copyright 2012 Maxime Bouroumeau-Fuseau'

__all__ = (
    'WithingsCredentials',
    'WithingsAuth',
    'WithingsApi',
    'WithingsMeasures',
    'WithingsMeasureGroup',
    'WithingsActivityGroup',
    'WithingsSleepSummaryGroup',
)
