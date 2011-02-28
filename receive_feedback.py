# -*- coding: utf-8 -*-
# ###
# Copyright (c) 2010 Konstantinos Spyropoulos <inigo.aldana@gmail.com>
# Copyright (c) 2011 Nicolas Raoul
#
# This file is part of ankidroid-triage
#
# ankidroid-triage is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# ankidroid-triage is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with ankidroid-triage.
# If not, see http://www.gnu.org/licenses/.
# #####

import logging, email, re, hashlib
from datetime import datetime
from cgi import escape
from string import strip
from urllib import quote
from urllib import quote_plus
from quopri import decodestring
from email.header import decode_header
from google.appengine.api import mail
from google.appengine.ext import webapp
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api.urlfetch import fetch
from google.appengine.api.urlfetch import Error

from pytz.gae import pytz
from pytz import timezone, UnknownTimeZoneError
from BeautifulSoup import BeautifulStoneSoup
from BeautifulSoup import BeautifulSoup


class FeedbackReport(db.Model):
	nonce = db.StringProperty(required=True)
	feedback = db.TextProperty(required=True)
	#versionName = db.StringProperty()
	#androidOSVersion = db.StringProperty()

class HttpReceiver(webapp.RequestHandler):
	def post(self):
		post_args = self.request.arguments()
		for name in post_args:
			logging.debug("http receiver, " + name + ": " + self.request.get(name, 0))
		self.response.out.write("OK got it!")
		
if __name__ == '__main__':
	main()

