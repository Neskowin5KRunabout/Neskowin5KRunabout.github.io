# Copyright 2011 Digital Inspiration
# http://www.labnol.org/

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
  def get (self, q):
    if q is None:
      q = 'index.html'

    path = os.path.join (os.path.dirname (__file__), q)
    self.response.headers ['Content-Type'] = 'text/html'
    self.response.out.write (template.render (path, {}))

    
import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, WebApp World!')

app = webapp2.WSGIApplication([('/', MainPage)])
