#!/usr/bin/env python
# imports
import webapp2
import helloworld
import logging

class BitmexDownloadController(webapp2.RequestHandler):

    def get(self): # This method gets called for incoming GET requests to this endpoint.

        self.response.status = 200
        self.response.headers["Content-Type"] = "text/html; charset=utf-8"
        self.response.write("HELLO FROM BitmexDownloadController")
        logging.debug("IGOR DEBUG: ****** CALL BitmexDownloadController")
        logging.error("IGOR: ****** CALL BitmexDownloadController")

# Requested URLs that are not listed here return with a 404

app = webapp2.WSGIApplication([
  ('/', helloworld.MainController),
  ('/tasks/bitmex-download', BitmexDownloadController)
], debug=True)
