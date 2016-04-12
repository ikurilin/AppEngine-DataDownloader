import webapp2
import json

from util.json_serializer import JsonSerializer

class BitmexDownloadController(webapp2.RequestHandler):

    def get(self): # This method gets called for incoming GET requests to this endpoint.

        self.response.status = 200
        self.response.write("HELLO FROM BitmexDownloadController")