"""Get the application version."""
import json
import webapp2

class VersionPage(webapp2.RequestHandler):
    """Version class."""

    def get(self):
        """Get method."""
        data = {'message':'success'}

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(data))

app = webapp2.WSGIApplication([
    ('/_bo/system/version', VersionPage)
], debug=True)